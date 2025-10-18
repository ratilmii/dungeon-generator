import pygame
import numpy as np
from dungeon import Dungeon
from pathfinding import Pathfinding

# Parametrit ikkunalle ja piirtoalueen ruudukolle
WIDTH, HEIGHT = 1600, 900
tile_size = 20
tiles_horizontal = 64
tiles_vertical = 40

grid_width, grid_height = tile_size * tiles_horizontal, tile_size * tiles_vertical

left_buffer = 270
buffer = 50

room_count = 16
room_min_len = 4
room_max_len = 14

color_bg = (200,200,200) 
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
blue = (0, 0, 255)

if __name__ == "__main__":
    pygame.init()
   
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon Generator")

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

    pathfinding = Pathfinding(dungeon)

    generate_button_rect = pygame.Rect(50, 50, 170, 40)
    font = pygame.font.Font(None, 32)
    button_text = font.render("Regenerate", True, white)    

    while True:        
        screen.fill(color_bg)
        dungeon.draw_grid(screen)
        dungeon.draw_rooms(screen)
        points = dungeon.points
        edges = dungeon.edges
        mst = dungeon.mst

        for i, j in edges:
            pygame.draw.line(screen, green, points[i], points[j], 2)
        
        for i, j in mst:
            pygame.draw.line(screen, blue, points[i], points[j], 4)

        for point in points:
            pygame.draw.circle(screen, black, point, 3)        
        
        pygame.draw.rect(screen, (100, 100, 100), generate_button_rect)        
        screen.blit(button_text, (70, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                if generate_button_rect.collidepoint(event.pos):
                    dungeon.generate_rooms()

        pygame.display.flip()