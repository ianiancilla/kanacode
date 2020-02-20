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

# def render_multi_line(text, x, y, fsize)    # TODO check this and implement
#     lines = text.splitlines()
#     for i, l in enumerate(lines):
#         screen.blit(sys_font.render(l, 0, hecolor), (x, y + fsize * i))


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


def create_containers(surface, containers_iter, layout="H"):
    """
    creates and places container rects to help layout.
    Containers divide the entire width(layout="H") or height(layout="V") of surface
    and are placed on it with no margins between them.
    :param surface: pygame surface object (for example the entire pygame window)
    :param containers_iter: iterable, in which each element is:
                            * Each element is a fraction (ex "1/10") indicating
                                the width or height of the container (depending on layout
                                 as a fraction of the surface it will be on
                            * Total of all fractions should be 1
    :param layout: can be "H" for horziontal layout (containers_rects next to each other)
                    or "V" for vertical (under each other)
    :return: a list of pygame.Rect objects, each of them a container, in the order they appear on screen
    """
    containers_rects = []

    if not isinstance(surface, pygame.Rect):
        surface = surface.get_rect()

    # create the containers_rects
    for container_fract in containers_iter:
        if layout == "H":
            rect = pygame.Rect(
                surface.left, surface.top,
                int(surface.width * container_fract),
                int(surface.height)
            )
        elif layout == "V":
                rect = pygame.Rect(
                    surface.left, surface.top,
                    int(surface.width),
                    int(surface.height * container_fract)
                )
        else:
            raise TypeError("Improper argument given for layout parameter")

        containers_rects.append(rect)


    # place the containers_rects
    for i in range(len(containers_rects)):
        if i != 0:
            if layout == "H":
                containers_rects[i].left = containers_rects[i - 1].right
            elif layout == "V":
                containers_rects[i].top = containers_rects[i - 1].bottom
            else:
                raise TypeError("Improper argument given for layout parameter")

    return containers_rects
