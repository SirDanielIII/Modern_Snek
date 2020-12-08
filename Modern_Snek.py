# -----------------------------------------------------------#----------#
# Modern Snek v1.02 Full Release by Sir Daniel III           #----------#
# Coded by Daniel Zhuo | Grade 11 Computer Science (ICS3U1)  #----------#
# -----------------------------------------------------------#----------#
# Features:                                                  #----------#
# 1. Multiple Theme/Game Modes                                 #--------#
# 2. Well Designed User Interface                               #-------#
# 3. Many Customizable Options, Including:                       #------#
#       a) Various Framerate Modes (for your potato PC)            #----#
#       b) Different Game Settings (for the perfect snek game)       #--#
#       c) WASD/Arrow Key Modes (for you weird people using arrow keys) #
#       d) Show FPS (to show how crappy the game is running)         #--#
#       e) Volume Adjustment (so your ears are kept intact)        #----#
# 4. Easter Eggs (snek hat)                                      #------#
# 5. And more! I guess... :D                                   #--------#
# -----------------------------------------------------------#----------#

import os
import sys
import time

# Importing Modules
import pygame as pg
from pygame.math import Vector2

from modules_MS import config as c
from modules_MS import m_MS_boot  # Boot Menu
from modules_MS import m_MS_audio_sys as a  # Audio System
from modules_MS import m_MS_extra_modules  # Extra Tools
from modules_MS import m_MS_game  # Game Screen
from modules_MS import m_MS_main_menu  # Main Menu
from modules_MS import m_MS_menu_fades  # Menu Fade Function
from modules_MS import m_MS_options  # Options Menu
from modules_MS.colours import *
from modules_MS.m_MS_HTP import how_to_play  # How to Play
from modules_MS.m_MS_credits import game_credits  # Game Credits
from modules_MS.m_MS_end import end  # End Screen
from modules_MS.m_MS_mode import mode  # Choose Mode
from modules_MS.m_MS_quit import quit_game  # Quit Game

# Initialization
pg.init()

# Surface & Window
surface = pg.display.set_mode((c.width, c.height), flags=pg.HWSURFACE and pg.DOUBLEBUF)  # Main Screen
pg.display.set_caption("Modern Snek")  # Sets Caption Text
snek_img = pg.image.load(os.getcwd() + "/resources_MS/logo.png").convert_alpha()  # Importing Caption Icon
pg.display.set_icon(snek_img)  # Sets Caption Icon

# Clocks
clock = pg.time.Clock()
FPS = 165

# Global VariablesBigNoodleTitling
running = True  # Runs The Game Loop
small_font = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 25)  # FPS Counter Font
last_time = time.time()  # Used for Delta Time (Framerate Independence)

