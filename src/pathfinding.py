import pygame
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
        self.rects = []

class Pathfinding:
    """
    Luodaan annetulle Dungeon-oliolle Pathfinding-olio,
    joka käyttää A*-algoritmia ja modifioitua Manhattan-heuristiikkaa.
    Tallennetaan kaikki polut listaan.
    """
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.tiles_horizontal = dungeon.grid_width // dungeon.tile_size
        self.tiles_vertical = dungeon.grid_height // dungeon.tile_size
        self.grid_table = np.zeros((self.tiles_vertical, self.tiles_horizontal), dtype=int)

        self.paths = []

        self.find_paths()

    def find_paths(self):
        self.grid_table.fill(0)

        for room in self.dungeon.rooms:
            grid_x1 = (room.left - self.dungeon.left_buffer) // self.dungeon.tile_size
            grid_y1 = (room.top - self.dungeon.buffer) // self.dungeon.tile_size
            grid_x2 = (room.right - self.dungeon.left_buffer) // self.dungeon.tile_size
            grid_y2 = (room.bottom - self.dungeon.buffer) // self.dungeon.tile_size
            self.grid_table[grid_y1:grid_y2, grid_x1:grid_x2] = 1

