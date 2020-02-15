""" a series of functions to help with common needs in pygame """


def create_centered_text(str, font, font_color, container):
    """ creates an image and a rect for easy blitting of text """
    # create text image
    str_img, str_rect = font.render(str, font_color)
    str_rect.center = container.center
    return str_img, str_rect
