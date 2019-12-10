def create_pixel_row(width, pixel):
    """ creates and returns a "row" of pixels with the specified width
        in which all of the pixels have the RGB values specified by pixel.
        input: width is a non-negative integer
               pixel is a list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    return [pixel[:] for _ in range(width)]


def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels have the RGB values given by pixel."""
    return [create_pixel_row(width, pixel)[:] for _ in range(height)]


def blank_image(height, width):
    """creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels are green (i.e., have RGB values [0,255,0])."""
    return create_uniform_image(height, width, pixel=[0, 255, 0])


def transpose(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list that is the transpose of pixels. """
    return [list(row) for row in zip(*pixels)]
