# Daniel Zhuo
# Modern Snek Module - Loads Snek Body Elements

import os

import pygame as pg

# Images
# Snek
snek = pg.image.load(os.getcwd() + "/resources_MS/snek.png").convert_alpha()
snek_rect = snek.get_rect(topleft=(1190, 400))
# Minecraft Easter Egg
snek_options = pg.transform.smoothscale(snek, (206, 300)).convert_alpha()
snek_options_rect = snek.get_rect(center=(1225, 825))
jukebox = pg.image.load(os.getcwd() + "/resources_MS/jukebox.png").convert_alpha()
jukebox_rect = snek.get_rect(topleft=(900, 750))
snek_box = False
# Game Fruits
fruit_0 = pg.image.load(os.getcwd() + "/resources_MS/fruit_0.png").convert_alpha()
fruit_1 = pg.image.load(os.getcwd() + "/resources_MS/fruit_1.png").convert_alpha()
fruit_2 = pg.image.load(os.getcwd() + "/resources_MS/fruit_2.png").convert_alpha()
fruit_3 = pg.image.load(os.getcwd() + "/resources_MS/fruit_3.png").convert_alpha()
fruit = pg.image.load(os.getcwd() + "/resources_MS/fruit_0.png")  # Selected Game Fruit
# Highscore & End Screen
trophy = pg.image.load(os.getcwd() + "/resources_MS/trophy.png").convert_alpha()
trophy_rect_end = trophy.get_rect(center=(450, 500))  # Used to center image on coordinate
# Game Edition Logos
base_logo = pg.image.load(os.getcwd() + "/resources_MS/ms_base_logo.png")
daniel_logo = pg.image.load(os.getcwd() + "/resources_MS/ms_daniel_logo.png")
soviet_logo = pg.image.load(os.getcwd() + "/resources_MS/ms_soviet_logo.png")
covid_logo = pg.image.load(os.getcwd() + "/resources_MS/ms_covid_logo.png")
logo_rect_mode = base_logo.get_rect(center=(1150, 470))  # Used to center image on coordinate
# HUD Logos - Resize Originals
base_hud = pg.transform.smoothscale(base_logo, (267, 102)).convert_alpha()
daniel_hud = pg.transform.smoothscale(daniel_logo, (267, 102)).convert_alpha()
soviet_hud = pg.transform.smoothscale(soviet_logo, (267, 102)).convert_alpha()
covid_hud = pg.transform.smoothscale(covid_logo, (267, 102)).convert_alpha()
logo_rect_hud = base_hud.get_rect(center=(200, 125))  # Used to center image on coordinate
# HUD Fruits - Resize Originals
fruit_0_hud = pg.transform.smoothscale(fruit_0, (75, 75)).convert_alpha()
fruit_1_hud = pg.transform.smoothscale(fruit_1, (75, 75)).convert_alpha()
fruit_2_hud = pg.transform.smoothscale(fruit_2, (75, 75)).convert_alpha()
fruit_3_hud = pg.transform.smoothscale(fruit_3, (75, 75)).convert_alpha()
score_rect = fruit_0_hud.get_rect(center=(145, 252))  # Used to center image on coordinate
# Game HUD - Resize Originals
trophy_hud = pg.transform.smoothscale(trophy, (58, 67)).convert_alpha()
trophy_rect_hud = fruit_0_hud.get_rect(center=(153, 353))  # Used to center image on coordinate
# End Screen
fruit_0_end = pg.transform.smoothscale(fruit_0, (113, 113)).convert_alpha()
fruit_1_end = pg.transform.smoothscale(fruit_1, (113, 113)).convert_alpha()
fruit_2_end = pg.transform.smoothscale(fruit_2, (113, 113)).convert_alpha()
fruit_3_end = pg.transform.smoothscale(fruit_3, (113, 113)).convert_alpha()
apple_rect = fruit_0_end.get_rect(center=(150, 500))

# Snek Design
# Base Edition
head_up_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/head_up.png")
head_down_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/head_down.png")
head_right_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/head_right.png")
head_left_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/head_left.png")
tail_up_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/tail_up.png")
tail_down_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/tail_down.png")
tail_right_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/tail_right.png")
tail_left_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/tail_left.png")
body_vertical_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/body_vertical.png")
body_horizontal_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/body_horizontal.png")
body_tr_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/body_tr.png")
body_tl_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/body_tl.png")
body_br_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/body_br.png")
body_bl_base = pg.image.load(os.getcwd() + "/resources_MS/snek_design_0/body_bl.png")

# Daniel Edition
head_up_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/head_up.png")
head_down_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/head_down.png")
head_right_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/head_right.png")
head_left_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/head_left.png")
tail_up_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/tail_up.png")
tail_down_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/tail_down.png")
tail_right_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/tail_right.png")
tail_left_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/tail_left.png")
body_vertical_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/body_vertical.png")
body_horizontal_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/body_horizontal.png")
body_tr_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/body_tr.png")
body_tl_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/body_tl.png")
body_br_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/body_br.png")
body_bl_daniel = pg.image.load(os.getcwd() + "/resources_MS/snek_design_1/body_bl.png")

# Soviet Edition
head_up_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/head_up.png")
head_down_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/head_down.png")
head_right_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/head_right.png")
head_left_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/head_left.png")
tail_up_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/tail_up.png")
tail_down_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/tail_down.png")
tail_right_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/tail_right.png")
tail_left_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/tail_left.png")
body_vertical_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/body_vertical.png")
body_horizontal_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/body_horizontal.png")
body_tr_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/body_tr.png")
body_tl_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/body_tl.png")
body_br_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/body_br.png")
body_bl_soviet = pg.image.load(os.getcwd() + "/resources_MS/snek_design_2/body_bl.png")

# COVID Edition
head_up_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/head_up.png")
head_down_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/head_down.png")
head_right_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/head_right.png")
head_left_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/head_left.png")
tail_up_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/tail_up.png")
tail_down_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/tail_down.png")
tail_right_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/tail_right.png")
tail_left_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/tail_left.png")
body_vertical_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/body_vertical.png")
body_horizontal_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/body_horizontal.png")
body_tr_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/body_tr.png")
body_tl_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/body_tl.png")
body_br_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/body_br.png")
body_bl_covid = pg.image.load(os.getcwd() + "/resources_MS/snek_design_3/body_bl.png")

# Global Body Part Variables
head_up = head_up_base
head_down = head_down_base
head_right = head_right_base
head_left = head_left_base
tail_up = tail_up_base
tail_down = tail_down_base
tail_right = tail_right_base
tail_left = tail_left_base
body_vertical = body_vertical_base
body_horizontal = body_horizontal_base
body_tr = body_tr_base
body_tl = body_tl_base
body_br = body_br_base
body_bl = body_bl_base

# Snek Head Used For Direction
snek_head = head_right
snek_tail = tail_left
