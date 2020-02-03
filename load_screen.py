import pygame

from vocab import Vocab
from round_rects import round_rect
import text

class Load_screen():
    """ a class for the app loading screen """
    def __init__(self, app):
        self.app = app

        # create text frame
        self.frame = pygame.Rect(0, 0,
                                 int(self.app.screen.get_rect().width*(2/3)),
                                 int(self.app.screen.get_rect().height*(1/2)))
        self.frame.center = self.app.screen.get_rect().center

        self.update_screen()
        self.draw_screen()


        self.app.vocab = Vocab(self)

    def update_screen(self):
        # create loading message
        loading_title = text.load_title
        self.txt_title_image = self.app.settings.load_font_title.render(loading_title,
                                                                  True, self.app.settings.load_color)
        # name and place rect for the loading text
        self.txt_rect = self.txt_title_image.get_rect()
        self.txt_rect.center = self.app.screen.get_rect().center

    def draw_screen(self):
        self.app.screen.fill(self.app.settings.col_dark)
        # draw frame for text
        round_rect(self.app.screen, self.frame, self.app.settings.col_brand, border=15,
                                inside=self.app.settings.col_dacc)

        # draw text
        self.app.screen.blit(self.txt_title_image, self.txt_rect)

    # EVENT HANDLING
    def check_events(self):
        """Checks for and responds to mouse and kb events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.quit_game()