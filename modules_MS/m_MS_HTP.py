# Daniel Zhuo
# Modern Snek Module - How to Play Menu
# State 4

import os

import pygame as pg

from . import config as c
from . import m_MS_audio_sys as a
from . import m_MS_main_menu
from . import m_MS_menu_back
from . import m_MS_menu_fades

# Screens/Surfaces
htp = pg.display.set_mode((c.width, c.height), c.surface_flags)

# Media
htp_picture = pg.image.load((os.getcwd() + "/resources_MS/how_to_play.png"))

# Global Variables
go_back = False


def how_to_play(screen, click, clock, fps, dt):
    """Function to run How to Play menu
    Args:
        screen::surface
            Usually the main program surface: Used to blit
        click::bool
            Boolean that turns False immediately when True, allows for menu interaction & audio switches
        clock::pygame.time.Clock()
            Used to set the Framerate of the menu
        fps::int
            Used in conjunction with clock; specifies program FPS - Set from m_MS_options
        dt::float
            Delta time is calculated from the main loop, and allows for framerate independence
            when it's multiplied by any variable speed. Currently runs at 60FPS (16.7ms)
            --> https://www.youtube.com/watch?v=OmkAUzvwsDk&t=142s
    """
    global go_back
    # ------------------------------------------------------------------------------------------------------------------
    mx, my = pg.mouse.get_pos()  # Get mouse position
    # ------------------------------------------------------------------------------------------------------------------
    screen.blit(htp_picture, (0, 0))  # Blit picture to main screen
    # ------------------------------------------------------------------------------------------------------------------
    # Fading
    if not go_back:
        if m_MS_menu_fades.trans_alpha != 0:  # Renders overlay only when fading
            m_MS_menu_fades.dissolve_in(dt, clock, fps)  # Fade in screen

    if click and m_MS_menu_back.button.collidepoint((mx, my)):  # Checking Button Collision
        m_MS_main_menu.change = 1
        go_back = True
        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
        a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound

    clock.tick(fps)

    return m_MS_menu_back.back_button(screen, go_back, clock, fps, dt)  # Returns to main menu
