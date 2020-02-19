""" a template file for kanacode state classes """

import pygame

# other imports here

class StateName(object):
    """ a class for the StateName state """
    def __init__(self, app):
        """ initialises StateName """
        self.app = app
        pass

    def update_screen(self, events):
        """ implements changed that are needed by StateName at every tick """
        pass

    def draw_screen(self):
        """ draws each element of StateName """
        pass

    # EVENT HANDLING
    def check_events(self):
        """Checks for and responds to user events"""
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.quit_game()
        return events