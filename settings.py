import pygame
import pygame.freetype


class Settings():
    """class to manage app settings"""

    def __init__(self):
        """initialise app settings"""
        self.game_title = "Kanacode"

        # DISPLAY settings
        self.full_screen = False
        self.screen_width = 1024
        self.screen_height = 768
        # color settings
        self.col_light = pygame.Color("#dcefe3")
        self.col_lacc = pygame.Color("#f5882e")
        self.col_brand = pygame.Color("#d06351")
        self.col_dacc = pygame.Color("#7b929c")
        self.col_dark = pygame.Color("#2b3746")
        # Loading screen display settings
        self.load_font_title = pygame.freetype.SysFont(None, 50)
        self.load_color = self.col_dark
        # Hiragana to Romaji screen display settings
        self.h2r_font_english = pygame.freetype.SysFont("", 36)
        self.h2r_font_english_color = self.col_dark
        self.h2r_font_kana = pygame.freetype.Font("font/KosugiMaru-Regular.ttf", 100)
        self.h2r_font_kana_color = self.col_dark
        self.h2r_font_romaji = pygame.freetype.SysFont("Mono", 50)    # TODO change font
        self.h2r_font_romaji_color = self.col_dark
        self.h2r_feedback_color_right = pygame.Color("green")
        self.h2r_feedback_color_wrong = pygame.Color("red")
        self.text_input_height = self.h2r_font_romaji.size + 10
        self.text_input_width = 600

        # KEY MAP settings
        self.key_quit = pygame.K_ESCAPE
