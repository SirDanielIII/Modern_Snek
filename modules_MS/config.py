# Daniel Zhuo
# Modern Snek Module - Config
# Stores Global Variables Shared By Other Modules

import pygame as pg

# Window Size
width, height = 1600, 900

# Time/Duration
seconds = 0
started_timer = False
activate_timer = False
# Fruit Timer
fruit_sec = 0  # 20 Seconds
fruit_time_cap = 20.00
fruit_time = fruit_time_cap  # 20 Seconds

# State
state = 0  # Controls Different Menus
return_state = 1  # Defaults to 1, 7 goes back to game

# Standard Grid Size
square_grid = 50

# Surface Flags
surface_flags = flags = pg.HWSURFACE and pg.SRCALPHA and pg.DOUBLEBUF

# Colours
ms_red = pg.Color("#e84a23")
ms_blue = pg.Color("#486ce4")
ms_green = pg.Color("#8bcc55")
ms_yellow = pg.Color("#fdc328")
ms_grey1 = pg.Color("#b1b1b1")
ms_grey2 = pg.Color("#9c9c9c")
# Grid Colours
# Base
ms_game_dark_green = pg.Color("#487631")
ms_g_dark_green = pg.Color("#8bce46")
ms_g_light_green = pg.Color("#a5db53")
# Daniel
ms_g_dark_red = pg.Color("#ffbaba")
ms_g_light_red = pg.Color("#FF7C7C")
ms_g_red_fill = pg.Color("#b71c1c")
# Soviet
ms_g_soviet_red = pg.Color("#CE0A06")
ms_g_soviet_yellow = pg.Color("#FFDB2D")
ms_g_soviet_fill = pg.Color("#6B1104")
# COVID
ms_g_covid_light = pg.Color("#AFA793")
ms_g_covid_dark = pg.Color("#948A76")
ms_g_covid_fill = pg.Color("#4A4235")
# Sets Default Colours
grid_light = ms_g_light_green
grid_dark = ms_g_dark_green

# Mode Menu
cell_size = 50
# Game Modes
m_base_e = True
m_daniel_e = False
m_soviet_e = False
m_covid_e = False

# Options Menu
# Game Settings
speed_increase_e = True
fruit_timer_e = True
WASD_e = True
# Music
sfx_e = True
music_e = True

# Grid Surface Coordinates
play_s_x = 1200
play_s_y = 800
# Generate Grid Squares
cell_numberX = play_s_x // cell_size
cell_numberY = play_s_y // cell_size

# Pause Menu
pause = False

# Held Mouse Button
mouse_down = False
just_released = False

# Running
dead = False
started_game = False
death_note = "WHATTA BOOT"

# Pre-generation Values
pos_x = cell_numberY // 2  # Middle X Value of Screen
pos_y = cell_numberY // 2  # Middle Y Value of Screen

# Scoring
score = 0
highscore = [0, 0]  # First index stores highscore, second index stores score

# User Events
# Different Snek Speeds
SCREEN_UPDATE_0 = pg.USEREVENT + 0
pg.time.set_timer(SCREEN_UPDATE_0, 100)

SCREEN_UPDATE_1 = pg.USEREVENT + 1
pg.time.set_timer(SCREEN_UPDATE_1, 90)

SCREEN_UPDATE_2 = pg.USEREVENT + 2
pg.time.set_timer(SCREEN_UPDATE_2, 80)

SCREEN_UPDATE_3 = pg.USEREVENT + 3
pg.time.set_timer(SCREEN_UPDATE_3, 70)

SCREEN_UPDATE_4 = pg.USEREVENT + 4
pg.time.set_timer(SCREEN_UPDATE_4, 60)

SCREEN_UPDATE_5 = pg.USEREVENT + 5
pg.time.set_timer(SCREEN_UPDATE_5, 50)

SCREEN_UPDATE_6 = pg.USEREVENT + 6
pg.time.set_timer(SCREEN_UPDATE_6, 40)

SCREEN_UPDATE_7 = pg.USEREVENT + 7
pg.time.set_timer(SCREEN_UPDATE_7, 30)

SCREEN_UPDATE_8 = pg.USEREVENT + 8
pg.time.set_timer(SCREEN_UPDATE_8, 20)

# Stopwatch Timer
stopwatch_count = pg.USEREVENT + 9
pg.time.set_timer(stopwatch_count, 10)  # Calculate Milliseconds

# Music Channels
pg.mixer.init()
channel0 = pg.mixer.Channel(0)  # Music
channel1 = pg.mixer.Channel(1)  # Music
channel2 = pg.mixer.Channel(2)  # Music
channel3 = pg.mixer.Channel(3)  # SFX
channel4 = pg.mixer.Channel(4)  # SFX
channel5 = pg.mixer.Channel(5)  # SFX
# Booleans To Change Songs
change_song = True
main_menu_song = True
pick_mode_song = False
game_song = False
death_song = False
rick_roll = False
rick_rolled = False
