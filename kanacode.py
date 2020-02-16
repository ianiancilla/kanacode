import pygame

from settings import Settings
from load_screen import Load_screen


class Kanacode():
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.running = True

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
        self.state = Load_screen(self)

    # APP LOOP
    def run_app(self):
        """
        Runs the main loop for the app
        """
        while self.running:
            # checks user input and handles it depending on state
            self.state.check_events()
            # updates screen depending on app state
            self.state.update_screen()
            # draws new screen depending on current state
            self.state.draw_screen()
            pygame.display.flip()
        pygame.quit()

    def quit_game(self):
        """ quits the game by ending the game loop """
        self.running = False


if __name__ == '__main__':
    kanacode = Kanacode()
    kanacode.run_app()