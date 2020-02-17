import pygame
import pygame.freetype

from settings import Settings
from states.games.game_h_to_r import H2R
from states.load_screen import Load_screen


class Kanacode():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.vocab = None
        self.running = True
        self.state = None
        self.clock = pygame.time.Clock()

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
        self.set_state(Load_screen(self))
        self.set_state(H2R(self))


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

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state


if __name__ == '__main__':
    kanacode = Kanacode()
    kanacode.run_app()
