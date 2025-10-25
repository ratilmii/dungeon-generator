import unittest
from dungeon import Dungeon
from prim import minimum_spanning_tree, weight

class TestPrim(unittest.TestCase):
    def setUp(self):
        """
        Luodaan testi-dungeon samoilla parametreilla, joita ohjelma käyttää oletuksena.
        Tallennetaan huoneiden keskipisteet ja pisteiden väliset sivut muuttujiin.
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
        self.edges = dungeon.edges

    def test_minimum_spanning_tree(self):
        """
        Generoidaan minimum spanning tree ja testataan, että        
        1. Kaikki points-listan pisteet sisältyvät MST:hen
        2. MST:ssä on oikea määrä sivuja
        3. Kaikki MST:n sivut kuuluvat triangulaatioon
        """
        
        mst = minimum_spanning_tree(self.points, self.edges)

        indices = set()
        
        for edge in mst:
            indices.add(edge[0])
            indices.add(edge[1])
                
        self.assertEqual(len(indices), len(self.points), f"Kaikki pisteet eivät sisälly MST:hen")

        self.assertEqual(len(mst), len(self.points) - 1, f"MST:ssä tulisi olla {len(self.points) - 1} sivua, nyt oli {len(mst)}")

        for edge in mst:
            self.assertIn(edge, self.edges, f"MST:n sivu {edge} ei kuulu triangulaation sivuihin")

    def test_weight(self):
        """
        Testataan yksinkertaisesti euklidisen etäisyyden laskeminen oikein.
        """

        self.assertAlmostEqual(weight((0, 0), (3, 0)), 3)

        self.assertAlmostEqual(weight((0, 0), (0, 4)), 4)

        self.assertAlmostEqual(weight((0, 0), (3, 4)), 5)

        self.assertAlmostEqual(weight((3, 4), (0, 0)), 5)
