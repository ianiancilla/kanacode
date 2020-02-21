import pygame
import pygame.freetype

from .pygame_helpers import create_centered_text, draw_frame

class Button():    # TODO test border function
    """ a class for pygame clickable buttons """
    def __init__(self, rect,
                 text="Button",
                 function=None,
                 color_base=pygame.Color("red"),
                 color_alt=pygame.Color("red"),
                 font=None,
                 font_color=pygame.Color("black"),
                 font_color_alt=pygame.Color("black")):
        """
        :param rect: a pygame rect object, or two tuples ((x, y), (width, height))
        :param text: a string, text to display on button
        :param function: a function, to be executed when button is clicked
        :param color_base: a pygame color
        :param color_alt: a pygame color (color to change button to when clicked or hovered)
        :param font: a pygame.freetype2 font
        :param font_color: a pygame color
        """
        if isinstance(rect, pygame.Rect):
            self.rect = rect
        else:
            self.rect = pygame.Rect(rect)

        self.text = text
        self.function = function
        self.color_base = color_base
        self.color_alt = color_alt
        if font:
            self.font = font
        else:
            self.font = pygame.freetype.SysFont(None, 36)
        self.font_color = font_color
        self.font_color_alt = font_color_alt

    def draw(self, surface, border=None, alt=False):
        """ draws button on surface
            :param surface: a pygame surface object to draw button on (pygame window for example)
            :param border: None for a button with no border, or a tuple (int, pygame colore object)
                - the int is the pixel thickness of the border
                - the color is the border color
            :param alt: False if button should be in its primary color, True if it should be in its alt color
        """
        # defines colors based on state of "alt" param
        if alt:
            col_button = self.color_alt
            col_font = self.font_color_alt
        else:
            col_button = self.color_base
            col_font = self.font_color

        # defines layout depending on atate of border param
        if border:
            button_rect = draw_frame(surface,
                                     self.rect,
                                     col_button,
                                     border[1],
                                     border[0])
        else:
            button_rect = pygame.draw.rect(surface,
                                           col_button,
                                           self.rect)

        if self.text:
            txt_img, txt_rect = create_centered_text(self.text, self.font, col_font, button_rect)
            surface.blit(txt_img, txt_rect)


    def is_inside(self, pos):
        """ checks the value of "pos" and returns true if it is inside button, false otherwise
            :param pos: a tuple (x, y) of numbers representing screen coordinates """
        if self.rect.left < pos[0] < self.rect.right:
            if self.rect.top < pos[1] < self.rect.bottom:
                return True
        return False

    def on_mouse(self):
        """ a function which checks if mouse position is on the button.
        if it is, self.function will be executed """
        pos_mouse = pygame.mouse.get_pos()
        if self.is_inside(pos_mouse):
            self.function()