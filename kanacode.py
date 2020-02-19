import pygame
import pygame.freetype

from settings import Settings
from states.games.game_H2R import H2R
from states.loadscreen import LoadScreen


class Kanacode(object):
    def __init__(self):
        """ initialises app """
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.vocab = None
        self.running = True
        self.state = None

        # create window
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        # set initial state
        self.set_state(LoadScreen(self))    # loading screen
        self.set_state(H2R(self))    # TODO once start menu is done, this should point there

    # APP LOOP
    def run_app(self):
        """
        Runs the main loop for the app
        """
        while self.running:
            # checks user input and handles it depending on state
            events = self.state.check_events()
            # updates screen depending on app state
            self.state.update_screen(events)
            # draws new screen depending on current state
            self.state.draw_screen()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def quit_game(self):
        """ quits the game by ending the game loop """
        self.running = False

    # Getters and setters
    def set_state(self, new_state):
        """ sets a new app state for kanacode class.
        new_state needs to be an instance of one of the state classes from the states folder (and subfolders) """
        self.state = new_state

    def get_state(self):
        return self.state

    def get_settings(self):
        return self.settings

    def get_clock(self):
        return self.clock

    def set_vocab(self, vocab):
        """ sets a new vocabulary for the app.
        vocab needs to be an instance of the Vocab class defined in vocabulary/vocab.py """
        self.vocab = vocab

    def get_vocab(self):
        return self.vocab

    def set_running(self, bool):
        """ changes state of game. if running is set to False game will quit.
        bool needs to be a boolean """
        self.running = bool

    def get_running(self):
        return self.running


if __name__ == '__main__':
    kanacode = Kanacode()
    kanacode.run_app()
