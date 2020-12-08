# Daniel Zhuo
# Modern Snek Module - Boot Screen
# State 0
# Now mostly useless since the game takes a while to load up

import os

import pygame as pg
from pygame import gfxdraw

from . import config as c
from .colours import *

# Stopwatch
start_ticks = pg.time.get_ticks()

# Initialization
pg.init()
pg.mixer.init()

# Screen
width, height = 1600, 900
bootup = pg.display.set_mode((width, height), flags=pg.HWSURFACE and pg.SRCALPHA and pg.DOUBLEBUF)
# Set Up Fade Overlay
fade = pg.Surface((width, height), c.surface_flags)  # Fade Overlay + Alpha
fade.fill(black)

# Media
logo = pg.image.load(os.getcwd() + "/resources_MS/boot/boot_logo.png").convert_alpha()  # Load logo
boot_sound = pg.mixer.Sound(os.getcwd() + "/resources_MS/boot/boot_bootup.mp3")
boot_sound.set_volume(0.3)
boot_finished = pg.mixer.Sound(os.getcwd() + "/resources_MS/boot/boot_confirm.mp3")
boot_finished.set_volume(0.4)
pg.mixer.music.load(os.getcwd() + "/resources_MS/boot/boot_logo.mp3")
play = 0  # Used to specific music files to play (only calls them once)

# Global Variables
fade_alpha = 0
first_fade = False
second_fade = False
start_fade = False
load_confirm = False
fade_in = True
last_fade = False
rect_width = 0
loading = pg.font.SysFont("BigNoodleTitling", 75)
loading_render = loading.render("LOADING", True, white)


def loading_screen():  # Loading Bar Animation
    """Plays loading screen part of boot screen

    Notes:
        If the loading bar can't keep up with its designated markers (based off seconds),
        it will automatically jump to the end.
    """
    global rect_width, loading_render, play
    seconds = (pg.time.get_ticks() - start_ticks) / 1000  # Timer

    pg.draw.rect(bootup, white, (150, height - 200, rect_width, 50))  # Loading Bar
    gfxdraw.rectangle(bootup, (140, height - 210, width - 280, 70), white)  # Bar Outline

    if rect_width < 1300 and seconds < 3:  # Bug Fix - Timer doesn't count when dragging window; snaps to end
        if play == 0:  # Plays the sound effect once
            pg.mixer.Channel(0).play(boot_sound)
            play = 1  # Change value to avoid loop
        if seconds < 0.75:
            loading_render = loading.render("LOADING.", True, white)
            bootup.blit(loading_render, (140, 610))
            rect_width += 1.5
        elif seconds < 1.25:
            loading_render = loading.render("LOADING..", True, white)
            bootup.blit(loading_render, (140, 610))
            rect_width += 0.75
        elif seconds < 2:
            loading_render = loading.render("LOADING...", True, white)
            bootup.blit(loading_render, (140, 610))
            rect_width += 11
        elif seconds < 3:
            loading_render = loading.render("LOADING...", True, white)
            bootup.blit(loading_render, (140, 610))
            rect_width += 1
    else:
        if play == 1:
            play = 2  # Avoids loop
        boot_sound.stop()  # Stops previous sound effect
        if play != 3:  # Plays the sound effect once
            pg.mixer.Channel(0).play(boot_finished)
            play = 3  # Avoids loop
        rect_width = 1300  # Ensures the width goes to the right place
        loading_render = loading.render("LOADING COMPLETE...", True, white)
        bootup.blit(loading_render, (140, 610))
        if seconds > 2.8:
            play = 3
            return True


def boot(screen, clock):
    global fade_alpha, fade_in, start_fade, first_fade, start_ticks, load_confirm, second_fade, last_fade, play
    seconds = (pg.time.get_ticks() - start_ticks) / 1000  # Timer

    # Fade Opacity
    fade.set_alpha(fade_alpha)  # Opacity (0-255)

    # Set Background Colour
    screen.fill(black)

    if not first_fade:
        load = loading_screen()  # Loading Bar
        load_confirm = load

    if load_confirm and not first_fade:  # Only lets the parameter be changed once
        start_fade = True
        start_ticks = pg.time.get_ticks()  # Resets timer to avoid hanging bug

    # Fade Out
    if fade_in and start_fade:
        fade_alpha += 2
        if fade_alpha >= 300:
            start_fade = False
            fade_in = False
            first_fade = True
            load_confirm = False
            if last_fade:
                c.state = 1  # Goes to main menu when animations are over

    # Fade In
    elif not fade_in and not start_fade and second_fade:
        fade_alpha -= 2
        if fade_alpha == 0:
            fade_in = True
            second_fade = False

    if first_fade and 1 < seconds:  # Show the logo after the first fade
        screen.blit(logo, (400, 0))
        second_fade = True
        if play == 3 and 1.5 < seconds:  # Plays the sound effect once
            pg.mixer.music.play()
            play = 4  # Avoids loop

        if 4.5 < seconds:  # Activate last fade
            fade_in = True
            start_fade = True
            last_fade = True
    screen.blit(bootup, (0, 0))
    screen.blit(fade, (0, 0))  # Fade Overlay
    clock.tick(165)  # Run at 165FPS
