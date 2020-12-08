# Daniel Zhuo
# Modern Snek Module - Gamemode Menu
# State 2

import os

import pygame as pg

from . import config as c
from . import m_MS_audio_sys as a
from . import m_MS_extra_modules
from . import m_MS_game
from . import m_MS_main_menu
from . import m_MS_menu_back
from . import m_MS_menu_fades
from . import m_MS_snek_assets as SA
from .colours import *

# Media
grid = pg.image.load(os.getcwd() + "/resources_MS/default_grid.png").convert()  # Load main menu logo

# Screens/Surfaces
menu_mode = pg.display.set_mode((c.width, c.height), c.surface_flags)
# Background Grid
grid_background = pg.Surface((c.width, c.height), c.surface_flags)
grid_background.blit(grid, (0, 0))
# Background Overlays
grid_back_overlay = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
pg.draw.rect(grid_back_overlay, pg.Color('#487631'), (0, 0, c.width, c.height))
grid_back_overlay.set_alpha(153)  # 60% Dark Green Overlay
# Header Overlay
grid_back_header = pg.Surface((c.width, 150), c.surface_flags).convert_alpha()
pg.draw.rect(grid_back_header, pg.Color('#487631'), (0, 0, c.width, 150))
grid_back_header.set_alpha(153)  # 60% Header Overlay
# Card Surfaces
card_background = pg.Surface((850, 500), c.surface_flags)
card_background.fill(black)
card_background.set_alpha(77)  # 30% Black Overlay
card = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()  # Card Surface

# Blit Surfaces Into One Before Loop To Save Performance
grid_background.blit(grid_back_overlay, (0, 0))
grid_background.blit(grid_back_header, (0, 0))

# Fonts
f_modes1 = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 70)
f_modes2 = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 60)
f_title = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 100)
f_sub_menu = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 65)
f_setting = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 45)
f_card = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 35)

# Global Variables
go_back = False
activate_fade = False
fade_end = True
card_fade = 300
switch = "Base"
transition = False
# Text Highlight Colours
gm_c_base = white
gm_c_daniel = white
gm_c_soviet = white
gm_c_covid = white
gm_c_start = white
# Cell Sizes
gm_50px = True
gm_80px = False
gm_25px = False
gm_5px = False


def draw_gm_text():
    """Function to draw Game Menu text"""
    m_MS_extra_modules.draw_text("Base Edition", gm_c_base, f_modes1, menu_mode, 250, 250)
    m_MS_extra_modules.draw_text("Daniel Edition", gm_c_daniel, f_modes2, menu_mode, 650, 250)
    m_MS_extra_modules.draw_text("Soviet Edition", gm_c_soviet, f_modes2, menu_mode, 1000, 250)
    m_MS_extra_modules.draw_text("COVID Edition", gm_c_covid, f_modes2, menu_mode, 1350, 250)
    grid_gen_t = f_sub_menu.render("Grid Generation Size", True, c.ms_yellow)
    menu_mode.blit(grid_gen_t, (100, 412.5))
    grid_gen_0 = f_setting.render("50px - Normal", True, white)
    menu_mode.blit(grid_gen_0, (200, 500))
    grid_gen_1 = f_setting.render("80px - That's What She Said", True, white)
    menu_mode.blit(grid_gen_1, (200, 600))
    grid_gen_2 = f_setting.render("25px - Below Average", True, white)
    menu_mode.blit(grid_gen_2, (200, 700))
    grid_gen_3 = f_setting.render("5px - Absolute Shrimp", True, white)
    menu_mode.blit(grid_gen_3, (200, 800))


# Function Template That Lets Me Easily Edit The Card Contents
def fill_card(font, logo, line1, line2):
    """
    Draws the info card's descriptions and logo
    Args:
        font::pg.font.SysFont("string", int)
            Specify which font to use
        logo::pygame.image.load("directory")
            Specifies which image to display
        line1::str
            Description text - first line
        line2::str
            Description text - second line
    """
    global card_fade
    # Draw Logo
    card.blit(logo, SA.logo_rect_mode)
    # Draw Text
    m_MS_extra_modules.draw_text(line1, white, font, card, 1150, 575)
    m_MS_extra_modules.draw_text(line2, white, font, card, 1150, 625)


