# game_logic.py

import pygame
from cell import Cell
from existence import Life, Death
from simulation import Simulation
from ui import UI  # Import the UI class

def run_game():
    # Initialize the simulation with a grid size and strategy
    sim = Simulation(grid_size=(200, 200), strategy=Life())

    # Pygame Initialization
    pygame.init()
    screen = pygame.display.set_mode((1024, 1024))
    sidebar_width = screen.get_width() * 0.2  # 20% of total width
    sidebar_height = screen.get_height()  # Same as screen height

    pygame.display.set_caption('Game of Life')
    
    ui = UI(screen, sidebar_width, sidebar_height)  # Initialize UI
    
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Update the grid using the strategy
        sim.update_grid()

        # Draw the grid
        for y, row in enumerate(sim.grid):
            for x, cell in enumerate(row):
                color = (255, 255, 255) if cell.state == 0 else (0, 128, 0)
                pygame.draw.rect(screen, color, (x*20, y*20, 20, 20))

        ui.draw_sidebar()  # Draw the sidebar
                
        pygame.display.update()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    run_game()
