# game_logic.py

import pygame
from cell import Cell
from existence import Life, Death
from simulation import Simulation

def run_game():
    # Initialize the simulation with a grid size and strategy
    sim = Simulation(grid_size=(20, 20), strategy=Life())

    # Pygame Initialization
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Game of Life')
    
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
                
        pygame.display.update()
        clock.tick(5)

    pygame.quit()

# Main entry point for running the game logic
if __name__ == "__main__":
    run_game()

