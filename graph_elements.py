""" a file holding functions to draw commonly used shapes and graphical elements in pygame """

def draw_frame(surface, rect, color_fill, color_border, border=1):
    """
    Creates and draws a rect woth a frame. Returns the inside rect object.
    returns rect obj of inside frame
    ** surface: the pygame surface to draw this on
    ** rect: rect object for the outer frame
    ** color: colors (in pygame accepted format) for the border and the fill
    ** border: border thickness, in pixel
    """
    surface.fill(color_border, rect)
    inside_rect = rect.inflate(-border*2, -border*2)
    surface.fill(color_fill, inside_rect)
    return inside_rect