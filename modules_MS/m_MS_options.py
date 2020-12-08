# Daniel Zhuo
# Modern Snek Module - Options Menu
# State 3

import os

import pygame as pg

from . import config as c
from . import m_MS_audio_sys as a
from . import m_MS_extra_modules
from . import m_MS_main_menu
from . import m_MS_menu_back
from . import m_MS_menu_fades
from . import m_MS_snek_assets as SA
from .colours import *

# Media
grid = pg.image.load(os.getcwd() + "/resources_MS/default_grid.png").convert()  # Load main menu logo

# Screens/Surfaces
options_menu = pg.display.set_mode((c.width, c.height), c.surface_flags).convert()

# Background Grid
grid_background = pg.Surface((c.width, c.height), c.surface_flags)
grid_background.blit(grid, (0, 0))

# Background Overlay
grid_back_overlay = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
pg.draw.rect(grid_back_overlay, pg.Color('#487631'), (0, 0, c.width, c.height))
grid_back_overlay.set_alpha(153)  # 60% Dark Green Overlay

# Header Overlay
grid_back_header = pg.Surface((c.width, 150), c.surface_flags).convert_alpha()
pg.draw.rect(grid_back_header, pg.Color('#487631'), (0, 0, c.width, 150))
grid_back_header.set_alpha(153)  # 60% Header Overlay

# Blit Surfaces Into One Before Loop To Save Performance
grid_background.blit(grid_back_overlay, (0, 0))
grid_background.blit(grid_back_header, (0, 0))

# Fonts
f_title = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 100)
f_sub_menu = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 65)
f_setting = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 45)

# Global Variables
go_back = False
# -----------------------------------
# Settings - Global Variables
# FPS
fps_potato = False
fps_30 = False
fps_60 = True
fps_75 = False
fps_165 = False
fps_o0 = None
fps_o1 = None
fps_o2 = None
fps_o3 = None
fps_o4 = None
fps_new = 60  # Sets 60 FPS to be the Default
# Game Settings
speed_increase_o = None
fruit_timer_o = None
WASD_o = None
show_fps = False
# Music
sfx_o = None
music_o = None
selected_sfx = False
selected_music = False
selected_sfx_o = None
selected_music_o = None
sfx_button_x, sfx_button_y = 1425, 362.5
music_button_x, music_button_y = 1425, 512.5
sfx_volume = 1.0
music_volume = 1.0


