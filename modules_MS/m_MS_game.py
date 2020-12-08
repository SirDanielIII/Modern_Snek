# Daniel Zhuo
# Modern Snek Module - Game Screen
# State 7

import math
import random

import pygame as pg
from pygame.math import Vector2

from . import config as c
from . import m_MS_audio_sys as a
from . import m_MS_extra_modules
from . import m_MS_menu_fades
from . import m_MS_snek_assets as SA
from .colours import *

# Main Surface
game_screen = pg.display.set_mode((c.width, c.height), c.surface_flags)
# Overlays
# Blit Low Opacity Images Into Background - Themes
game_background = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
play_screen = pg.Surface((c.play_s_x, c.play_s_y), c.surface_flags)
# Grid Generation
# Grid Surface
grid_surface = pg.Surface((c.play_s_x, c.play_s_y), c.surface_flags)
# HUD
# Top and Bottom Overlay
hud_overlay = pg.Surface((c.width, c.height), flags=pg.HWSURFACE and pg.SRCALPHA).convert_alpha()
hud_overlay.set_alpha(77)  # 30% Opacity
# Background Overlay
hud_background = pg.Surface((c.width, c.height), flags=pg.HWSURFACE and pg.SRCALPHA).convert_alpha()
hud_background.set_alpha(77)  # 30% Opacity
# Creating Transparency With Surfaces
hud_background.fill((0, 0, 0, 0))
hud_overlay.fill((0, 0, 0, 0))
# Background Overlays
pg.draw.rect(hud_overlay, black, (50, 50, 300, 150))  # Top Rectangle
pg.draw.rect(hud_background, black, (50, 50, 300, 800))  # Middle Overlay
pg.draw.rect(hud_overlay, black, (50, 700, 300, 150))  # Bottom Rectangle
# Blit Surfaces
hud = pg.Surface((c.width, c.height), flags=pg.HWSURFACE and pg.SRCALPHA).convert_alpha()
hud.blit(hud_background, (0, 0))
hud.blit(hud_overlay, (0, 0))
# Pause Menu
# Pause Menu Surface
pause_menu = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
# Background Overlay
pause_background = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
pause_background.fill(black)
pause_background.set_alpha(153)  # 60% Opacity
# Pre-Blit Background Overlay For Performance
pause_overlay = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
# Pause Menu Fading Control
pause_fade = 0
resume = False

# Fruit Properties
fruit_x = c.cell_numberX // 2  # Spawns apple on the screen
fruit_y = c.cell_numberY // 2  # Spawns apple on the screen
fruit_pos = Vector2(fruit_x, fruit_y)  # Creates vector of the apple; efficient way to store 2D data

# Snek Properties
# Calculate Middle Y From Start Button
snek_body = [Vector2(4, c.pos_y), Vector2(3, c.pos_y), Vector2(2, c.pos_y)]
snek_direction = Vector2(0, 0)  # Sets No Initial Direction
snek_current_direction = "NONE"
new_block = False  # To Add A New Block Or Not To

# Global Variables
go_back = False  # Menu Fading
pause_c = white  # Pause Button Highlight
return_screen = None
transition = False
speed_level = 0
speed_text = "Normal"
output_string = "00:00"
fruit_time_c = green
wait = False
start_ticks = pg.time.get_ticks()  # Used to Pause Fruit Timer For 1 Second
fruit_pause = 0

# Fonts
pause_title = pg.font.SysFont("BigNoodleTitling", 150)
game_enable_t = pg.font.SysFont("BigNoodleTitling", 100)
game_timer_t = pg.font.SysFont("BigNoodleTitling", 75)
pause_text = pg.font.SysFont("BigNoodleTitling", 65)
game_sub_t = pg.font.SysFont("BigNoodleTitling", 25)

# Pause Menu Colours
resume_c = white
options_c = white
htp_c = white
quit_c = white


