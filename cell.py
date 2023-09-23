# cell.py

class Cell:
    """
    Represents a cell in the grid.
    Utilizes Encapsulation design pattern to bundle the cell's state and position.
    """
    def __init__(self, state, position):
        """
        Initialize a cell with a state and position.

        Parameters:
        state (int): The initial state of the cell, 0 for dead and 1 for alive.
        position (tuple): The (x, y) position of the cell in the grid.
        """
        self.state = state
        self.position = position

    def flip_state(self):
        """
        Flip the cell's state from dead to alive or vice versa.
        """
        self.state = 1 - self.state

if __name__ == "__main__":
    example_cell = Cell(state=0, position=(0, 0))
    print(f"Initial state: {example_cell.__dict__}")

    example_cell.flip_state()
    print(f"State after flip: {example_cell.__dict__}")