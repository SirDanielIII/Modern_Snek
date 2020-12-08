# Daniel Zhuo
# Modern Snek Module - Back Button

import pygame as pg
from pygame import gfxdraw

from . import config as c
from . import m_MS_menu_fades
from . colours import *

button = None
button_colour = white
button_filled = pg.Color("#fdc328")


def back_button(screen, go, clock, fps, dt):
    """Function to run Credits menu
    Args:
        screen::surface
            Usually the main program surface: Used to blit
        go::bool
            Boolean that returns to specified state if True
        clock::pygame.time.Clock()
            Used to set the Framerate of the menu
        fps::int
            Used in conjunction with clock; specifies program FPS - Set from m_MS_options
        dt::float
            Delta time is calculated from the main loop, and allows for framerate independence
            when it's multiplied by any variable speed. Currently runs at 60FPS (16.7ms)
            --> https://www.youtube.com/watch?v=OmkAUzvwsDk&t=142s
    """
    global button, button_colour
    mx, my = pg.mouse.get_pos()  # Get mouse position

    # Triangle Coordinates
    tri_x1, tri_y1 = 20, 50  # Left Point
    tri_x2, tri_y2 = tri_x1 + 55, tri_y1 - 35  # Bottom Right
    tri_x3, tri_y3 = tri_x1 + 55, tri_y1 + 35  # Top Right

    # Draw Anti-Aliased Triangle
    button = pg.draw.polygon(screen, button_colour, [[tri_x1, tri_y1], [tri_x2, tri_y2], [tri_x3, tri_y3]])
    pg.gfxdraw.aatrigon(screen, tri_x1, tri_y1, tri_x2, tri_y2, tri_x3, tri_y3, button_colour)  # Antialiasing

    # Collision Check
    if button.collidepoint((mx, my)):
        button_colour = button_filled
    else:
        button_colour = white

    # If button pressed
    if go:
        m_MS_menu_fades.dissolve_out(dt, clock, fps)  # Activates Dissolve Out Function
        if m_MS_menu_fades.trans_alpha >= 300:
            c.state = c.return_state  # Return to set state
