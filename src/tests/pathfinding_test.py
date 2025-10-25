import unittest
import pygame
import numpy as np
from dungeon import Dungeon
from pathfinding import Path, Pathfinding

class TestPath(unittest.TestCase):
    def setUp(self):
        """
        Luodaan yksinkertainen testi-path
        """
        self.path = Path((0, 0), (1, 1))
        self.path.grid_cells = [(0, 0), (0, 1), (1, 1)]


    def test_generate_cells(self):
        """
        Testataan, että path luo oikean määrän soluja ja että
        jokainen solu on oikean kokoinen pygame.rect-olio oikeassa sijainnissa
        """
        tile_size = 20
        left_buffer = 270
        buffer = 50

        self.path.generate_cells(tile_size, left_buffer, buffer)
        self.assertEqual(len(self.path.cells), 3)
        
        for (row, col), rect in zip(self.path.grid_cells, self.path.cells):
            self.assertIsInstance(rect, pygame.Rect)
            self.assertEqual((rect.width, rect.height), (tile_size, tile_size))
            expected_x = left_buffer + col * tile_size
            expected_y = buffer + row * tile_size
            self.assertEqual((rect.x, rect.y), (expected_x, expected_y))

class TestPathfinding(unittest.TestCase):
    def setUp(self):
        """
        Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena. 
        """

        self.left_buffer = 270
        self.buffer = 50
        self.tile_size = 20
        self.grid_width = self.tile_size * 64
        self.grid_height = self.tile_size * 40
        
        self.room_count = 16
        
        self.room_min_len = 4 
        self.room_max_len = 14

        self.dungeon = Dungeon(
            self.left_buffer,
            self.buffer,
            self.grid_width,
            self.grid_height,
            self.tile_size,
            self.room_count,
            self.room_min_len,
            self.room_max_len
        )

        self.pathfinding = Pathfinding(self.dungeon)

    def test_pixel_to_grid(self):
        """
        Testataan, että pikselikoordinaatit muutetaan onnistuneesti grid_table solukoordinaateiksi.
        """
        px, py = 500, 300
        row = (py - self.dungeon.buffer) // self.dungeon.tile_size
        col = (px - self.dungeon.left_buffer) // self.dungeon.tile_size
        expected = (row, col)

        result = self.pathfinding.pixel_to_grid((px, py))
        self.assertEqual(result, expected)

    def test_set_rooms_walkable(self):
        """
        Testataan, että huoneiden solujen arvo muutetaan 1:ksi.
        """
        self.pathfinding.grid_table.fill(0)
        self.pathfinding.set_rooms_walkable()
        self.assertTrue(np.any(self.pathfinding.grid_table == 1))

    def test_get_neighbors(self):
        """
        Testataan, että naapureiden solukoordinaatit saadaan oikein
        sekä keskellä että reunasijainneissa.
        """
        neighbors_center = self.pathfinding.get_neighbors((5, 5))
        expected_center = [(5, 6), (6, 5), (5, 4), (4, 5)]
        self.assertCountEqual(neighbors_center, expected_center)

        neighbors_edge = self.pathfinding.get_neighbors((0, 0))
        expected_edge = [(0, 1), (1, 0)]
        self.assertCountEqual(neighbors_edge, expected_edge)

    def test_heuristic(self):
        """
        Testataan, että Manhattan-etäisyys lasketaan oikein.
        """
        a, b = (2, 3), (5, 7)
        self.assertEqual(self.pathfinding.heuristic(a, b), 7)

    def test_reconstruct_path(self):
        """
        Testataan, että polku on luotu oikein ja sisältää alku- ja loppupisteen.
        """
        came_from = {
            (2, 2): (1, 2),
            (1, 2): (1, 1),
            (1, 1): (0, 1),
            (0, 1): (0, 0)
        }

        current = (2, 2)
        expected_path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]

        result = self.pathfinding.reconstruct_path(came_from, current)

        self.assertEqual(result, expected_path)
        self.assertEqual(result[0], (0, 0))
        self.assertEqual(result[-1], (2, 2))

    def test_A_Star(self):
        """
        Testataan, että A*-algoritmi löytää polun alku- ja loppupisteen välille.
        """
        start = (0, 0)
        goal = (3, 3)
        path = self.pathfinding.A_Star(start, goal)

        self.assertIn(start, path)
        self.assertIn(goal, path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_find_all_paths(self):
        """
        Testataan, että polkuja on löydetty ja niillä kaikilla on jokin pituus.
        """
        self.pathfinding.find_all_paths()
        self.assertGreater(len(self.pathfinding.paths), 0)
        for path in self.pathfinding.paths:
            self.assertTrue(len(path.grid_cells) > 0)
