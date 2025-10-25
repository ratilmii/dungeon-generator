import unittest
import numpy as np
from dungeon import Dungeon
from delaunay import circumcircle_contains, triangulate, get_edges

class TestDelaunay(unittest.TestCase):
    def setUp(self):
        """
        Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena.
        Tallennetaan huoneiden keskipisteet, triangulaatio ja kolmioiden sivut muuttujiin.
        """
        
        tile_size = 20
        grid_width, grid_height = tile_size * 64, tile_size * 40

        left_buffer = 270
        buffer = 50

        room_count = 16
        room_min_len = 4
        room_max_len = 14
        
        dungeon = Dungeon(
            left_buffer,
            buffer,
            grid_width,
            grid_height,
            tile_size,
            room_count,
            room_min_len,
            room_max_len
        )

        self.points = dungeon.points
        self.triangles = triangulate(self.points)
        self.edges = get_edges(self.triangles)
    
    def test_circumcircle_contains(self):
        p1, p2, p3 = (0, 0), (1, 0), (0, 1)
        p = (0.5, 0.5)
        self.assertTrue(circumcircle_contains(p1, p2, p3, p), f"Piste ei ollut ympärysympyrän sisällä")

    def test_points_on_same_line(self):
        p1, p2, p3 = (0, 0), (1, 0), (2, 0)
        p = (0.5, 0)
        self.assertFalse(circumcircle_contains(p1, p2, p3, p), f"Pisteet eivät olleet samalla viivalla")

    def test_triangulate_at_least_one_triangle(self):
        points = []
        self.assertEqual(triangulate(points), set(), f"Triangulaatiossa ei ollut yhtään kolmiota")


    def test_triangulate(self):
        """
        Tarkistetaan, että
        1. jokainen piste kuuluu ainakin yhteen triangulaatiosta saatuun kolmioon
        2. yksikään piste ei ole sellaisen kolmion, johon se ei kuulu, ympärysympyrän sisällä        
        3. kaikki kolmioiden indeksit ovat valideja
        """      

        for i in range(len(self.points)):
            in_triangle = any(i in triangle for triangle in self.triangles)
            self.assertTrue(in_triangle, f"Piste {i} ei esiinny yhdessäkään kolmiossa")

            for triangle in self.triangles:
                if i not in triangle:
                    if circumcircle_contains(
                        self.points[triangle[0]],
                        self.points[triangle[1]],
                        self.points[triangle[2]],
                        self.points[i]
                    ):
                        self.fail(f"Piste {i} on kolmion {triangle} ympärysympyrän sisällä")

        for triangle in self.triangles:
            for idx in triangle:
                self.assertTrue(0 <= idx < len(self.points), f"Kolmion indeksi {idx} pistelistan ulkopuolella")

    def test_get_edges(self):
        """
        Testataan, että kaikki sivut, jotka saadaan triangulaatiosta, ovat jossakin kolmiossa.
        """
        
        for edge in self.edges:
            i, j = edge
            found = False
            for triangle in self.triangles:
                if i in triangle and j in triangle:
                    found = True
                    break
            self.assertTrue(found, f"Sivu {edge} ei esiinny yhdessäkään kolmiossa")

        