# ----------------------------------------------------------------------------------------------------------------------
def game_load():
    """
    This functions loads and calculates a lot of variables that are needed for the game.
    E.G. Settings, Block Sizes, Grid-Generation, etc).
    The function also acts as a game reset
    """
    # ------------------------------------------------------------------------------------------------------------------
    global snek_body, fruit_pos, go_back, transition, return_screen, \
        snek_direction, snek_current_direction, pause_fade
    # ------------------------------------------------------------------------------------------------------------------
    # Resize Image Assets
    if c.m_base_e:
        # Fruit
        SA.fruit = pg.transform.smoothscale(SA.fruit_0, (c.cell_size, c.cell_size)).convert_alpha()
        # Snek
        SA.head_up = pg.transform.smoothscale(SA.head_up_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_down = pg.transform.smoothscale(SA.head_down_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_right = pg.transform.smoothscale(SA.head_right_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_left = pg.transform.smoothscale(SA.head_left_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_up = pg.transform.smoothscale(SA.tail_up_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_down = pg.transform.smoothscale(SA.tail_down_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_right = pg.transform.smoothscale(SA.tail_right_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_left = pg.transform.smoothscale(SA.tail_left_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_vertical = pg.transform.smoothscale(SA.body_vertical_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_horizontal = pg.transform.smoothscale(
            SA.body_horizontal_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tr = pg.transform.smoothscale(SA.body_tr_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tl = pg.transform.smoothscale(SA.body_tl_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_br = pg.transform.smoothscale(SA.body_br_base, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_bl = pg.transform.smoothscale(SA.body_bl_base, (c.cell_size, c.cell_size)).convert_alpha()
    elif c.m_daniel_e:
        SA.fruit = pg.transform.smoothscale(SA.fruit_1, (c.cell_size, c.cell_size)).convert_alpha()
        # Snek
        SA.head_up = pg.transform.smoothscale(SA.head_up_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_down = pg.transform.smoothscale(SA.head_down_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_right = pg.transform.smoothscale(SA.head_right_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_left = pg.transform.smoothscale(SA.head_left_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_up = pg.transform.smoothscale(SA.tail_up_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_down = pg.transform.smoothscale(SA.tail_down_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_right = pg.transform.smoothscale(SA.tail_right_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_left = pg.transform.smoothscale(SA.tail_left_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_vertical = pg.transform.smoothscale(SA.body_vertical_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_horizontal = pg.transform.smoothscale(
            SA.body_horizontal_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tr = pg.transform.smoothscale(SA.body_tr_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tl = pg.transform.smoothscale(SA.body_tl_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_br = pg.transform.smoothscale(SA.body_br_daniel, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_bl = pg.transform.smoothscale(SA.body_bl_daniel, (c.cell_size, c.cell_size)).convert_alpha()
    elif c.m_soviet_e:
        # Fruit
        SA.fruit = pg.transform.smoothscale(SA.fruit_2, (c.cell_size, c.cell_size)).convert_alpha()
        # Snek
        SA.head_up = pg.transform.smoothscale(SA.head_up_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_down = pg.transform.smoothscale(SA.head_down_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_right = pg.transform.smoothscale(SA.head_right_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_left = pg.transform.smoothscale(SA.head_left_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_up = pg.transform.smoothscale(SA.tail_up_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_down = pg.transform.smoothscale(SA.tail_down_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_right = pg.transform.smoothscale(SA.tail_right_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_left = pg.transform.smoothscale(SA.tail_left_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_vertical = pg.transform.smoothscale(SA.body_vertical_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_horizontal = pg.transform.smoothscale(
            SA.body_horizontal_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tr = pg.transform.smoothscale(SA.body_tr_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tl = pg.transform.smoothscale(SA.body_tl_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_br = pg.transform.smoothscale(SA.body_br_soviet, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_bl = pg.transform.smoothscale(SA.body_bl_soviet, (c.cell_size, c.cell_size)).convert_alpha()
    elif c.m_covid_e:
        # Fruit
        SA.fruit = pg.transform.smoothscale(SA.fruit_3, (c.cell_size, c.cell_size)).convert_alpha()
        # Snek
        SA.head_up = pg.transform.smoothscale(SA.head_up_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_down = pg.transform.smoothscale(SA.head_down_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_right = pg.transform.smoothscale(SA.head_right_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.head_left = pg.transform.smoothscale(SA.head_left_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_up = pg.transform.smoothscale(SA.tail_up_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_down = pg.transform.smoothscale(SA.tail_down_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_right = pg.transform.smoothscale(SA.tail_right_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.tail_left = pg.transform.smoothscale(SA.tail_left_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_vertical = pg.transform.smoothscale(SA.body_vertical_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_horizontal = pg.transform.smoothscale(
            SA.body_horizontal_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tr = pg.transform.smoothscale(SA.body_tr_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_tl = pg.transform.smoothscale(SA.body_tl_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_br = pg.transform.smoothscale(SA.body_br_covid, (c.cell_size, c.cell_size)).convert_alpha()
        SA.body_bl = pg.transform.smoothscale(SA.body_bl_covid, (c.cell_size, c.cell_size)).convert_alpha()
    # ------------------------------------------------------------------------------------------------------------------
    # Calculate Grid Squares
    c.cell_numberX = c.play_s_x // c.cell_size  # Game Breaks On This Calculation
    c.cell_numberY = c.play_s_y // c.cell_size
    # ------------------------------------------------------------------------------------------------------------------
    # Reset Dead Status
    c.dead = False
    # ------------------------------------------------------------------------------------------------------------------
    # Calculate Middle of Grid
    c.pos_x = c.cell_numberX // 2
    c.pos_y = c.cell_numberY // 2
    # ------------------------------------------------------------------------------------------------------------------
    # Pre-generate Snek Spawn - Centered
    snek_body = [Vector2(4, c.pos_y), Vector2(3, c.pos_y), Vector2(2, c.pos_y)]
    # Pre-generate Apple Spawn - Centered
    fruit_pos = Vector2(c.pos_x, c.pos_y)
    # ------------------------------------------------------------------------------------------------------------------
    # Reset Values
    c.pause = False
    go_back = False
    transition = False
    return_screen = 0
    snek_direction = Vector2(0, 0)  # Sets No Initial Direction
    snek_current_direction = "NONE"  # Sets No Initial Direction
    pause_fade = 0  # Resets Pause Menu Fade
    c.score = 0  # Set Score to 0
    # ------------------------------------------------------------------------------------------------------------------
    # Sets Timer Caps
    if c.cell_size == 50:
        c.fruit_time_cap = 20.00
    elif c.cell_size == 80:
        c.fruit_time_cap = 10.00
    elif c.cell_size == 25:
        c.fruit_time_cap = 30.00
    elif c.cell_size == 5:
        c.fruit_time_cap = 50.00
    c.fruit_time = c.fruit_time_cap  # Reset Fruit Timer To Designated Cap
    # ------------------------------------------------------------------------------------------------------------------
    time_reset()  # Reset Stopwatch
    # ------------------------------------------------------------------------------------------------------------------
    # Grid Colours
    if c.m_base_e:
        c.grid_light = c.ms_g_light_green
        c.grid_dark = c.ms_g_dark_green
    if c.m_daniel_e:
        c.grid_light = c.ms_g_dark_red
        c.grid_dark = c.ms_g_light_red
    if c.m_soviet_e:
        c.grid_light = c.ms_g_soviet_yellow
        c.grid_dark = c.ms_g_soviet_red
    if c.m_covid_e:
        c.grid_light = c.ms_g_covid_light
        c.grid_dark = c.ms_g_covid_dark
    # ------------------------------------------------------------------------------------------------------------------
    draw_grid(grid_surface)  # Pre-generates grid to save huge amounts of performance
    # ------------------------------------------------------------------------------------------------------------------
    if not c.rick_rolled:
        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
        a.dj(False, False, True, False, c.channel1, 500, True, c.channel3, a.m_click)  # Audio Handler
    else:
        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
        a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.m_click)  # Audio Handler


# ----------------------------------------------------------------------------------------------------------------------
def draw_grid(screen):
    """This function generates the game grid
    Args:
        screen::surface
            Specifies screen to blit grid
    Notes:
        To save tons of FPS, blit the generated grid to a surface before the game loop, and
        blit that surface to the main surface during the loop.
    """
    for row in range(c.width // c.cell_size):  # 800 Height
        for col in range((c.height // c.cell_size) * 2):  # 1,200 Width
            if (row + col) % 2 == 0:
                rect_x = pg.Rect(col * c.cell_size, row * c.cell_size, c.cell_size, c.cell_size)
                pg.draw.rect(screen, c.grid_light, rect_x)
            else:
                rect_y = pg.Rect(col * c.cell_size, row * c.cell_size, c.cell_size, c.cell_size)
                pg.draw.rect(screen, c.grid_dark, rect_y)


# ----------------------------------------------------------------------------------------------------------------------
def draw_fruit(screen):
    """This function draws the game fruit
    Args:
        screen::surface
            Specifies screen to draw fruit
    """
    fruit_rect = pg.Rect(fruit_pos.x * c.cell_size, fruit_pos.y * c.cell_size, c.cell_size, c.cell_size)
    # pg.draw.rect(screen, red, fruit_rect) # Reference Square
    screen.blit(SA.fruit, fruit_rect)
    return fruit_rect


# ----------------------------------------------------------------------------------------------------------------------
def randomize_fruit():
    """This function calculates the random grid generation of the fruit"""
    global fruit_x, fruit_y, fruit_pos
    fruit_x = random.randint(0, c.cell_numberX - 1)  # Spawns apple on the screen
    fruit_y = random.randint(0, c.cell_numberY - 1)  # Spawns apple on the screen
    # If Apple Spawns Inside Snek
    for block in snek_body:
        if fruit_x == block.x and fruit_y == block.y:
            fruit_x = random.randint(0, c.cell_numberX - 1)  # Regen Apple X
            fruit_y = random.randint(0, c.cell_numberY - 1)  # Regen Apple Y

    fruit_pos = Vector2(fruit_x, fruit_y)  # Creates vector of the apple; efficient way to store 2D data


# ----------------------------------------------------------------------------------------------------------------------
def fruit_timer():
    """This function specifies snek speed, dependant on the score - faster every 5 fruits"""
    global speed_text, speed_level
    if c.score == 0:
        speed_level = 0
        speed_text = "Normal"
    elif c.score == 5:
        speed_level = 1
        speed_text = "Normal+"
    elif c.score == 10:
        speed_level = 2
        speed_text = "Fast"
    elif c.score == 15:
        speed_level = 3
        speed_text = "Faster"
    elif c.score == 20:
        speed_level = 4
        speed_text = "Faster+"
    elif c.score == 25:
        speed_level = 5
        speed_text = "Pro"
    elif c.score == 30:
        speed_level = 6
        speed_text = "Pro Max"
    elif c.score == 35:
        speed_level = 7
        speed_text = "iPhone"
    elif c.score == 40:
        speed_level = 8
        speed_text = "JEEZ, DIE!"


def update_head_graphics():
    """This function updates the snek head graphics"""
    head_relation = snek_body[1] - snek_body[0]  # Calculates Direction Using Position of Head and Body
    if head_relation == Vector2(1, 0):  # Facing Left
        SA.snek_head = SA.head_left
    elif head_relation == Vector2(-1, 0):  # Facing Right
        SA.snek_head = SA.head_right
    elif head_relation == Vector2(0, 1):  # Facing Up
        SA.snek_head = SA.head_up
    elif head_relation == Vector2(0, -1):  # Facing Down
        SA.snek_head = SA.head_down


def update_tail_graphics():
    """This function updates the snek tail graphics"""
    tail_relation = snek_body[-2] - snek_body[-1]  # Calculates Direction Using Position of Tail and Piece Before Tail
    if tail_relation == Vector2(1, 0):  # Facing Left
        SA.snek_tail = SA.tail_left
    elif tail_relation == Vector2(-1, 0):  # Facing Right
        SA.snek_tail = SA.tail_right
    elif tail_relation == Vector2(0, 1):  # Facing Up
        SA.snek_tail = SA.tail_up
    elif tail_relation == Vector2(0, -1):  # Facing Down
        SA.snek_tail = SA.tail_down


# ----------------------------------------------------------------------------------------------------------------------
def draw_snek(screen):
    """This function draws the snek graphics
    Args:
        screen::surface
            Specifies screen to draw snek
    """
    update_head_graphics()
    update_tail_graphics()

    for idx, block in enumerate(snek_body):  # E.G. [1] = Vector2[X, Y]
        x_pos = block.x * c.cell_size
        y_pos = block.y * c.cell_size
        block_rect = pg.Rect(x_pos, y_pos, c.cell_size, c.cell_size)

        if idx == 0:  # Snek Head
            screen.blit(SA.snek_head, block_rect)  # Draws Head
        elif idx == len(snek_body) - 1:
            screen.blit(SA.snek_tail, block_rect)  # Draws Tail
        else:
            previous_block = snek_body[idx + 1] - block
            next_block = snek_body[idx - 1] - block
            if previous_block.x == next_block.x:  # If both body parts have same X - Vertical
                screen.blit(SA.body_vertical, block_rect)
            elif previous_block.y == next_block.y:
                screen.blit(SA.body_horizontal, block_rect)
            else:
                # Drawing Corners - Comparing Blocks
                if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    screen.blit(SA.body_tl, block_rect)  # Top Left Corner
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    screen.blit(SA.body_bl, block_rect)  # Bottom Left Corner
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    screen.blit(SA.body_tr, block_rect)  # Top Right Corner
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    screen.blit(SA.body_br, block_rect)  # Bottom Left Corner


# ----------------------------------------------------------------------------------------------------------------------
def move_snek():
    """This function moves the snek"""
    global snek_body, new_block, snek_direction
    # Snake Directions Are Given From The Main Loop
    if snek_current_direction != "NONE":
        if new_block:
            snek_body_copy = snek_body[:]  # Don't delete anything
            snek_body_copy.insert(0, snek_body_copy[0] + snek_direction)  # Inserts head at beginning of list
            snek_body = snek_body_copy[:]
            new_block = False
        else:
            snek_body_copy = snek_body[:-1]  # Gives first two elements
            snek_body_copy.insert(0, snek_body_copy[0] + snek_direction)  # Inserts head at beginning of list
            snek_body = snek_body_copy[:]


# ----------------------------------------------------------------------------------------------------------------------
def add_block_snek():
    """Resets new_block value to allow the snek to expand if needed"""
    global new_block
    new_block = True


# ----------------------------------------------------------------------------------------------------------------------
def check_collision():
    """Checks fruit collision with snek"""
    global wait
    if fruit_pos == snek_body[0]:
        randomize_fruit()  # Change fruit position
        add_block_snek()
        c.score += 1
        if c.m_base_e:
            a.dj(False, False, False, False, c.channel3, 100, False, c.channel3, a.crunch_0)  # Crunch Sound
        elif c.m_daniel_e:
            a.dj(False, False, False, False, c.channel3, 100, False, c.channel3, a.crunch_1)  # Gulp Sound
        elif c.m_soviet_e:
            a.dj(False, False, False, False, c.channel3, 100, False, c.channel3, a.crunch_2)  # NEIN Sound
        elif c.m_covid_e:
            a.dj(False, False, False, False, c.channel3, 100, False, c.channel3, a.crunch_3)  # CORONAVIRUS Sound

        if c.fruit_timer_e:
            wait = True  # Activate boolean to disable timer for a short period of time
            c.fruit_sec = 0  # Reset fruit timer if enabled


# ----------------------------------------------------------------------------------------------------------------------
def highscore():
    """Calculates the current highscore of the game
    Notes:
        c.highscore is a global list, with Index[0] being the highscore, and Index[1] being the actual score.
        Index[1] is shown in the end screen to prevent the displayed score
        from changing to zero due to the load_game() function being called again
    """
    if c.score > c.highscore[0]:
        c.highscore[0] = c.score
    c.highscore[1] = c.score  # Store current score in highscore to display during end screen


# ----------------------------------------------------------------------------------------------------------------------
def check_fail_snek():
    """This function checks snek collisions"""
    # Border Check
    if not 0 <= snek_body[0].x <= c.cell_numberX - 1 or not 0 <= snek_body[0].y < c.cell_numberY:
        c.dead = True
        if not c.rick_rolled:
            if c.m_daniel_e:
                a.dj(False, False, False, True, c.channel2, 500, True, c.channel3, a.ow)  # Audio Handler
            else:
                a.dj(False, False, False, True, c.channel2, 500, True, c.channel3, a.smack)  # Audio Handler
            c.death_note = "Snek has run into the wall"
        else:
            if c.m_daniel_e:
                a.dj(False, False, False, True, c.channel2, 500, False, c.channel3, a.ow)  # Audio Handler
            else:
                a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.smack)  # Smack Sound
                c.death_note = "Snek has been rick rolled"

    # Snek Body Collision
    for block in snek_body[1:]:  # Loops through body parts, but not the head
        if block == snek_body[0]:
            c.dead = True
            if not c.rick_rolled:
                if c.m_daniel_e:
                    a.dj(False, False, False, True, c.channel2, 500, True, c.channel3, a.ow)  # Audio Handler
                else:
                    a.dj(False, False, False, True, c.channel2, 500, True, c.channel3, a.smack)  # Audio Handler
                c.death_note = "Snek has committed Not Alive"
            else:
                if c.m_daniel_e:
                    a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.ow)  # Smack Sound
                else:
                    a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.smack)  # Smack Sound
                c.death_note = "Snek has been rick rolled"


# ----------------------------------------------------------------------------------------------------------------------
def time_start():
    """Starts duration timer"""
    c.started_timer, c.activate_timer = True, True


# ----------------------------------------------------------------------------------------------------------------------
def time_stop():
    """Stops duration timer"""
    if c.activate_timer:
        c.activate_timer = False


# ----------------------------------------------------------------------------------------------------------------------
def time_reset():
    """Reset duration stopwatch to it's default values"""
    if c.activate_timer:
        c.activate_timer = False
    c.started_timer = False
    c.seconds = 0
    c.fruit_sec = 0
    c.fruit_time = 20


# ----------------------------------------------------------------------------------------------------------------------
def stopwatch():
    """Stopwatch that counts seconds"""
    if c.activate_timer:
        c.seconds += 0.01  # Calculates milliseconds
        if not wait:
            c.fruit_sec += 0.01  # Used to subtract from fruit time


# ----------------------------------------------------------------------------------------------------------------------
def display_stopwatch():
    """Calculates and displays the stopwatch values"""
    global output_string, fruit_time_c, start_ticks, fruit_pause, wait
    if not c.pause and snek_current_direction != "NONE":  # If paused or not moving
        time_start()  # Start timer
    else:
        time_stop()  # Stop timer
    # ------------------------------------------------------------------------------------------------------------------
    # Rounding the Seconds
    int_seconds = math.floor(c.seconds)

    # Divide by 60 to get total minutes
    minutes = int_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = int_seconds % 60

    # Use python string formatting to format duration in leading zeros
    output_string = "{0:02}:{1:02}".format(minutes, seconds)
    # ------------------------------------------------------------------------------------------------------------------
    # Fruit Timers
    if c.fruit_timer_e:  # If Enabled
        c.fruit_time = round(c.fruit_time_cap - (c.fruit_sec % 60), 1)  # Calculate Number for Timer
        if c.fruit_time < 0:  # When Fruit Timer Reaches Zero
            c.dead = True
            if not c.rick_rolled:
                if not c.m_daniel_e:
                    a.dj(False, False, False, True, c.channel2, 500, True, c.channel3, a.oof)  # Audio Handler
                else:
                    a.dj(False, False, False, True, c.channel2, 500, True, c.channel3, a.weh)  # Audio Handler
                c.death_note = "Snek has died of hunger, Snek sad"
            else:
                if not c.m_daniel_e:
                    a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.oof)  # Oof Sound
                else:
                    a.dj(False, False, False, False, c.channel3, 500, False, c.channel3, a.weh)  # Weh Sound
                c.death_note = "Snek has been rick rolled"

    if wait and fruit_pause < 0.1:  # 0.1 Second Delay - Keeps Timer at 20.0
        fruit_pause = (pg.time.get_ticks() - start_ticks) / 1000
    else:
        fruit_pause = (pg.time.get_ticks() - start_ticks) / 1000
        start_ticks = pg.time.get_ticks()
        wait = False  # Reset Wait Boolean To Enable Timer Again
    # ----------------------------------------------------------------------------------------------------------------------
    # Change Text Colours
    if c.fruit_time > c.fruit_time_cap / 2:
        fruit_time_c = c.ms_green
    elif c.fruit_time_cap / 2 >= c.fruit_time > c.fruit_time_cap / 4:
        fruit_time_c = c.ms_yellow
    elif c.fruit_time_cap / 4 >= c.fruit_time > 0:
        fruit_time_c = c.ms_red


# ----------------------------------------------------------------------------------------------------------------------
def display_hud(screen):
    """This function draws the Game HUD
    Args:
        screen::surface
            Specifies screen to draw HUD
    """
    # Base Edition
    if c.m_base_e:
        # Background Colour
        screen.fill(c.ms_game_dark_green)
        screen.blit(hud, (0, 0))
        # HUD Icons
        screen.blit(SA.base_hud, SA.logo_rect_hud)  # Draws the logo centered on one point
        screen.blit(SA.fruit_0_hud, SA.score_rect)  # Draws the fruit centered on one point
    # Daniel Edition
    elif c.m_daniel_e:
        # Background Colour
        screen.fill(c.ms_g_red_fill)
        screen.blit(hud, (0, 0))
        # HUD Icons
        screen.blit(SA.daniel_hud, SA.logo_rect_hud)  # Draws the logo centered on one point
        screen.blit(SA.fruit_1_hud, SA.score_rect)  # Draws the fruit centered on one point
    # Soviet Edition
    elif c.m_soviet_e:
        # Background Colour
        screen.fill(c.ms_g_soviet_fill)
        screen.blit(hud, (0, 0))
        # HUD Icons
        screen.blit(SA.soviet_hud, SA.logo_rect_hud)  # Draws the logo centered on one point
        screen.blit(SA.fruit_2_hud, SA.score_rect)  # Draws the fruit centered on one point
    # COVID Edition
    elif c.m_covid_e:
        # Background Colour
        screen.fill(c.ms_g_covid_fill)
        screen.blit(hud, (0, 0))
        # HUD Icons
        screen.blit(SA.covid_hud, SA.logo_rect_hud)  # Draws the logo centered on one point
        screen.blit(SA.fruit_3_hud, SA.score_rect)  # Draws the fruit centered on one point

    screen.blit(SA.trophy_hud, SA.trophy_rect_hud)  # Draws the trophy centered on one point
    # ------------------------------------------------------------------------------------------------------------------
    # Top Text
    m_MS_extra_modules.draw_text(str(c.score), white, game_timer_t, screen, 237.5, 250)  # Score
    m_MS_extra_modules.draw_text(str(c.highscore[0]), white, game_timer_t, screen, 237.5, 350)  # Highscore
    # ------------------------------------------------------------------------------------------------------------------
    # Middle Text
    m_MS_extra_modules.draw_text("Fruit Timer", white, game_sub_t, screen, 200, 437.5)  # Fruit Timer Header
    if c.fruit_timer_e:  # If Fruit Timer is enabled
        m_MS_extra_modules.draw_text(f"{abs(c.fruit_time):.1f}", fruit_time_c, game_enable_t,
                                     screen, 200, 500)  # Fruit Timer
    else:  # Fruit timer disabled
        m_MS_extra_modules.draw_text("DISABLED", c.ms_grey1, game_enable_t, screen, 200, 500)  # Fruit Timer
    # ------------------------------------------------------------------------------------------------------------------
    m_MS_extra_modules.draw_text("Snek Speed Increase", white, game_sub_t, screen, 200, 575)  # Speed Up Header
    if c.speed_increase_e:  # Snek speed increase is enabled
        m_MS_extra_modules.draw_text(speed_text, white, game_enable_t, screen, 200, 637.5)  # Speed Up Text
    else:  # Snek speed increase is disabled
        m_MS_extra_modules.draw_text("DISABLED", c.ms_grey1, game_enable_t, screen, 200, 637.5)  # Speed Up Text
    # ------------------------------------------------------------------------------------------------------------------
    # Bottom Text
    m_MS_extra_modules.draw_text("Time Elapsed", white, game_sub_t, screen, 137.5, 745)  # Time Elapsed Header
    m_MS_extra_modules.draw_text(output_string, white, game_timer_t, screen, 137.5, 787.5)  # Time Elapsed Header
    # ------------------------------------------------------------------------------------------------------------------
    display_stopwatch()
    # ------------------------------------------------------------------------------------------------------------------
    if c.rick_roll:
        c.rick_rolled = True  # Lets song play during the main menu


# ----------------------------------------------------------------------------------------------------------------------
def blit_game(screen):
    """This function draws the game screen
    Args:
        screen::surface
            Specifies screen to game screen
    """
    screen.blit(play_screen, (350, 50))
    screen.blit(game_screen, (0, 0))


# ----------------------------------------------------------------------------------------------------------------------
def main_snek(screen, click, clock, fps, dt):
    """Function to run Game menu
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
    global snek_direction, snek_current_direction, pause_c, pause_fade, \
        resume_c, options_c, htp_c, quit_c, resume, go_back, return_screen, transition
    mx, my = pg.mouse.get_pos()
    # ------------------------------------------------------------------------------------------------------------------
    if not c.dead:  # If Snake Isn't Dead
        play_screen.blit(grid_surface, (0, 0))  # Blit Pre-generated grid to save FPS
        display_hud(game_screen)
        draw_fruit(play_screen)
        draw_snek(play_screen)
        check_collision()
        fruit_timer()
        check_fail_snek()
        highscore()
        blit_game(screen)  # Blit Screens
        # --------------------------------------------------------------------------------------------------------------
        # Pause Button
        pause_button = pg.Rect(225, 725, 100, 100)
        pg.draw.rect(game_screen, c.ms_blue, pause_button)
        pause_button_s1 = pg.Rect(250, 744.75, 20, 62.5)  # Pause Left Rectangle
        pg.draw.rect(game_screen, pause_c, pause_button_s1)
        pause_button_s2 = pg.Rect(280, 744.75, 20, 62.5)  # Pause Right Rectangle
        pg.draw.rect(game_screen, pause_c, pause_button_s2)
        # --------------------------------------------------------------------------------------------------------------
        if pause_button.collidepoint((mx, my)):
            pause_c = c.ms_yellow
            if click:
                c.pause = True
                a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
        elif c.pause:  # Keep Pause Button Yellow When In Menu
            pause_c = c.ms_yellow
        else:
            pause_c = white
        # ---------------------------------------------------------------------------------------------------------------
        if c.pause:  # Pause Menu
            # Fading In
            if pause_fade < 300 and not resume:
                pause_fade += 25 * dt
            elif pause_fade >= 300 and not resume:  # Stops the fade from going infinitely
                pause_fade = 300
            # Fading Out
            if pause_fade > 0 and resume:
                pause_fade -= 25 * dt
            elif pause_fade < 0 and resume:  # Stops the fade from going infinitely
                pause_fade = 0
                c.pause = False
                resume = False
            # --------------------------------------------------------------------------------------------------------------
            # Background Overlay
            pause_menu.fill((0, 0, 0, 0))  # Create Pause Menu Transparency
            pause_menu.blit(pause_background, (0, 0))
            # Title
            title = pause_title.render("PAUSED", True, white)
            pause_menu.blit(title, (393, 365))
            # Buttons
            resume_button = pg.Rect(400, 550, 6 * c.square_grid, 2 * c.square_grid)
            htp_button = pg.Rect(400, 700, 6 * c.square_grid, 2 * c.square_grid)
            options_button = pg.Rect(750, 550, 6 * c.square_grid, 2 * c.square_grid)
            quit_button = pg.Rect(750, 700, 6 * c.square_grid, 2 * c.square_grid)
            # Drawing Buttons
            pg.draw.rect(pause_menu, c.ms_blue, resume_button)
            pg.draw.rect(pause_menu, c.ms_blue, htp_button)
            pg.draw.rect(pause_menu, c.ms_blue, options_button)
            pg.draw.rect(pause_menu, c.ms_blue, quit_button)
            # Drawing Text
            m_MS_extra_modules.draw_text("Resume", resume_c, pause_text, pause_menu, 550, 600)
            m_MS_extra_modules.draw_text("How to Play", htp_c, pause_text, pause_menu, 550, 750)
            m_MS_extra_modules.draw_text("Options", options_c, pause_text, pause_menu, 900, 600)
            m_MS_extra_modules.draw_text("Main Menu", quit_c, pause_text, pause_menu, 900, 750)
            # ----------------------------------------------------------------------------------------------------------
            # Resume Game
            if resume_button.collidepoint((mx, my)):
                resume_c = c.ms_yellow
                if click:
                    resume = True  # Resumes Game
                    a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
            else:
                resume_c = white

            # Options Menu
            if options_button.collidepoint((mx, my)):
                options_c = c.ms_yellow
                if click:
                    go_back = True
                    transition = True
                    return_screen = 3
                    c.return_state = 7  # Back button returns back to game
                    a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                    a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
            else:
                options_c = white

            # How to Play
            if htp_button.collidepoint((mx, my)):
                htp_c = c.ms_yellow
                if click:
                    go_back = True
                    transition = True
                    return_screen = 4
                    c.return_state = 7  # Back button returns back to game
                    a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                    a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
            else:
                htp_c = white

            # Back to Main Menu
            if quit_button.collidepoint((mx, my)):
                quit_c = c.ms_yellow
                if click:
                    go_back = True
                    transition = True
                    return_screen = 1
                    c.return_state = 1
                    if not c.rick_rolled:
                        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                        a.dj(True, False, False, False, c.channel2, 500, True, c.channel3, a.m_click)  # Audio Handler
                    else:
                        a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                        a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound

            else:
                quit_c = white
        # --------------------------------------------------------------------------------------------------------------
    else:
        go_back = True
        transition = True
        return_screen = 8
        c.return_state = 1
    # ------------------------------------------------------------------------------------------------------------------
    if c.pause:
        game_screen.blit(pause_menu, (0, 0))  # Blit Pause Menu to Screen When Activated
    # ------------------------------------------------------------------------------------------------------------------
    if go_back:  # Fading out to other menus
        m_MS_menu_fades.dissolve_out(dt, clock, fps)
        if m_MS_menu_fades.trans_alpha >= 300:
            go_back = False
            transition = False
            c.state = return_screen
    # ------------------------------------------------------------------------------------------------------------------
    # Fading In
    if not go_back:
        if m_MS_menu_fades.trans_alpha != 0:  # Renders overlay only when fading
            m_MS_menu_fades.dissolve_in(dt, clock, fps)  # Fade in screen
    # ------------------------------------------------------------------------------------------------------------------
    # Pause Menu Opacity
    pause_menu.set_alpha(pause_fade)
