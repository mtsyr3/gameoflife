# simulation.py

# importing Cell and Existence classes
import random
from cell import Cell
from existence import Existence, Life, Death

class Simulation:
    """
    Manages the simulation grid and updates.
    """
    def __init__(self, grid_size, strategy):
        """
        Iniitalise the simulation with grid size and strategy.
        
        Parameters:
        grid_size (tuple): the size of the grid as (width, height)
        strategy (Existence): the rule strategy to be applied
        """
        self.grid_size = grid_size
        self.strategy = strategy
        self.grid = self.initialise_grid()


    def initialise_grid(self):
        """
        Initialise grid with Cell objects.

        Returns:
        list: a 2D list representing the grid of cells
        """
        width, height = self.grid_size
        return [[Cell(state=random.choice([0, 1]), position=(x, y)) for x in range(width)] for y in range(height)]

    def update_grid(self):
        """
        Update the grid's state by applying the strategy's rules.
        """
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                neighbours = self.get_neighbours(x, y)
                self.strategy.apply_rules(cell, neighbours)

    def get_neighbours(self, x, y):
        """
        Retrieve the neighboring cells for a given cell position.
        
        Parameters:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        
        Returns:
        list: A list of neighboring Cell objects.
        """
        neighbours = [
            self.grid[ny][nx]
            for dx in [-1, 0, 1] for dy in [-1, 0, 1]
            if dx != 0 or dy != 0
            if 0 <= (nx := x + dx) < self.grid_size[0] and 0 <= (ny := y + dy) < self.grid_size[1]
        ]
        return neighbours


# For testing individual files using __main__.py

if __name__ == "__main__":

    sim = Simulation(grid_size=(5, 5), strategy=Life())
    print("Initial grid state:")
    print([[cell.state for cell in row] for row in sim.grid])


    sim.update_grid()
    print("Grid state after update:")
    print([[cell.state for cell in row] for row in sim.grid])

