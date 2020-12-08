# Daniel Zhuo
# Modern Snek Module - Main Menu
# State 1

import os

import pygame as pg

from . import config as c
from . import m_MS_HTP
from . import m_MS_audio_sys as a
from . import m_MS_credits
from . import m_MS_extra_modules
from . import m_MS_menu_fades
from . import m_MS_mode
from . import m_MS_options
from . import m_MS_snek_assets as SA
from .colours import *

# Screens/Surfaces
menu_main = pg.display.set_mode((c.width, c.height), c.surface_flags)
header_box = pg.Surface((c.width, c.height), flags=pg.HWSURFACE and pg.SRCALPHA).convert_alpha()  # Header Overlay
header_box.set_alpha(153)  # Make Header Translucent
pg.draw.rect(header_box, c.ms_game_dark_green, (0, 0, c.width, 350))

# Media
main_menu_logo = pg.image.load(os.getcwd() + "/resources_MS/main_menu_logo.png").convert_alpha()  # Load main menu logo
grid = pg.image.load(os.getcwd() + "/resources_MS/default_grid.png").convert()  # Load main menu logo

# Font Sizes
snek_hat_f = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 100)
font_options = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 75)
font_htp = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 65)
font_play_game = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 125)

# Global Variables
change = 1

# Text Highlight Colours
mm_c_play = white
mm_c_options = white
mm_c_htp = white
mm_c_cred = white
mm_c_quit = white


def main_menu(screen, click, clock, fps, dt):  # Loading Bar Animation
    """Function to run Main Menu
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
    # ------------------------------------------------------------------------------------------------------------------
    global mm_c_play, mm_c_options, mm_c_htp, mm_c_cred, mm_c_quit, change
    # ------------------------------------------------------------------------------------------------------------------
    mx, my = pg.mouse.get_pos()  # Get mouse position
    # ------------------------------------------------------------------------------------------------------------------
    menu_main.blit(grid, (0, 0))  # Grid Background
    # ------------------------------------------------------------------------------------------------------------------
    # Buttons
    choose_mode = pg.draw.rect(menu_main, c.ms_blue, (100, 400, 650, 150))  # Play Game
    m_MS_extra_modules.draw_text("Play Game", mm_c_play, font_play_game, menu_main, 425, 475)

    options_menu = pg.draw.rect(menu_main, c.ms_blue, (100, 600, 300, 100))  # Options
    m_MS_extra_modules.draw_text("Options", mm_c_options, font_options, menu_main, 250, 650)

    htp_menu = pg.draw.rect(menu_main, c.ms_blue, (450, 600, 300, 100))  # How to Play
    m_MS_extra_modules.draw_text("How to Play", mm_c_htp, font_htp, menu_main, 600, 650)

    credits_menu = pg.draw.rect(menu_main, c.ms_blue, (100, 750, 300, 100))  # Credits
    m_MS_extra_modules.draw_text("Credits", mm_c_cred, font_options, menu_main, 250, 800)

    close_game = pg.draw.rect(menu_main, c.ms_blue, (450, 750, 300, 100))  # Quit Game
    m_MS_extra_modules.draw_text("Quit Game", mm_c_quit, font_options, menu_main, 600, 800)
    # ------------------------------------------------------------------------------------------------------------------
    # Rick Roll Easter Egg
    if SA.snek_rect.collidepoint((mx, my)):
        if click:
            c.rick_roll = not c.rick_roll  # Enables Rick Roll Easter Egg
            # Click Sound Effect
            if c.rick_roll:
                a.dj(False, False, False, False, c.channel5, 0, False, c.channel5, a.activate_rick_roll_s)
            else:
                if c.rick_rolled:
                    a.dj(True, False, False, False, c.channel1,
                         500, True, c.channel5, a.deactivate_rick_roll_s)  # Audio Handler
                else:
                    a.dj(True, False, False, False, c.channel5, 0, False, c.channel5, a.deactivate_rick_roll_s)
                c.rick_rolled = False  # Reset Value
    # ------------------------------------------------------------------------------------------------------------------
    # Show Text
    if c.rick_roll:
        always_gonna = font_htp.render("Always gonna", True, white)
        snek_hat = snek_hat_f.render("SNEK HAT", True, white)
        menu_main.blit(always_gonna, (850, 489))
        menu_main.blit(snek_hat, (900, 545))
    # ------------------------------------------------------------------------------------------------------------------
    menu_main.blit(SA.snek, SA.snek_rect)
    # ------------------------------------------------------------------------------------------------------------------
    # Play Game
    if choose_mode.collidepoint((mx, my)):
        mm_c_play = c.ms_yellow
        if click:
            change = 2  # Go to mode module
            if not c.rick_rolled:
                a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                a.dj(False, True, False, False, c.channel0, 500, True, c.channel3, a.m_click)  # Audio Handler
            else:
                a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    else:
        mm_c_play = white
    # ------------------------------------------------------------------------------------------------------------------
    # Options
    if options_menu.collidepoint((mx, my)):
        mm_c_options = c.ms_yellow
        if click:
            change = 3  # Go to options module
            a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
            a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    else:
        mm_c_options = white
    # ------------------------------------------------------------------------------------------------------------------
    # How to Play
    if htp_menu.collidepoint((mx, my)):
        mm_c_htp = c.ms_yellow
        if click:
            change = 4  # Go to how to play module
            a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
            a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    else:
        mm_c_htp = white
    # ------------------------------------------------------------------------------------------------------------------
    # Credits
    if credits_menu.collidepoint((mx, my)):
        mm_c_cred = c.ms_yellow
        if click:
            change = 5
            a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
            a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
        # else:
    else:
        mm_c_cred = white
    # ------------------------------------------------------------------------------------------------------------------
    # Quit Game
    if close_game.collidepoint((mx, my)):
        mm_c_quit = c.ms_yellow
        if click:
            change = 6
            a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
            a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    else:
        mm_c_quit = white
    # ------------------------------------------------------------------------------------------------------------------
    screen.blit(header_box, (0, 0))
    menu_main.blit(main_menu_logo, (0, 0))
    screen.blit(menu_main, (0, 0))  # Draws menu screen to main screen
    # ------------------------------------------------------------------------------------------------------------------
    clock.tick(fps)
    # ------------------------------------------------------------------------------------------------------------------
    if change != 1:
        m_MS_menu_fades.dissolve_out(dt, clock, fps)
        # Fade Bug Prevention
        m_MS_mode.go_back = False
        m_MS_HTP.go_back = False
        m_MS_credits.go_back = False
        m_MS_options.go_back = False
        if m_MS_menu_fades.trans_alpha >= 300:
            c.state = change
    else:
        m_MS_menu_fades.dissolve_in(dt, clock, fps)
