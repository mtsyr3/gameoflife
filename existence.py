# existence.py

from abc import ABC, abstractmethod
from cell import Cell

# Existence Interface
class Existence(ABC):
    @abstractmethod
    def apply_rules(self, cell, neighbors):
        pass

# Concrete Strategy: Life
class Life(Existence):
    def apply_rules(self, cell, neighbours):
        """
        Apply Conway's Game of Life rules.
        
        Parameters:
        cell (Cell): The cell for which to apply the rules.
        neighbours (list): A list of neighbouring Cell objects.
        """
        alive_neighbours = sum(neighbour.state for neighbour in neighbours)
        
        # Rule 1: Any live cell with fewer than two live neighbours dies (underpopulation).
        # Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
        # Rule 3: Any live cell with more than three live neighbours dies (overpopulation).
        if cell.state == 1:
            if alive_neighbours < 2 or alive_neighbours > 3:
                cell.state = 0
                
        # Rule 4: Any dead cell with exactly three live neighbours becomes a live cell (reproduction).
        if cell.state == 0 and alive_neighbours == 3:
            cell.state = 1


# Concrete Strategy: Death
class Death(Existence):
    def apply_rules(self, cell, neighbours):
        """
        All cells will die. Useful for testing.
        
        Parameters:
        cell (Cell): The cell for which to apply the rules.
        neighbours (list): A list of neighbouring Cell objects.
        """
        cell.state = 0

# Test to make sure the classes are defined correctly
life = Life()
death = Death()
isinstance(life, Existence), isinstance(death, Existence)

if __name__ == "__main__":

    # Create a few example Cell objects
    cell_alive = Cell(state=1, position=(0, 0))
    cell_dead = Cell(state=0, position=(1, 1))
    neighbours_alive = [Cell(state=1, position=(x, y)) for x in range(2) for y in range(2)]
    neighbours_mixed = [Cell(state=i%2, position=(x, y)) for i, (x, y) in enumerate([(0, 0), (1, 0), (0, 1), (1, 1)])]

    # Instantiate Life and Death strategies
    life = Life()
    death = Death()

    # Test Life strategy
    life.apply_rules(cell_alive, neighbours_alive)
    assert cell_alive.state == 0, "Life strategy failed for an alive cell"

    life.apply_rules(cell_dead, neighbours_alive)
    assert cell_dead.state == 0, "Life strategy failed for a dead cell"

    # Test Death strategy
    death.apply_rules(cell_alive, neighbours_alive)
    assert cell_alive.state == 0, "Death strategy failed for an alive cell"

    death.apply_rules(cell_dead, neighbours_alive)
    assert cell_dead.state == 0, "Death strategy failed for a dead cell"

    print("All tests passed!")