def info_card(s_width):
    """The game mode info card
    Args:
        s_width::int
            Standard sizing used to draw elements - currently 50px
    """
    global gm_c_base, gm_c_daniel, gm_c_soviet, gm_c_covid, card_fade, activate_fade
    # -----------------------------------------------------------------
    menu_mode.blit(card_background, (700, 350))  # Dark Background
    card.fill((0, 0, 0, 0))  # Creates Transparent Background for Surface
    # -----------------------------------------------------------------
    # Yellow Bar
    card_bar = pg.Rect(700, 350, s_width / 2, s_width * 10)
    pg.draw.rect(menu_mode, c.ms_yellow, card_bar)
    # -----------------------------------------------------------------
    # Display Descriptions
    if c.m_base_e:
        gm_c_base = c.ms_yellow  # Keep Text Highlighted
        str1 = "The Standard Modern Snek Experience"
        str2 = "Default Graphics, Sounds and Music"
        fill_card(f_card, SA.base_logo, str1, str2)  # Spits Contents into Function Template
    elif c.m_daniel_e:
        gm_c_daniel = c.ms_yellow  # Keep Text Highlighted
        str1 = "The Modern Snek Experience, but WEIRD"
        str2 = "Authentic Sounds & Music by Daniel Zhuo"
        fill_card(f_card, SA.daniel_logo, str1, str2)  # Spits Contents into Function Template
    elif c.m_soviet_e:
        gm_c_soviet = c.ms_yellow  # Keep Text Highlighted
        str1 = "Ah, Hello there Comrade."
        str2 = "A Modern Series Classic Theme"
        fill_card(f_card, SA.soviet_logo, str1, str2)  # Spits Contents into Function Template
    elif c.m_covid_e:
        gm_c_covid = c.ms_yellow  # Keep Text Highlighted
        str1 = "'CORONAVIRUSSS! SH*T IS REAL!"
        str2 = "SH*T IS GETTING REAL!' - Cardi B"
        fill_card(f_card, SA.covid_logo, str1, str2)  # Spits Contents into Function Template
    # ------------------------------------------------------------------------------------------------------------------


