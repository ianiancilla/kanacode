import pygame

from vocabulary.vocab import Vocab
from helper.graph_elements import draw_frame
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
        pygame.display.flip()
        self.app.vocab = Vocab(self)

        # TODO test, remove
        for word in self.app.vocab.hiragana:
            print(word)

    def update_screen(self, events = None):
        # create loading message
        loading_title = text.load_title
        self.txt_title_image, self.txt_rect = self.app.settings.load_font_title.render(
                                            loading_title,
                                            self.app.settings.load_color,
                                            size = 40)

        # name and place rect for the loading text
        self.txt_rect = self.txt_title_image.get_rect()
        self.txt_rect.center = self.app.screen.get_rect().center

    def draw_screen(self):
        self.app.screen.fill(self.app.settings.col_dark)
        # draw frame for text
        draw_frame(self.app.screen, self.frame, self.app.settings.col_dacc, self.app.settings.col_brand, 15)

        # draw text
        self.app.screen.blit(self.txt_title_image, self.txt_rect)

    # EVENT HANDLING
    def check_events(self):
        """Checks for and responds to mouse and kb events"""
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.quit_game()
        return events