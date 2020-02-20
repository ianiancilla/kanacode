import random
import pygame

from helper.textinput import TextInput
from helper.pygame_helpers import create_centered_text, create_containers
from helper.button import Button
import text


class H2R(object):
    """ A mode in which a hiragana word is displayed,
    and the user needs to enter the correct romaji transliteration"""

    def __init__(self, app):
        """ initialises the Hiragana to Romaji exercise
        - creates container rects for the 3 main screen areas
        - selects a word
        - updates and draws screen accordingly """
        self.app = app

        # create and place container rects for different UI elements
        self.container_english, \
        self.container_kana, \
        self.container_romaji, \
        self.container_buttons = create_containers(
            self.app.screen,
            (5 / 20, 6 / 20, 5 / 20, 4 / 20),
            layout="V")

        # creates text input field
        self.text_input = TextInput(
            initial_string="",
            font_family=self.app.settings.h2r_font_romaji.name,
            font_size=int(self.app.settings.h2r_font_romaji.size),
            antialias=True,
            text_color=self.app.settings.h2r_font_romaji_color,
            cursor_color=self.app.settings.h2r_font_romaji_color,
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=self.app.settings.h2r_text_input_max_string_length
        )

        # creates background frame for input field
        self.input_frame = pygame.Rect(0, 0,
                                       self.app.settings.h2r_text_input_width + 20,
                                       self.app.settings.h2r_text_input_height)
        self.input_frame.center = self.container_romaji.center

        # creates rect for input box
        self.text_input_rect = pygame.Rect(0, 0,
                                           self.app.settings.h2r_text_input_width,
                                           self.app.settings.h2r_text_input_height)
        self.text_input_rect.center = self.input_frame.center

        # init attributes for text rects and images
        self.str_english_img, self.str_english_rect = None, None
        self.str_kana_img, self.str_kana_rect = None, None

        # create and place input tip
        self.input_tip_img, self.input_tip_rect = create_centered_text(
            text.h2r_input_tip,
            self.app.settings.h2r_font_tip,
            self.app.settings.h2r_font_tip_color,
            self.container_romaji)

        # creates buttons
        self.butt_help = self._h2r_button(text.h2r_button_help)
        self.butt_check = self._h2r_button(text.h2r_button_check)
        self.butt_quit = self._h2r_button(text.h2r_button_quit)

        self.buttons = [self.butt_help, self.butt_check, self.butt_quit]

        self._place_buttons(self.buttons, self.container_buttons)

        # set initial status
        self.word = self._pick_word()
        self.previous_try = None  # determines background of text input field as feedback

    def update_screen(self, events):
        """ implements changes that are needed by H2R at every tick, based on user events """
        # creates english word img
        self.str_english_img, self.str_english_rect = create_centered_text(
            self.word.english,
            self.app.settings.h2r_font_english,
            self.app.settings.h2r_font_english_color,
            self.container_english)
        # creates kana word img
        self.str_kana_img, self.str_kana_rect = create_centered_text(
            self.word.hiragana,
            self.app.settings.h2r_font_kana,
            self.app.settings.h2r_font_kana_color,
            self.container_kana)

        # updates text input box
        if self.text_input.update(events):
            self._check_word()

    def draw_screen(self):
        """ draws each element of H2R """
        # draw backgrounds of containers
        self.app.screen.fill(self.app.settings.col_dark)
        pygame.draw.rect(self.app.screen,
                         self.app.settings.h2r_col_bg_en,
                         self.container_english)
        pygame.draw.rect(self.app.screen,
                         self.app.settings.h2r_col_bg_kan,
                         self.container_kana)
        pygame.draw.rect(self.app.screen,
                         self.app.settings.h2r_col_bg_rom,
                         self.container_romaji)
        pygame.draw.rect(self.app.screen,
                         self.app.settings.h2r_col_bg_but,
                         self.container_buttons)

        # draw bg of text input box
        if self.previous_try:
            if self.previous_try == "right":
                romaji_frame_color = self.app.settings.col_success
            else:
                romaji_frame_color = self.app.settings.col_danger
        else:
            romaji_frame_color = self.app.settings.h2r_col_bg_input
        pygame.draw.rect(self.app.screen,
                         romaji_frame_color,
                         self.input_frame)

        # draw all texts
        self.app.screen.blit(self.str_english_img, self.str_english_rect)
        self.app.screen.blit(self.str_kana_img, self.str_kana_rect)

        if not self.text_input.get_text():    # only if there is no text in input field
            self.app.screen.blit(self.input_tip_img, self.input_tip_rect)

        # draw text input box
        self.app.screen.blit(self.text_input.get_surface(), self.text_input_rect)

        # draw all buttons
        for button in self.buttons:
            button.draw(self.app.screen)

    # EVENT HANDLING
    def check_events(self):
        """Checks for and responds to mouse and kb events
        NOTE: kb events related to input box and RETURN kez are handled in update function"""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                             and event.key == self.app.settings.key_quit):
                self.app.quit_game()
                return []  # this is so the text input does not activate while app is quitting
        return events

    def _pick_word(self):
        """ picks a random Word instance from the app's vocab"""
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

    # HELPERS
    def _place_buttons(self, button_list, container_rect, layout="H"):
        """
        places buttons equidistant and centered on given container_rect, following given layout.
        :param button_list: a list of Button objects
        :param container_rect: a rect, delimiting the area of the screen buttons should occupy
        :return: None
        """
        # define fraction of surface each container will take
        butt_num = len(button_list)
        containers_sizes = []
        for i in range(butt_num):
            containers_sizes.append(1/butt_num)

        # create ane places containers for buttons according to chosen layout
        if layout == "H":
            butt_containers = create_containers(container_rect, containers_sizes, layout="H")
        elif layout == "V":
            butt_containers = create_containers(container_rect, containers_sizes, layout="V")
        else:
            raise TypeError("Improper argument given for layout parameter")

        # places each button
        for i in range(butt_num):
            button_list[i].rect.center = butt_containers[i].center

    def _h2r_button(self, txt):
        return Button(((0, 0), self.app.settings.h2r_button_size),
                      text=txt,
                      color_base=self.app.settings.h2r_button_color,
                      color_alt=self.app.settings.h2r_button_color_alt,
                      font=self.app.settings.h2r_button_font,
                      font_color=self.app.settings.h2r_button_font_color,
                      font_color_alt=self.app.settings.h2r_button_font_color_alt
                      )
