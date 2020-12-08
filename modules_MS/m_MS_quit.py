# Daniel Zhuo
# Modern Snek Module - Credits Menu
# State 6

import os
import sys

import pygame as pg

from . import config as c
from . import m_MS_menu_fades
from .colours import *

# Screens/Surfaces
credits_menu = pg.display.set_mode((c.width, c.height), c.surface_flags)

# Media
credits_image = pg.image.load(os.getcwd() + "/resources_MS/credits.png").convert()


def quit_game(screen, clock, fps, dt):
    """Shuts down program
    Args:
        screen::surface
            Usually the main program surface: Used to blit
        clock::pygame.time.Clock()
            Used to set the Framerate of the menu
        fps::int
            Used in conjunction with clock; specifies program FPS - Set from m_MS_options
        dt::float
            Delta time is calculated from the main loop, and allows for framerate independence
            when it's multiplied by any variable speed. Currently runs at 60FPS (16.7ms)
            --> https://www.youtube.com/watch?v=OmkAUzvwsDk&t=142s
    """
    screen.fill(black)
    pg.mixer.fadeout(500)  # Fade all audio out

    if m_MS_menu_fades.trans_alpha != 0:  # Renders overlay only when fading
        m_MS_menu_fades.dissolve_in(dt, clock, fps)  # Fade in screen
    else:
        pg.quit()
        sys.exit()

    clock.tick(fps)