def mode(screen, click, clock, fps, dt):
    """Function to run Choose Mode menu
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
    global go_back, gm_c_base, gm_c_daniel, gm_c_soviet, gm_c_covid, gm_80px, gm_50px, gm_25px, gm_5px, \
        gm_c_start, card_fade, activate_fade, fade_end, switch, transition
    square_width = 50  # Sets Standard Width For All The Buttons
    mx, my = pg.mouse.get_pos()  # Get mouse position
    # -----------------------------------------------------------------
    menu_mode.blit(grid_background, (0, 0))  # Draw Menu Background
    # -----------------------------------------------------------------
    # Header Text
    m_MS_extra_modules.draw_text("Choose Gamemode", white, f_title, menu_mode, c.width / 2, 75)
    # ------------------------------------------------------------------------------------------------------------------
    # Gamemode Buttons
    base_e = pg.Rect(100, 200, square_width * 6, square_width * 2)
    daniel_e = pg.Rect(500, 200, square_width * 6, square_width * 2)
    soviet_e = pg.Rect(850, 200, square_width * 6, square_width * 2)
    covid_e = pg.Rect(1200, 200, square_width * 6, square_width * 2)
    # Grid Generation Buttons
    gg_0 = pg.Rect(100, 500, square_width, square_width)
    gg_1 = pg.Rect(100, 600, square_width, square_width)
    gg_2 = pg.Rect(100, 700, square_width, square_width)
    gg_3 = pg.Rect(100, 800, square_width, square_width)
    button_bar = pg.Rect(437.5, 200, square_width / 2, square_width * 2)  # Separator Bar
    # ------------------------------------------------------------------------------------------------------------------
    # Drawing Buttons
    # Game Mode Buttons
    pg.draw.rect(menu_mode, c.ms_blue, base_e)
    pg.draw.rect(menu_mode, c.ms_blue, daniel_e)
    pg.draw.rect(menu_mode, c.ms_blue, soviet_e)
    pg.draw.rect(menu_mode, c.ms_blue, covid_e)
    # Grid Generation Buttons
    pg.draw.rect(menu_mode, white, gg_0)
    pg.draw.rect(menu_mode, white, gg_1)
    pg.draw.rect(menu_mode, white, gg_2)
    pg.draw.rect(menu_mode, white, gg_3)
    pg.draw.rect(menu_mode, c.ms_yellow, button_bar)  # Yellow Separator Bar
    # ------------------------------------------------------------------------------------------------------------------
    # Game Mode Button Collisions
    if base_e.collidepoint((mx, my)) and switch != "Base":
        gm_c_base = c.ms_yellow
        if click:
            switch = "Base"
            activate_fade = True
            fade_end = False
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif not c.m_base_e:  # Reverts text back to white if not selected
        gm_c_base = white
    if daniel_e.collidepoint((mx, my)) and switch != "Daniel":
        gm_c_daniel = c.ms_yellow
        if click:
            switch = "Daniel"
            activate_fade = True
            fade_end = False
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif not c.m_daniel_e:  # Reverts text back to white if not selected
        gm_c_daniel = white
    if soviet_e.collidepoint((mx, my)) and switch != "Soviet":
        gm_c_soviet = c.ms_yellow
        if click:
            switch = "Soviet"
            activate_fade = True
            fade_end = False
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif not c.m_soviet_e:  # Reverts text back to white if not selected
        gm_c_soviet = white
    if covid_e.collidepoint((mx, my)) and switch != "COVID":
        gm_c_covid = c.ms_yellow
        if click:
            switch = "COVID"
            activate_fade = True
            fade_end = False
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif not c.m_covid_e:  # Reverts text back to white if not selected
        gm_c_covid = white
    # ------------------------------------------------------------------------------------------------------------------
    # Grid Generation Button Collisions
    if gg_0.collidepoint((mx, my)) and not gm_50px:
        m_MS_extra_modules.draw_rect_outline(menu_mode, gg_0, c.ms_yellow, 5)
        if click:
            gm_50px = True
            gm_80px = False
            gm_25px = False
            gm_5px = False
            c.cell_size = 50  # Sets Cell Size
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif gg_1.collidepoint((mx, my)) and not gm_80px:
        m_MS_extra_modules.draw_rect_outline(menu_mode, gg_1, c.ms_yellow, 5)
        if click:
            gm_50px = False
            gm_80px = True
            gm_25px = False
            gm_5px = False
            c.cell_size = 80  # Sets Cell Size
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif gg_2.collidepoint((mx, my)) and not gm_25px:
        m_MS_extra_modules.draw_rect_outline(menu_mode, gg_2, c.ms_yellow, 5)
        if click:
            gm_50px = False
            gm_80px = False
            gm_25px = True
            gm_5px = False
            c.cell_size = 25  # Sets Cell Size
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif gg_3.collidepoint((mx, my)) and not gm_5px:
        m_MS_extra_modules.draw_rect_outline(menu_mode, gg_3, c.ms_yellow, 5)
        if click:
            gm_50px = False
            gm_80px = False
            gm_25px = False
            gm_5px = True
            c.cell_size = 5  # Sets Cell Size
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    # ------------------------------------------------------------------------------------------------------------------
    # Selected Grid Generation
    if gm_50px:
        gm_50mx_filled = pg.Rect(100 + 5, 500 + 5, square_width - 10, square_width - 10)
        pg.draw.rect(menu_mode, c.ms_red, gm_50mx_filled)
    elif gm_80px:
        gm_100mx_filled = pg.Rect(100 + 5, 600 + 5, square_width - 10, square_width - 10)
        pg.draw.rect(menu_mode, c.ms_red, gm_100mx_filled)
    elif gm_25px:
        gm_25mx_filled = pg.Rect(100 + 5, 700 + 5, square_width - 10, square_width - 10)
        pg.draw.rect(menu_mode, c.ms_red, gm_25mx_filled)
    elif gm_5px:
        gm_5mx_filled = pg.Rect(100 + 5, 800 + 5, square_width - 10, square_width - 10)
        pg.draw.rect(menu_mode, c.ms_red, gm_5mx_filled)
    # ------------------------------------------------------------------------------------------------------------------
    draw_gm_text()  # Draws Most of the Text in the Menu
    info_card(square_width)  # Displays info card
    # ------------------------------------------------------------------------------------------------------------------
    # Start Button
    start_b = pg.Rect(1000, 700, square_width * 6, square_width * 2)
    pg.draw.rect(card, c.ms_blue, start_b)
    m_MS_extra_modules.draw_text("Start Game", gm_c_start, f_modes1, card, 1150, 750)
    # ------------------------------------------------------------------------------------------------------------------
    # Start Button Collision
    if start_b.collidepoint((mx, my)):
        gm_c_start = c.ms_yellow
        if click:
            # Activate Fade
            m_MS_menu_fades.dissolve_out(dt, clock, fps)
            # Reset Current Function's Transition Value
            transition = True
            # Load Game Elements
            m_MS_game.game_load()

    else:
        gm_c_start = white
    # ------------------------------------------------------------------------------------------------------------------
    card.set_alpha(card_fade)
    menu_mode.blit(card, (0, 0))  # Merge the Card and Menu Screens

    if not fade_end:  # Activate Fade When Button Is Pressed Above
        card_fade_out(dt)
    if card_fade <= 300:  # Automatically Fade Back
        card_fade_in(dt, switch)

    # ------------------------------------------------------------------------------------------------------------------
    # Fading Menus
    if not go_back and not transition:
        if m_MS_menu_fades.trans_alpha != 0:  # Renders overlay only when fading
            m_MS_menu_fades.dissolve_in(dt, clock, fps)  # Fade in screen
            c.last_state = 2

    if click and m_MS_menu_back.button.collidepoint((mx, my)):  # Checking Button Collision
        m_MS_main_menu.change = 1
        go_back = True
        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
        if SA.snek_box:
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.m_click)  # Audio
        elif c.rick_rolled:
            a.dj(True, False, False, False, c.channel1, 500, True, c.channel3, a.m_click)  # Audio
        else:
            a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound

    if transition:  # Becomes True When Start Game Button Is Pressed
        m_MS_menu_fades.dissolve_out(dt, clock, fps)
        if m_MS_menu_fades.trans_alpha >= 300:
            c.state = 7
            transition = False  # Resets Value
    # ------------------------------------------------------------------------------------------------------------------
    clock.tick(fps)
    return m_MS_menu_back.back_button(screen, go_back, clock, fps, dt)  # Returns to main menu


def card_fade_out(dt):
    global card_fade, activate_fade, fade_end
    if card_fade > 0 and activate_fade:
        card_fade -= 25 * dt
        if card_fade <= 0:
            card_fade = 0
            activate_fade = False
            fade_end = False


def card_fade_in(dt, switch_mode):
    global card_fade, activate_fade, fade_end
    # ------------------------------------------
    if card_fade < 300 and not activate_fade:
        card_fade += 10 * dt
        if card_fade >= 300:
            card_fade = 300
            activate_fade = False
            fade_end = True
    # ------------------------------------------
    if card_fade <= 20:
        if switch_mode == "Base":
            c.m_base_e = True
            c.m_daniel_e = False
            c.m_soviet_e = False
            c.m_covid_e = False
        # ------------------------------------------
        elif switch_mode == "Daniel":
            c.m_base_e = False
            c.m_daniel_e = True
            c.m_soviet_e = False
            c.m_covid_e = False
        # ------------------------------------------
        elif switch_mode == "Soviet":
            c.m_base_e = False
            c.m_daniel_e = False
            c.m_soviet_e = True
            c.m_covid_e = False
        # ------------------------------------------
        elif switch_mode == "COVID":
            c.m_base_e = False
            c.m_daniel_e = False
            c.m_soviet_e = False
            c.m_covid_e = True
