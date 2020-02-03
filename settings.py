import pygame


class Settings():
    """class to manage app settings"""

    def __init__(self):
        """initialise app settings"""
        self.game_title = "Kanacode"

        # DISPLAY SETTINGS
        self.full_screen = False
        self.screen_width = 1024
        self.screen_height = 768

        # color settings
        self.col_light = pygame.Color("#dcefe3")
        self.col_lacc = pygame.Color("#f5882e")
        self.col_brand = pygame.Color("#d06351")
        self.col_dacc = pygame.Color("#7b929c")
        self.col_dark = pygame.Color("#2b3746")

        # LOADING SCREEN settings
        self.load_font_title = pygame.font.SysFont(None, 70)
        self.load_color = self.col_dark