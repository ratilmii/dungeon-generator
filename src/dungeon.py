import pygame
import numpy as np
from delaunay import triangulate, get_edges
from prim import minimum_spanning_tree

class Dungeon:
    def __init__(self, left_buffer, buffer, grid_width, grid_height, tile_size, room_count, room_min_len, room_max_len):
        """
        Luodaan Dungeon-olio joka generoi room_count määrän satunnaisen kokoisia (room_min_len - room_max_len) huoneita.
        left_buffer ja buffer rajaavat piirtoalueen ohjelman pääikkunaa pienemmäksi.
        grid_width ja grid_height määrittelevät piirtoalueen leveyden ja korkeuden.
        tile_size määrittelee ruudukon yksittäisen ruudun koon.
        """

        self.left_buffer = left_buffer
        self.buffer = buffer
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tile_size = tile_size
        self.room_count = room_count
        
        self.room_min_len = room_min_len 
        self.room_max_len = room_max_len

        self.rooms = []
        self.points = []
        self.triangulation = []
        self.edges = set()
        self.mst = set()

        self.generate_rooms()   

    def generate_rooms(self):
        """
        Generoidaan huoneet annettujen parametrien perusteella. 
        Huoneet eivät saa olla päällekkäin, tai aivan vierekkäin, ja niiden sijoittamiselle on attempts_left määrä yrityksiä.
        Kun huoneet on generoitu, niille tehdään Delaunay-triangulaatio ja luodaan minimum spanning tree.
        """
        
        self.rooms.clear()
        self.points.clear()

        BUFFER = 1 * self.tile_size

        attempts_left = 1000

        while len(self.rooms) < self.room_count and attempts_left > 0:
            room_width = np.random.randint(self.room_min_len, self.room_max_len) * self.tile_size
            room_height = np.random.randint(self.room_min_len, self.room_max_len) * self.tile_size

            x = self.left_buffer + BUFFER + np.random.randint(0, 63 - (room_width // self.tile_size)) * self.tile_size
            y = self.buffer + BUFFER + np.random.randint(0, 39 - (room_height // self.tile_size)) * self.tile_size

            new_room = pygame.Rect(x, y, room_width, room_height)

            if not any(new_room.inflate(BUFFER, BUFFER).colliderect(existing.inflate(BUFFER, BUFFER)) for existing in self.rooms):
                self.rooms.append(new_room)
                self.points.append(new_room.center)
            
            attempts_left -= 1

        self.triangulation = triangulate(self.points)
        self.edges = get_edges(self.triangulation)
        self.mst = minimum_spanning_tree(self.points, self.edges)

    def draw_rooms(self, screen): # pragma: no cover
        """
        Piirretään huoneet näytölle.
        """

        for room in self.rooms:
            pygame.draw.rect(screen, (200, 100, 100), room)
            pygame.draw.rect(screen, (50, 50, 50), room, 1)

    def draw_grid(self, screen): # pragma: no cover
        """
        Piirretään ruudukon viivat perustuen tile_size-kokoon.
        """

        color_grid_line = (180,180,180)
        color_outline = (0,0,0)

        for x in range(65):
            position_x = self.left_buffer + x * self.tile_size
            pygame.draw.line(screen, color_grid_line, (position_x, self.buffer), (position_x, self.buffer + self.grid_height), 1)
        for y in range(41):
            position_y = self.buffer + y * self.tile_size
            pygame.draw.line(screen, color_grid_line, (self.left_buffer, position_y), (self.left_buffer + self.grid_width, position_y), 1)
            
        pygame.draw.rect(screen, color_outline, (self.left_buffer, self.buffer, self.grid_width, self.grid_height), 2)