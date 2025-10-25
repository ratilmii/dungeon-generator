import unittest
from dungeon import Dungeon

class TestDungeon(unittest.TestCase):
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

    def test_generate_rooms(self):
        """
        Generoidaan huoneet ja testataan, että        
        1. Huoneita generoidaan vähintään yksi, mutta ei enempää kuin room_count
        2. Generoidut huoneet eivät ole päällekkäin tai aivan vierekkäin (BUFFER minimiväli)
        """
        
        self.assertGreater(len(self.dungeon.rooms), 0, "Huoneita ei generoitu ollenkaan")
        self.assertLessEqual(len(self.dungeon.rooms), self.dungeon.room_count, f"Huoneita generoitiin {len(self.dungeon.rooms) - self.dungeon.room_count} liikaa")

        BUFFER = 1 * self.tile_size
        for i, room1 in enumerate(self.dungeon.rooms):
            for j, room2 in enumerate(self.dungeon.rooms):
                if i != j:
                    self.assertFalse(
                        room1.inflate(BUFFER, BUFFER).colliderect(room2.inflate(BUFFER, BUFFER)),
                        f"Huoneet {i} ja {j} osuvat toisiinsa"
                    )