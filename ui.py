# ui.py

import pygame

class UI:
    def __init__(self, screen, sidebar_width, sidebar_height):
        """
        Initialise the UI elements. 

        Parameters:
        screen (pygame.Surface): the game screen
        sidebar_width (int): the width of the screen
        sidebar_height (int): the height of the screen
        """

        self.screen = screen
        self.sidebar_width = sidebar_width  # 20% of total width
        self.sidebar_height = sidebar_height  # Same as screen height


    def draw_sidebar(self):
        """
        Sidebar drawn on the side of the screen
        """
        pygame.draw.rect(self.screen, (128, 128, 128), (0, 0, self.sidebar_width, self.sidebar_height))
        
    def draw_buttons(self):
        """
        Drawn buttons onto the sidebar
        """
    def draw_sliders(self):
        """
        We got sliders on the siders.
        """

    def handle_events(self, event):
    
        pass