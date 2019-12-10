from hmcpng import *

def create_pixel_row(width, pixel):
    """ creates and returns a "row" of pixels with the specified width
        in which all of the pixels have the RGB values specified by pixel.
        input: width is a non-negative integer
               pixel is a list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    row = []
    
    for col_num in range(width):
        row += [pixel]

    return row

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels have the RGB values given by pixel."""
    column = []
    for row_num in range(height):
        column += [create_pixel_row(width, pixel)]

    return column


def blank_image(height, width):
    """creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels are green (i.e., have RGB values [0,255,0])."""
    pixel = [0, 255, 0]
    
    blank = create_uniform_image(height, width, pixel)

    return blank

def transpose(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list that is the transpose of pixels. """
    height = len(pixels[0])
    width = len(pixels)
    new_pixels = blank_image(height, width)

    for r in range(len(new_pixels)):
        for c in range(len(new_pixels[0])):
            new_pixels[r][c] = pixels[c][r]

    return new_pixels
