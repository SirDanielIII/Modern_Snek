# Daniel Zhuo
# Modern Snek Module - Extra Modules

import pygame as pg
from pygame import gfxdraw


def draw_text(text, colour, font_type, screen, x, y):  # Draws Centered Text
    """Function that centers text in Pygame
    Args:
        text::str
            String text to be centered
        colour::tuple
            Pretty self explanatory
        font_type::pg.font.SysFont("string", int)
            Specify which font to use
        screen::surface
            Specify which surface to blit centered text on
        x::float
            The x value of centered text
        y::float
            The y value of centered text
    """
    text_obj = font_type.render(text, True, colour)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


def draw_rect_outline(screen, rect, colour, width=1):
    """This function properly draws a stroke inside/outside a rectangle
    Args:
        screen::surface
            Specify which surface to blit rectangle on
        rect::pygame.Rect(x1, y1, x2, y2)
            Rectangle to have a stroke (haha I'm funny)
        colour::tuple
            Pretty self explanatory
        width::int
            Sets stroke width
    Notes:
        This function requires you to import gfxdraw
        Invert operator directions for outer stroke
        --> pygame.gfxdraw.rectangle(screen, (x - i, y - i, w + i * 2, h + i * 2), colour)
    """
    x, y, w, h = rect
    width = max(width, 1)  # Draw at least one rect
    width = min(min(width, w // 2), h // 2)  # Don't overdraw

    # This draws several smaller outlines inside the first outline.
    # Invert the direction if it should grow outwards.
    for i in range(width):
        pg.gfxdraw.rectangle(screen, (x + i, y + i, w - i * 2, h - i * 2), colour)


# Displays FPS On Screen (Toggled From Options Module)
def display_fps(enable, screen, clock, font, colour):
    """Function to display program frames per second
    Args:
        enable::boolean
            To enable the display or not
        screen::surface
            Where to blit text
        clock::pygame.time.Clock()
            Used with get_fps() to retrieve current FPS
        font::pygame.font.SysFont("string", int)
            Specify which font to use
        colour::tuple
            Pretty self explanatory
    """
    if enable:
        fps = str(int(clock.get_fps()))  # Retrieves FPS Value
        fps_counter = font.render(f"FPS: {str(fps)}", True, colour)
        screen.blit(fps_counter, (1500, 10))
