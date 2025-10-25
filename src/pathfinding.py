import pygame
import heapq
import numpy as np

class Path:
    """
    Path-olio jolla on alku- ja loppupiste.
    Tallentaa yksittäisen polun listana pygame rect-olioita.
    Jokainen rect vastaa ruudukon yhtä ruutua.
    """

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.grid_cells = []
        self.cells = []

    def generate_cells(self, tile_size, left_buffer, buffer):
        """
        Luodaan pygame-rect oliot grid_cells sijainneista.
        Yksi ruudukon solu laajennetaan tile_size-kokoiseksi neliöksi pikselikoordinaatteihin.
        """
        
        self.cells = [
            pygame.Rect(
                left_buffer + col * tile_size,
                buffer + row * tile_size,
                tile_size,
                tile_size
            )
            for row, col in self.grid_cells
        ]

class Pathfinding:
    """
    Luodaan annetulle Dungeon-oliolle Pathfinding-olio,
    joka käyttää A*-algoritmia ja Manhattan-heuristiikkaa.
    Mikäli ruudukon sijainnissa on jo käyty, suositaan sitä jatkossa uusille, lähelle tuleville poluille.
    Tallennetaan kaikki polut listaan.
    """

    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.tiles_horizontal = dungeon.grid_width // dungeon.tile_size
        self.tiles_vertical = dungeon.grid_height // dungeon.tile_size
        self.grid_table = np.zeros((self.tiles_vertical, self.tiles_horizontal), dtype=int)

        self.paths = []
        self.extra_paths = []
        self.extra_path_count = 0

        self.find_all_paths()

    def pixel_to_grid(self, point):
        """
        Muuntaa pikselikoordinaatit grid_table solukoordinaateiksi (row, col).
        """

        px, py = point
        row = (py - self.dungeon.buffer) // self.dungeon.tile_size
        col = (px - self.dungeon.left_buffer) // self.dungeon.tile_size        
        return (row, col)

    def set_rooms_walkable(self):
        """
        Asettaa generoitujen huoneiden arvoksi 1 grid_tablessa.
        Tämä merkitsee sijaintia, jossa on jo olemassaoleva "käveltävissä oleva" tila, jota suositaan pathfindingissa.
        """

        self.grid_table.fill(0)

        for room in self.dungeon.rooms:
            row1, col1 = self.pixel_to_grid((room.left, room.top))
            row2, col2 = self.pixel_to_grid((room.right, room.bottom))
            self.grid_table[row1:row2, col1:col2] = 1

    def get_neighbors(self, node):
        """
        Palauttaa ei-diagonaaliset naapurit.
        """

        (row, col) = node
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []

        for drow, dcol in directions:
            neighbor_row, neighbor_col = row + drow, col + dcol
            if 0 <= neighbor_row < self.tiles_vertical and 0 <= neighbor_col < self.tiles_horizontal:
                neighbors.append((neighbor_row, neighbor_col))

        return neighbors

    def heuristic(self, a, b):
        """
        Manhattan-etäisyys.
        """

        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def reconstruct_path(self, came_from, current):
        """
        Kuljetaan reitti taaksepäin kunnes se ollaan käyty kokonaan läpi.
        Käännetään saatu tulos ympäri, jolloin saadaan lista kaikista reitin koordinaateista alusta maaliin.
        """

        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return total_path

    def A_Star(self, start, goal):
        """
        A*-algoritmi etsii lyhyimmän reitin kahden pisteen välillä.
        Algoritmi tutkii kunkin solun naapurit antaen niille arvon perustuen siihen,
        kuinka pitkän matkan olemme jo kulkeneet (g_score) ja kuinka pitkä matka naapurin kautta
        maaliin tulee yhteensä olemaan (f_score) perustuen valittuun Manhattan-heuristiikkaan (f(n)=g(n)+h(n)).
        Siirrytään soluun, jolle saadaan matalin arvo ja toistetaan, kunnes ollaan maalissa.
        Käytetään prioriteettijonoa heapq, joka säilöö solut pienimmän arvon mukaiseen järjestykseen.
        """
        
        open_set = [(0, start)]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            # heappop palauttaa solun jolla on pienin arvo
            _, current = heapq.heappop(open_set)

            # Maali saavutettu
            if current == goal:
                return self.reconstruct_path(came_from, current)
            
            # Mikäli naapurissa on käyty aikaisemmin, suosi sitä 
            for neighbor in self.get_neighbors(current):
                cost = 1
                if self.grid_table[neighbor[0], neighbor[1]] == 1:
                    cost = 0

                tentative_g = g_score[current] + cost

                if tentative_g < g_score.get(neighbor, np.inf):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None
    
    def find_all_paths(self):
        """
        Luo kaikki polut MST:n pisteiden (huoneiden keskipisteiden) välille.
        Tallentaa ne Path-olioina self.paths-listaan.
        """

        self.paths.clear()
        self.extra_paths.clear()
        self.set_rooms_walkable()

        for (i, j) in self.dungeon.edges:
            p1 = self.dungeon.points[i]
            p2 = self.dungeon.points[j]

            start = self.pixel_to_grid(p1)
            goal = self.pixel_to_grid(p2)

            path_cells = self.A_Star(start, goal)
            if path_cells:
                path = Path(start, goal)
                path.grid_cells = path_cells
                path.generate_cells(self.dungeon.tile_size, self.dungeon.left_buffer, self.dungeon.buffer)
                if (i, j) in self.dungeon.mst:
                    self.paths.append(path)
                else:
                    self.extra_paths.append(path)

                for row, col in path_cells:
                    self.grid_table[row, col] = 1

    def draw_all_paths(self, screen): # pragma: no cover
        """
        Piirretään kaikki polut, myös ne, jotka menevät huoneiden päälle.
        """

        for path in self.paths:
            for cell in path.cells:
                pygame.draw.rect(screen, (120, 100, 100), cell)

        for path in self.extra_paths[:self.extra_path_count]:
            for cell in path.cells:
                pygame.draw.rect(screen, (120, 100, 100), cell)
    
    def draw_clean_paths(self, screen): # pragma: no cover
        """
        Piirretään vain ne polut, jotka eivät osu huoneiden kanssa päällekkäin.
        """

        for path in self.paths:
            for cell in path.cells:
                if not any(cell.colliderect(existing) for existing in self.dungeon.rooms):
                    screen.fill((120, 100, 100), cell)

        for path in self.extra_paths[:self.extra_path_count]:
            for cell in path.cells:
                if not any(cell.colliderect(existing) for existing in self.dungeon.rooms):
                    pygame.draw.rect(screen, (120, 100, 100), cell)
