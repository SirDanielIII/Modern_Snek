# Daniel Zhuo
# Modern Snek Module - Fade Functions

import pygame as pg

from . import config as c
from . import m_MS_HTP
from . import m_MS_credits
from . import m_MS_main_menu
from . import m_MS_options

# Screens/Surfaces
transition = pg.Surface((c.width, c.height), c.surface_flags).convert()
transition.fill(pg.Color("#8bce46"))
transition.set_alpha(0)

trans_alpha = 0


def dissolve_out(dt, clock, fps):
    """Function to dissolve screen out
    Args:
        dt::float
            Delta time is calculated from the main loop, and allows for framerate independence
            when it's multiplied by any variable speed. Currently runs at 60FPS (16.7ms)
            --> https://www.youtube.com/watch?v=OmkAUzvwsDk&t=142s
        clock::pygame.time.Clock()
            Used to set the Framerate of the menu
        fps::int
            Used in conjunction with clock; specifies program FPS - Set from m_MS_options
    """
    global trans_alpha
    if trans_alpha < 300:
        trans_alpha += 10 * dt
        if trans_alpha >= 300:
            trans_alpha = 300
            return False
    transition.set_alpha(trans_alpha)
    clock.tick(fps)


def dissolve_in(dt, clock, fps):
    """Function to dissolve screen in
    Args:
        dt::float
            Delta time is calculated from the main loop, and allows for framerate independence
            when it's multiplied by any variable speed. Currently runs at 60FPS (16.7ms)
            --> https://www.youtube.com/watch?v=OmkAUzvwsDk&t=142s
        clock::pygame.time.Clock()
            Used to set the Framerate of the menu
        fps::int
            Used in conjunction with clock; specifies program FPS - Set from m_MS_options
    """
    global trans_alpha
    if trans_alpha > 0:
        trans_alpha -= 10 * dt
        if trans_alpha <= 0:
            # Reset Different Menu Global Variables
            m_MS_credits.go_back = False
            m_MS_options.go_back = False
            m_MS_HTP.go_back = False
            m_MS_main_menu.change = 1
            trans_alpha = 0
            return False
    transition.set_alpha(trans_alpha)
    clock.tick(fps)