# ----------------------------------------------------------------------------------------------------------------------
def options(screen, click, clock, fps, dt):
    """Function to run Options menu
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
    global go_back, fps_potato, fps_30, fps_60, fps_75, fps_165, fps_o0, fps_o1, fps_o2, fps_o3, fps_o4, fps_new, \
        speed_increase_o, fruit_timer_o, WASD_o, show_fps, sfx_o, music_o, selected_sfx, \
        selected_music, selected_sfx_o, selected_music_o, sfx_button_x, sfx_button_y, \
        music_button_x, music_button_y, sfx_volume, music_volume
    mx, my = pg.mouse.get_pos()  # Get mouse position
    # -----------------------------------------------------------------
    options_menu.blit(grid_background, (0, 0))  # Draw Grid Background
    # -----------------------------------------------------------------
    # Header Text
    m_MS_extra_modules.draw_text("Options", white, f_title, options_menu, c.width / 2, 75)
    # ------------------------------------------------------------------------------------------------------------------
    # FPS Mode - Rectangles
    m_MS_extra_modules.draw_text("FPS Modes", c.ms_yellow, f_sub_menu, options_menu, 200, 250)
    fps_1 = pg.Rect(100, 300, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, fps_1)
    fps_2 = pg.Rect(100, 400, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, fps_2)
    fps_3 = pg.Rect(100, 500, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, fps_3)
    fps_4 = pg.Rect(100, 600, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, fps_4)
    fps_5 = pg.Rect(100, 700, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, fps_5)

    # Button Collisions
    if fps_1.collidepoint((mx, my)) and not fps_potato:
        m_MS_extra_modules.draw_rect_outline(options_menu, fps_1, c.ms_yellow, 5)
        if click:
            fps_potato = True
            fps_30 = False
            fps_60 = False
            fps_75 = False
            fps_165 = False
            fps_new = 10
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound

    elif fps_2.collidepoint((mx, my)) and not fps_30:
        m_MS_extra_modules.draw_rect_outline(options_menu, fps_2, c.ms_yellow, 5)
        if click:
            fps_potato = False
            fps_30 = True
            fps_60 = False
            fps_75 = False
            fps_165 = False
            fps_new = 30
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif fps_3.collidepoint((mx, my)) and not fps_60:
        m_MS_extra_modules.draw_rect_outline(options_menu, fps_3, c.ms_yellow, 5)
        if click:
            fps_potato = False
            fps_30 = False
            fps_60 = True
            fps_75 = False
            fps_165 = False
            fps_new = 60
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif fps_4.collidepoint((mx, my)) and not fps_75:
        m_MS_extra_modules.draw_rect_outline(options_menu, fps_4, c.ms_yellow, 5)
        if click:
            fps_potato = False
            fps_30 = False
            fps_60 = False
            fps_75 = True
            fps_165 = False
            fps_new = 75
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif fps_5.collidepoint((mx, my)) and not fps_165:
        m_MS_extra_modules.draw_rect_outline(options_menu, fps_5, c.ms_yellow, 5)
        if click:
            fps_potato = False
            fps_30 = False
            fps_60 = False
            fps_75 = False
            fps_165 = True
            fps_new = 165
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound

    # Applying Options
    if fps_potato:
        fps_o0 = pg.Rect(100 + 5, 300 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, fps_o0)
    elif fps_30:
        fps_o1 = pg.Rect(100 + 5, 400 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, fps_o1)
    elif fps_60:
        fps_o2 = pg.Rect(100 + 5, 500 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, fps_o2)
    elif fps_75:
        fps_o3 = pg.Rect(100 + 5, 600 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, fps_o3)
    elif fps_165:
        fps_o4 = pg.Rect(100 + 5, 700 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, fps_o4)

    # FPS Mode - Text
    fps_t1 = f_setting.render("Potato", True, white)
    options_menu.blit(fps_t1, (200, 300))
    fps_t2 = f_setting.render("30 FPS", True, white)
    options_menu.blit(fps_t2, (200, 400))
    fps_t3 = f_setting.render("60 FPS", True, white)
    options_menu.blit(fps_t3, (200, 500))
    fps_t4 = f_setting.render("75 FPS", True, white)
    options_menu.blit(fps_t4, (200, 600))
    fps_t5 = f_setting.render("165 FPS", True, white)
    options_menu.blit(fps_t5, (200, 700))
    # ------------------------------------------------------------------------------------------------------------------
    # Game Settings - Rectangles
    m_MS_extra_modules.draw_text("Game Settings", c.ms_yellow, f_sub_menu, options_menu, 588, 250)
    speed_i = pg.Rect(450, 300, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, speed_i)
    fruit_t = pg.Rect(450, 400, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, fruit_t)
    wasd_c = pg.Rect(450, 500, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, wasd_c)
    arrow_k_c = pg.Rect(450, 600, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, arrow_k_c)
    show_fps_c = pg.Rect(450, 700, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, show_fps_c)
    # Button Collisions
    if speed_i.collidepoint((mx, my)):
        m_MS_extra_modules.draw_rect_outline(options_menu, speed_i, c.ms_yellow, 5)
        if click:
            c.speed_increase_e = not c.speed_increase_e
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif fruit_t.collidepoint((mx, my)):
        m_MS_extra_modules.draw_rect_outline(options_menu, fruit_t, c.ms_yellow, 5)
        if click:
            c.fruit_timer_e = not c.fruit_timer_e
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif wasd_c.collidepoint((mx, my)) and not c.WASD_e:
        m_MS_extra_modules.draw_rect_outline(options_menu, wasd_c, c.ms_yellow, 5)
        if click:
            c.WASD_e = True
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif arrow_k_c.collidepoint((mx, my)) and c.WASD_e:
        m_MS_extra_modules.draw_rect_outline(options_menu, arrow_k_c, c.ms_yellow, 5)
        if click:
            c.WASD_e = False
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    elif show_fps_c.collidepoint((mx, my)):
        m_MS_extra_modules.draw_rect_outline(options_menu, show_fps_c, c.ms_yellow, 5)
        if click:
            show_fps = not show_fps
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound

    # Applying Settings
    if c.speed_increase_e:
        speed_increase_o = pg.Rect(450 + 5, 300 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_blue, speed_increase_o)
        speed_i_t = f_setting.render("Gradual Speed Increase (Enabled)", True, white)
        options_menu.blit(speed_i_t, (550, 300))
    else:
        speed_i_t = f_setting.render("Gradual Speed Increase (Disabled)", True, white)
        options_menu.blit(speed_i_t, (550, 300))
    if c.fruit_timer_e:
        fruit_timer_o = pg.Rect(450 + 5, 400 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, fruit_timer_o)
        fruit_t_t = f_setting.render("Fruit Timer (Enabled)", True, white)
        options_menu.blit(fruit_t_t, (550, 400))
    else:
        speed_i_t = f_setting.render("Fruit Timer (Disabled)", True, white)
        options_menu.blit(speed_i_t, (550, 400))
    if c.WASD_e:
        WASD_o = pg.Rect(450 + 5, 500 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_green, WASD_o)
    else:
        WASD_o = pg.Rect(450 + 5, 600 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_green, WASD_o)
    if show_fps:
        show_fps_o = pg.Rect(450 + 5, 700 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_grey2, show_fps_o)
        speed_i_t = f_setting.render("Show FPS (Enabled)", True, white)
        options_menu.blit(speed_i_t, (550, 700))
    else:
        speed_i_t = f_setting.render("Show FPS (Disabled)", True, white)
        options_menu.blit(speed_i_t, (550, 700))

    # Game Settings - Text
    wasd_c_t = f_setting.render("WASD Controls", True, white)
    options_menu.blit(wasd_c_t, (550, 500))
    arrow_k_c_t = f_setting.render("Arrow Key Controls", True, white)
    options_menu.blit(arrow_k_c_t, (550, 600))
    # ------------------------------------------------------------------------------------------------------------------
    # Music - Rectangles
    m_MS_extra_modules.draw_text("Music", c.ms_yellow, f_sub_menu, options_menu, 1156, 250)  # Header
    sound_effects_b = pg.Rect(1100, 300, c.square_grid, c.square_grid)  # SFX Button
    pg.draw.rect(options_menu, white, sound_effects_b)
    music_b = pg.Rect(1100, 450, c.square_grid, c.square_grid)  # Music Button
    pg.draw.rect(options_menu, white, music_b)

    # Buttons
    # SFX
    if sound_effects_b.collidepoint((mx, my)):
        m_MS_extra_modules.draw_rect_outline(options_menu, sound_effects_b, c.ms_yellow, 5)
        if click:
            c.sfx_e = not c.sfx_e
            a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ding)  # Ding Sound
    # Music
    elif music_b.collidepoint((mx, my)):
        m_MS_extra_modules.draw_rect_outline(options_menu, music_b, c.ms_yellow, 5)
        if click:
            c.music_e = not c.music_e
            if c.return_state == 1:
                if not c.rick_rolled:
                    a.dj(True, False, False, False, c.channel3, 0, True, c.channel3, a.ding)  # Click Sound
                else:
                    a.dj(False, False, False, False, c.channel3, 0, True, c.channel3, a.ding)  # Click Sound
            elif c.return_state == 7:
                a.dj(False, False, True, False, c.channel3, 0, True, c.channel3, a.ding)  # Click Sound

    # Applying Settings
    if c.sfx_e:
        sfx_o = pg.Rect(1100 + 5, 300 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_blue, sfx_o)
        speed_i_t = f_setting.render(f"Sound Effects ({str(int(sfx_volume * 100))}%)", True, white)
        options_menu.blit(speed_i_t, (1200, 300))
    else:
        sound_effects_t = f_setting.render("Sound Effects (Disabled)", True, white)
        options_menu.blit(sound_effects_t, (1200, 300))

    if c.music_e:
        music_o = pg.Rect(1100 + 5, 450 + 5, c.square_grid - 10, c.square_grid - 10)
        pg.draw.rect(options_menu, c.ms_red, music_o)
        speed_i_t = f_setting.render(f"Music ({str(int(music_volume * 100))}%)", True, white)
        options_menu.blit(speed_i_t, (1200, 450))
    else:
        sound_effects_t = f_setting.render("Music (Disabled)", True, white)
        options_menu.blit(sound_effects_t, (1200, 450))

    # Drawing Volume Bars
    bar_length = 250
    sfx_bar = pg.Rect(1200, 375, bar_length, c.square_grid / 2)
    music_bar = pg.Rect(1200, 525, bar_length, c.square_grid / 2)
    pg.draw.rect(options_menu, white, sfx_bar)
    pg.draw.rect(options_menu, white, music_bar)

    # Music Bar Buttons
    # SFX
    sfx_button = pg.Rect(sfx_button_x, sfx_button_y, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, sfx_button)
    selected_sfx_o = pg.Rect(sfx_button_x + 5, sfx_button_y + 5, c.square_grid - 10, c.square_grid - 10)
    if c.sfx_e:
        pg.draw.rect(options_menu, c.ms_green, selected_sfx_o)
    else:
        pg.draw.rect(options_menu, c.ms_grey1, selected_sfx_o)
    # Music
    music_button = pg.Rect(music_button_x, music_button_y, c.square_grid, c.square_grid)
    pg.draw.rect(options_menu, white, music_button)
    selected_music_o = pg.Rect(music_button_x + 5, music_button_y + 5, c.square_grid - 10, c.square_grid - 10)

    if c.music_e:
        pg.draw.rect(options_menu, c.ms_green, selected_music_o)
    else:
        pg.draw.rect(options_menu, c.ms_grey1, selected_music_o)

    # SFX Slider Button
    if sfx_button.collidepoint((mx, my)) and c.sfx_e and not selected_music:  # Sound Effects Button
        m_MS_extra_modules.draw_rect_outline(options_menu, sfx_button, c.ms_yellow, 5)
        # Click SFX
        if c.mouse_down:
            selected_sfx = True
            c.just_released = True
        if click:
            if selected_sfx:
                a.dj(False, False, False, False, c.channel3, 100, True, c.channel3, a.plop_1)  # Click Sound

    # Music Slider Button
    elif music_button.collidepoint((mx, my)) and c.music_e and not selected_sfx:
        m_MS_extra_modules.draw_rect_outline(options_menu, music_button, c.ms_yellow, 5)
        if c.mouse_down:
            selected_music = True
            c.just_released = True
        # Click SFX
        if click:
            if selected_music:
                a.dj(False, False, False, False, c.channel3, 100, True, c.channel3, a.plop_1)  # Click Sound
    # Unselect buttons when mouse button is released
    if not c.mouse_down:
        if c.just_released:
            a.dj(False, False, False, False, c.channel3, 100, True, c.channel3, a.plop_2)  # Click Sound
            c.just_released = False
            selected_music = False
            selected_sfx = False
    # Button Selection
    # Sound Effects
    if selected_sfx:
        m_MS_extra_modules.draw_rect_outline(options_menu, sfx_button, c.ms_yellow, 5)
        if 1200 <= mx <= 1450:
            sfx_button_x = mx - c.square_grid / 2
        elif mx <= 1200:
            sfx_button_x = 1175
        elif 1450 <= mx:
            sfx_button_x = 1425

    elif selected_music:
        m_MS_extra_modules.draw_rect_outline(options_menu, music_button, c.ms_yellow, 5)
        if 1200 <= mx <= 1450:
            music_button_x = mx - c.square_grid / 2
        elif mx <= 1200:
            music_button_x = 1175
        elif 1450 <= mx:
            music_button_x = 1425

    # Functions to Calculate Volume Based on X Button Coordinates
    c_sfx_volume(sfx_button_x + c.square_grid / 2)  # Sends Rect Center For Volume Calculation
    c_music_volume(music_button_x + c.square_grid / 2)  # Sends Rect Center For Volume Calculation
    # ------------------------------------------------------------------------------------------------------------------
    # Note Block Easter Egg
    options_menu.blit(SA.snek_options, SA.snek_options_rect)
    options_menu.blit(SA.jukebox, SA.jukebox_rect)
    # ------------------------------------------------------------------------------------------------------------------
    # Check Noteblock Collision
    if SA.jukebox_rect.collidepoint((mx, my)):
        if click:
            SA.snek_box = not SA.snek_box
            if not c.pause and not c.rick_rolled:  # Don't switch songs if Rick Rolled
                c.channel1.fadeout(500)  # Fades out music if playing
                if c.state == 3:
                    a.dj(True, False, False, False, c.channel0, 500, True, c.channel3, a.m_click)  # Audio Handler
            else:
                a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    # ------------------------------------------------------------------------------------------------------------------
    if SA.snek_box:  # Draw Text
        m_MS_extra_modules.draw_text("Snek Box", white, f_setting, options_menu, 975, 725)
    # ------------------------------------------------------------------------------------------------------------------
    screen.blit(options_menu, (0, 0))  # Blit Surfaces Onto Screen
    # ----------------------------------------------------------------------------------------------------------------------
    # Fading
    if not go_back:
        if m_MS_menu_fades.trans_alpha >= 0:  # Renders overlay only when fading
            m_MS_menu_fades.dissolve_in(dt, clock, fps)  # Fade in screen

    if click and m_MS_menu_back.button.collidepoint((mx, my)):  # Checking Button Collision
        m_MS_main_menu.change = 1
        go_back = True
        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
        a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    # ----------------------------------------------------------------------------------------------------------------------
    clock.tick(fps)
    # ----------------------------------------------------------------------------------------------------------------------
    return m_MS_menu_back.back_button(screen, go_back, clock, fps, dt)  # Returns to main menu


# ----------------------------------------------------------------------------------------------------------------------
def c_sfx_volume(sfx_v):  # Takes in button center for calculation
    global sfx_volume
    '''
    Takes in the X-coord, sets its range to 0-250 by subtracting 1200. To normalize it to a range of 0-100, 
    we divide the number by 2.5, giving us a percentage value that we divide again by 100 to get a usable number
    to set the pygame audio channel volume with. 
    '''
    sfx_volume = ((sfx_v - 1200) / 2.5) / 100


# ----------------------------------------------------------------------------------------------------------------------
def c_music_volume(music_v):
    global music_volume
    '''
    Takes in the X-coord, sets its range to 0-250 by subtracting 1200. To normalize it to a range of 0-100, 
    we divide the number by 2.5, giving us a percentage value that we divide again by 100 to get a usable number
    to set the pygame audio channel volume with. 
    '''
    music_volume = ((music_v - 1200) / 2.5) / 100
