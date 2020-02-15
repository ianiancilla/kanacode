import random

import pygame

from helper.pygame_helpers import create_centered_text
from helper.textinput import TextInput
import text

class H2R():
    """ A mode in which a hiragana word is displayed,
    and the user needs to enter the correct romaji transliteration"""
    def __init__(self, app):
        """ initialises the Hiragana to Romaji exercise
        - creates container rects for the 3 main screen areas
        - selects a word
        - updates and draws screen accordingly """
        self.app = app
        # create and place container rects for different UI elements
        self._create_container_rects()

        self.text_input = TextInput(
                                    initial_string = "",
                                    font_family=self.app.settings.h2r_font_romaji.name,
                                    font_size=int(self.app.settings.h2r_font_romaji.size),
                                    antialias=True,
                                    text_color=self.app.settings.h2r_font_romaji_color,
                                    cursor_color=self.app.settings.h2r_font_romaji_color,
                                    repeat_keys_initial_ms=400,
                                    repeat_keys_interval_ms=35,
                                    max_string_length=15
        )

        self.word = self._pick_word()
        self.previous_try = None

    def update_screen(self, events):
        # creates english
        self.str_english_img, self.str_english_rect = create_centered_text(
                        self.word.english,
                        self.app.settings.h2r_font_english,
                        self.app.settings.h2r_font_english_color,
                        self.container_english)
        # creates kana
        self.str_kana_img, self.str_kana_rect = create_centered_text(
                        self.word.kana,
                        self.app.settings.h2r_font_kana,
                        self.app.settings.h2r_font_kana_color,
                        self.container_kana)

        # creates rect for input box
        self.text_input_rect = pygame.Rect(0, 0,
                                           self.app.settings.text_input_width,
                                           self.app.settings.text_input_height)
        self.text_input_rect.center = self.romaji_frame.center

        # updates text input box
        if self.text_input.update(events):
            self._check_word()

    def draw_screen(self):
        # draw backgrounds of containers
        pygame.draw.rect(self.app.screen,
                    self.app.settings.col_lacc,
                    self.container_english)
        pygame.draw.rect(self.app.screen,
                    self.app.settings.col_lacc,
                    self.container_kana)
        pygame.draw.rect(self.app.screen,
                    self.app.settings.col_dark,
                    self.container_romaji)
        pygame.draw.rect(self.app.screen,
                    self.app.settings.col_dark,
                    self.container_buttons)

        # draw bg of text input box
        if self.previous_try:
            if self.previous_try == "right":
                romaji_frame_color = self.app.settings.h2r_feedback_color_right
            else:
                romaji_frame_color = self.app.settings.h2r_feedback_color_wrong
        else:
            romaji_frame_color = self.app.settings.col_light
        pygame.draw.rect(self.app.screen,
                    romaji_frame_color,
                    self.romaji_frame)

        # draw all texts
        self.app.screen.blit(self.str_english_img, self.str_english_rect)
        self.app.screen.blit(self.str_kana_img, self.str_kana_rect)

        # draw text input box
        self.app.screen.blit(self.text_input.get_surface(), self.text_input_rect)

    # EVENT HANDLING

    def check_events(self):
        """Checks for and responds to mouse and kb events
        NOTE: kb events related to input box and RETURN kez are handled in update function"""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                and event.key == self.app.settings.key_quit):
                self.app.quit_game()
        return events

    def _create_container_rects(self):
        """ create and place container rects for different UI elements
        - self.container_english
        - self.container_kana
        - self.container_romaji
        - self.container_buttoms
        - self.romaji_frame
        """
        self.container_english = pygame.Rect(
            0, 0,
            int(self.app.screen.get_rect().width),
            int(self.app.screen.get_rect().height * (2 / 10))
        )
        self.container_kana = pygame.Rect(
            0, 0,
            int(self.app.screen.get_rect().width),
            int(self.app.screen.get_rect().height * (3 / 10))
        )
        self.container_kana.top = self.container_english.bottom
        self.container_romaji = pygame.Rect(
            0, 0,
            int(self.app.screen.get_rect().width),
            int(self.app.screen.get_rect().height * (3 / 10))
        )
        self.container_romaji.top = self.container_kana.bottom
        self.container_buttons = pygame.Rect(
            0, 0,
            int(self.app.screen.get_rect().width),
            int(self.app.screen.get_rect().height * (2 / 10))
        )
        self.container_buttons.top = self.container_romaji.bottom

        self.romaji_frame = pygame.Rect(0, 0,
                                        self.app.settings.text_input_width + 20,
                                        self.app.settings.text_input_height)
        self.romaji_frame.center = self.container_romaji.center

    def _pick_word(self):
        """ picks a random Word istance from the app's vocab"""
        return random.choice(list(self.app.vocab.hiragana))

    def _check_word(self):
        """ checks whether input text is correct for current word """
        current_input = self.text_input.get_text().lower().strip()
        print(current_input)
        print(self.word.romaji)
        if current_input == self.word.romaji:
            if self.previous_try == "right":
                self.previous_try = None
                self._next_word()

            else:
                self.previous_try = "right"
        else:
            self.previous_try = "wrong"

    def _next_word(self):
        self.word = self._pick_word()
        self.text_input.clear_text()