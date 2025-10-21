import pygame
import pygame_gui
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
    clock = pygame.time.Clock()
   
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), "gui/theme.json")
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

    generate_button = pygame_gui.elements.UIButton(
        relative_rect = pygame.Rect((30, 790), (210, 60)),
        text = "Generoi",
        manager = manager,
        tool_tip_text = "Generoi luolaston uudelleen annetuilla parametreilla.",
        object_id="#generate_button"
    )

    triangulation_checkbox = pygame_gui.elements.UICheckBox(
        relative_rect = pygame.Rect((10, 50), (22, 22)),
        text = "Näytä triangulaatio",
        manager = manager,
        tool_tip_text = "Näytä/piilota Delaunay-triangulaatio",
        initial_state = False
    )

    mst_checkbox = pygame_gui.elements.UICheckBox(
        relative_rect = pygame.Rect((10, 92), (22, 22)),
        text = "Näytä minimum spanning tree",
        manager = manager,
        tool_tip_text = "Näytä/piilota MST:n reitti.",
        initial_state = False
    )

    points_checkbox = pygame_gui.elements.UICheckBox(
        relative_rect = pygame.Rect((10, 134),(22,22)),
        text = "Näytä huoneiden keskipisteet",
        manager = manager,
        tool_tip_text = "Näytä/piilota huoneiden keskipisteet.",
        initial_state = False
    )

    path_display_label = pygame_gui.elements.ui_label.UILabel(
        relative_rect = pygame.Rect((12, 176), (190, 20)),
        text = "Näytä käytävät:",
        manager = manager,
    )

    dropdown_options = ["Siisti", "Kaikki"]
    display_paths_dropdown =  pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list = dropdown_options,
        starting_option = "Siisti",
        relative_rect = pygame.Rect((10, 198), (110, 30)),
        manager = manager,
    )

    room_count_label = pygame_gui.elements.ui_label.UILabel(
        relative_rect = pygame.Rect((10, 240), (190, 20)),
        text = "Huoneiden määrä:",
        manager = manager
    )

    room_count_slider = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
        relative_rect = pygame.Rect((10, 270), (175, 25)),
        start_value = 16,
        value_range = (4, 20),
        click_increment = 1,
        manager = manager
    )

    running = True
    show_triangulation = False
    show_mst = False
    show_points = False
    selected_paths_display = "Siisti"
    
    while running:
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:  
                if event.ui_element == generate_button:
                    dungeon.generate_rooms()
                    pathfinding.find_all_paths()

            if event.type == pygame_gui.UI_CHECK_BOX_CHECKED or event.type == pygame_gui.UI_CHECK_BOX_UNCHECKED:
                if event.ui_element == triangulation_checkbox:
                    show_triangulation = triangulation_checkbox.is_checked
                elif event.ui_element == mst_checkbox:
                    show_mst = mst_checkbox.is_checked
                elif event.ui_element == points_checkbox:
                    show_points = points_checkbox.is_checked
            
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == display_paths_dropdown:
                    selected_paths_display = event.text

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == room_count_slider:
                    current_value = int(event.value)
                    
                    if current_value != room_count:
                        room_count = current_value
                        dungeon.room_count = room_count
                        dungeon.generate_rooms()
                        pathfinding.find_all_paths()


        manager.update(dt)

        screen.fill(color_bg)
        dungeon.draw_grid(screen)
        dungeon.draw_rooms(screen)
        if selected_paths_display == "Kaikki":
            pathfinding.draw_all_paths(screen)
        else:
            pathfinding.draw_clean_paths(screen)

        points = dungeon.points
        edges = dungeon.edges
        mst = dungeon.mst

        if show_triangulation:
            for i, j in edges:
                pygame.draw.line(screen, green, points[i], points[j], 2)
        if show_mst:
            for i, j in mst:
                pygame.draw.line(screen, blue, points[i], points[j], 3)
        if show_points:
            for point in points:
                pygame.draw.circle(screen, black, point, 3)       
        
        manager.draw_ui(screen)
        pygame.display.flip()