import pygame

from vocabulary.vocab import Vocab
from helper.pygame_helpers import draw_frame
import text


class LoadScreen(object):
    """ a class for the app loading screen """
    def __init__(self, app):
        """ initialises loading screen """
        self.app = app

        # create and position text frame
        self.frame = pygame.Rect(0, 0,
                                 int(self.app.screen.get_rect().width*(2/3)),
                                 int(self.app.screen.get_rect().height*(1/2)))
        self.frame.center = self.app.screen.get_rect().center

        # create loading message
        self.txt_image, self.txt_rect = self.app.settings.load_font.render(
                                                                            text.load_title,
                                                                            self.app.settings.load_font_color,
                                                                            size=40)
        # name and place rect for the loading text
        self.txt_rect = self.txt_image.get_rect()
        self.txt_rect.center = self.app.screen.get_rect().center

        self.draw_screen()
        # flip() needed to display the screen before it does the actual loading, so that it will be on screen
        # during the loading time. That is why we cannot rely on the game loop as usual for flipping
        # (while loop is stuck while loading)
        pygame.display.flip()
        self.app.vocab = Vocab(self)

        # TODO test, remove
        for word in self.app.vocab.hiragana:
            print(word)

    def update_screen(self, events=None):
        """ implements changes that are needed by loading screen at every tick """
        # needed as it is called by loop, but screen is static and needs no changes
        pass

    def draw_screen(self):
        """ draws each element of LoadingScreen """
        # draws background
        self.app.screen.fill(self.app.settings.load_bg)
        # draw frame for text
        draw_frame(self.app.screen, self.frame,
                   self.app.settings.load_bg_frame,
                   self.app.settings.load_bg_frame_border, 30)
        # draw text
        self.app.screen.blit(self.txt_image, self.txt_rect)

    # EVENT HANDLING
    def check_events(self):
        """Checks for and responds to mouse and kb events"""
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.quit_game()
        return events