# ------------------------------------------- Main Program Loop --------------------------------------------------------
while running:
    global trans_alpha
    # ------------------------------------------------------------------------------------------------------------------
    # Framerate Independence
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    # ------------------------------------------------------------------------------------------------------------------
    click = False  # Resets Click Variable
    # ------------------------------------------------------------------------------------------------------------------
    for event in pg.event.get():  # User did something
        if event.type == pg.QUIT:  # If User Clicked Close
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:  # When Mouse Button Clicked
            if event.button == 1:  # Left Mouse Button
                click = True
                c.mouse_down = True
        if event.type == pg.MOUSEBUTTONUP:  # Reset Mouse Down value when button is released
            if event.button == 1:  # Left Mouse Button
                c.mouse_down = False
        if c.state == 7 and not c.pause:  # These conditions only work during the game
            # Snek Speeds
            if c.speed_increase_e:  # Only Change Speed When Setting is Enable
                if m_MS_game.speed_level == 0:
                    if event.type == c.SCREEN_UPDATE_0:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 1:
                    if event.type == c.SCREEN_UPDATE_1:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 2:
                    if event.type == c.SCREEN_UPDATE_2:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 3:
                    if event.type == c.SCREEN_UPDATE_3:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 4:
                    if event.type == c.SCREEN_UPDATE_4:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 5:
                    if event.type == c.SCREEN_UPDATE_5:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 6:
                    if event.type == c.SCREEN_UPDATE_6:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 7:
                    if event.type == c.SCREEN_UPDATE_7:
                        m_MS_game.move_snek()
                elif m_MS_game.speed_level == 8:
                    if event.type == c.SCREEN_UPDATE_8:
                        m_MS_game.move_snek()
            else:
                if event.type == c.SCREEN_UPDATE_0:
                    m_MS_game.move_snek()
            if event.type == pg.KEYDOWN:  # Includes WASD/Arrow Key Mods
                # Pause Menu
                if event.key == pg.K_ESCAPE:
                    c.pause = True
                    c.channel3.play(a.m_click)  # Click Sound
                # Snek Movement
                if event.key == pg.K_w and c.WASD_e or not c.WASD_e and event.key == pg.K_UP:
                    if m_MS_game.snek_direction.y != 1:  # Prevents going backwards
                        m_MS_game.snek_direction = Vector2(0, -1)
                        if m_MS_game.snek_current_direction != "UP":  # Don't repeat sfx when in same direction
                            if not c.m_daniel_e:
                                c.channel4.play(a.move_up)  # Normal Sound
                            else:
                                c.channel4.play(a.daniel_up)  # Daniel Sound (If enabled)
                        m_MS_game.snek_current_direction = "UP"
                elif event.key == pg.K_s and c.WASD_e or not c.WASD_e and event.key == pg.K_DOWN:
                    if m_MS_game.snek_direction.y != -1:  # Prevents going backwards
                        m_MS_game.snek_direction = Vector2(0, 1)
                        if m_MS_game.snek_current_direction != "DOWN":  # Don't repeat sfx when in same direction
                            if not c.m_daniel_e:
                                c.channel4.play(a.move_down)  # Normal Sound
                            else:
                                c.channel4.play(a.daniel_down)  # Daniel Sound (If enabled)
                        m_MS_game.snek_current_direction = "DOWN"
                elif event.key == pg.K_a and c.WASD_e or not c.WASD_e and event.key == pg.K_LEFT:
                    if m_MS_game.snek_direction.x != 1:
                        m_MS_game.snek_direction = Vector2(-1, 0)
                        if m_MS_game.snek_current_direction != "LEFT":  # Don't repeat sfx when in same direction
                            if not c.m_daniel_e:
                                c.channel5.play(a.move_left)  # Normal Sound
                            else:
                                c.channel5.play(a.daniel_left)  # Daniel Sound (If enabled)
                        m_MS_game.snek_current_direction = "LEFT"
                elif event.key == pg.K_d and c.WASD_e or not c.WASD_e and event.key == pg.K_RIGHT:
                    if m_MS_game.snek_direction.x != -1:  # Prevents going backwards
                        m_MS_game.snek_direction = Vector2(1, 0)
                        if m_MS_game.snek_current_direction != "RIGHT":  # Don't repeat sfx when in same direction
                            if not c.m_daniel_e:
                                c.channel5.play(a.move_right)  # Normal Sound
                            else:
                                c.channel5.play(a.daniel_right)  # Daniel Sound (If enabled)
                        m_MS_game.snek_current_direction = "RIGHT"
            if event.type == c.stopwatch_count:  # Event that happens every 10 milliseconds
                m_MS_game.stopwatch()  # Count Seconds
    # Bug: If you head one direction, press another direction that's not opposite, it resets the current direction,
    # and allows the snek to go back into itself
    # ------------------------------------------------------------------------------------------------------------------
    # Main Function Programs
    if c.state == 0:  # Bootup
        m_MS_boot.boot(surface, clock)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 1:  # Main Menu
        m_MS_main_menu.main_menu(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 2:  # Choose Mode
        mode(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 3:  # Options
        m_MS_options.options(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 4:  # How to Play
        how_to_play(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 5:  # Credits
        game_credits(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 6:  # Quit Game
        quit_game(surface, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 7:  # Play Game
        m_MS_game.main_snek(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    elif c.state == 8:  # End Screen
        end(surface, click, clock, FPS, dt)
    # ------------------------------------------------------------------------------------------------------------------
    if m_MS_menu_fades.trans_alpha != 0:  # Don't render fade surface when not fading (Saves 10FPS)
        surface.blit(m_MS_menu_fades.transition, (0, 0))
    # ------------------------------------------------------------------------------------------------------------------
    m_MS_extra_modules.display_fps(m_MS_options.show_fps, surface, clock, small_font, white)  # Display FPS Function
    # ------------------------------------------------------------------------------------------------------------------
    a.audio_mixer()  # Audio System That Manages All Sound
    # ------------------------------------------------------------------------------------------------------------------
    pg.display.update()  # Update Screen
    # ------------------------------------------------------------------------------------------------------------------
    # Boot Screen Runs 165FPS Default - Switch To User FPS When In Menu
    if c.state != 0:
        FPS = m_MS_options.fps_new
        clock.tick(FPS)
    # ------------------------------------------------------------------------------------------------------------------
    # Debugging Prints
    # print(f"FPS: {int(clock.get_fps())} | State: {c.state} | "
    #       f"Click: {click} | Fade Opacity: {m_MS_menu_fades.trans_alpha}")
