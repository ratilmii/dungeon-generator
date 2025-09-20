import pygame
import numpy as np
from delaunay import triangulate

class Dungeon:
    """
    Luodaan Dungeon-olio joka generoi annetun määrän satunnaisen kokoisia (annetuissa rajoissa) huoneita.

    Huoneiden keskipisteet tallennetaan points-listaan ja niille tehdään Delaunay-triangulaatio.

    Triangulaatiosta saatu edges-setti sisältää huoneiden keskipisteiden väliset yhteydet.
    """

    def __init__(self, left_buffer, buffer, width, height, tile_size, room_count, room_min_len, room_max_len):
        self.left_buffer = left_buffer
        self.buffer = buffer
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.room_count = room_count
        
        self.room_min_len = room_min_len 
        self.room_max_len = room_max_len

        self.rooms = []
        self.points = []
        self.edges = set()

        self.generate_rooms()   

    def generate_rooms(self):
        self.rooms = []
        self.points = []
        self.edges = set()
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

        self.edges = triangulate(self.points)

    def draw_rooms(self, screen):
        for room in self.rooms:
            pygame.draw.rect(screen, (200, 100, 100), room)

    def draw_grid(self, screen):
        color_grid_line = (180,180,180)
        color_outline = (0,0,0)

        for x in range(65):
            position_x = self.left_buffer + x * self.tile_size
            pygame.draw.line(screen, color_grid_line, (position_x, self.buffer), (position_x, self.buffer + self.height), 1)
        for y in range(41):
            position_y = self.buffer + y * self.tile_size
            pygame.draw.line(screen, color_grid_line, (self.left_buffer, position_y), (self.left_buffer + self.width, position_y), 1)
            
        pygame.draw.rect(screen, color_outline, (self.left_buffer, self.buffer, self.width, self.height), 2)