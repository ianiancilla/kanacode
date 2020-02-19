""" a series of functions to help with common needs in pygame """
import pygame


def create_centered_text(string, font, font_color, container):
    """ creates an image and a rect for easy blitting of text
    - string: the string to write
    - font: the font to use, should be a pygame.freetype font
    - font_color: the color, as a pygame.Color() object
    - container: a pygame.Rect() object, on which the text will be centered"""
    # create text image
    str_img, str_rect = font.render(string, font_color)
    # center text image rect on container
    str_rect.center = container.center
    return str_img, str_rect


def draw_frame(surface, rect, color_fill, color_border, border=1):
    """
    Creates and draws a rect with a frame. Returns the inside rect object.
    returns a pygame.Rect() object, which is the filled area inside the frame
    - surface: the pygame surface to draw this on
    - rect: pygame.Rect() object for the outer frame
    - color_fill, color_border: pygame.Color() object for fill and the border
    - border: border thickness, in pixel (an int)
    """
    surface.fill(color_border, rect)
    inside_rect = rect.inflate(-border*2, -border*2)
    surface.fill(color_fill, inside_rect)
    return inside_rect


def create_containers_hor(surface, containers_tup):
    """ creates and places container rects to help layout.
    - each container is as wide as surface, and as tall as specified in containers_tup
    - containers are placed one under the other, with no space in between
    - containers are created and place following the order in which they appear in the list
    - surface is a pygame surface object (for example the entire pygame window)
    - containers_tup is a tuple.
            * Each element is a fraction (ex "1/10") indicating
                the HEIGHT of the container as a fraction of the surface it will be on
            * Total of all fractions should be 1
    - RETURNS a list of pygame.Rect objects, each of them a container,
        in the order they appear on screen from top to bottom
    """
    containers = []
    # create the containers
    for container in containers_tup:
        rect = pygame.Rect(
            0, 0,
            int(surface.get_rect().width),
            int(surface.get_rect().height * (container))
        )
        containers.append(rect)

    # place the containers
    for i in range(len(containers)):
        if i != 0:
            containers[i].top = containers[i - 1].bottom

    return containers
