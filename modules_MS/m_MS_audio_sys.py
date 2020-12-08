# Daniel Zhuo
# Modern Snek Module - Master Sound System
# Plays Sound Effects and Music

import os

import pygame as pg

from . import config as c
from . import m_MS_options
from . import m_MS_snek_assets as SA

# Main Menu Music
cardigan = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/8 Bit Universe - Cardigan (Taylor Swift).mp3")
# Choose Mode Music
diamond_sword = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/8 Bit Universe - I Can Swing My Sword!.mp3")
# Game Music
congratulations = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/8 Bit Universe - Congratulations.mp3")
terrible = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/Revenge - Daniel Cover (TERRIBLE).mp3")  # TERRIBLE
moskau = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/Dschinghis Khan - Moskau.mp3")
coronavirus = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/iMarkkeyz - Coronavirus ft. Cardi B.mp3")
# Death
smack = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/snek_death.mp3")
oof = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/Old Minecraft Hurt Sound.mp3")
weh = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/weh weh weh.mp3")
ow = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/snek_death_daniel.mp3")
astronomia = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/8 Bit Universe - Astronomia.mp3")
# Easter Eggs
rick_roll = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/8 Bit Universe - Never Gonna Give You Up.mp3")
activate_rick_roll_s = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/Never Gonna Give You Up.mp3")
deactivate_rick_roll_s = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/Gonna Give You Up.mp3")
cat = pg.mixer.Sound(os.getcwd() + "/resources_MS/music/C418 - Cat (Minecraft Volume Alpha).mp3")
# Menu Interaction
whoosh = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/transition_whoosh.mp3")
m_click = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/mouse_click.mp3")
ding = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/ding.mp3")
plop_1 = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/plop_1.mp3")
plop_2 = pg.mixer.Sound(os.getcwd() + "/resources_MS/menu_interaction/plop_2.mp3")
# Snek Movement
move_up = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/move_up.mp3")
move_down = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/move_down.mp3")
move_right = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/move_right.mp3")
move_left = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/move_left.mp3")
daniel_up = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/daniel_up.mp3")
daniel_down = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/daniel_down.mp3")
daniel_right = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/daniel_right.mp3")
daniel_left = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/daniel_left.mp3")
# Crunch
crunch_0 = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/snek_crunch_0.mp3")
crunch_1 = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/snek_crunch_1.mp3")
crunch_2 = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/snek_crunch_2.mp3")
crunch_3 = pg.mixer.Sound(os.getcwd() + "/resources_MS/sfx/snek_crunch_3.mp3")


# ------------------------------------------------------------------------------------------------------------------
def dj(main, mode, game, death, fade, ms, change, sfx_c, sfx):
    """ Handles music activation, switching, and fading.
    Args:
        main::bool
            Boolean that decides if the Main Menu song plays or not
        mode::bool
            Boolean that decides if the Choose Mode song plays or not
        game::bool
            Boolean that decides if the Game song plays or not
        death::bool
            Boolean that decides if the Death song plays or not
        fade::mixer.channel
            Specifies a specific Pygame Channel to fade its audio out
        ms::int
            Specifies how long the fadeout is in milliseconds
        change::bool
            Changes global boolean to switch songs in play_sounds()
        sfx_c::mixer.channel
            Specifies a specific Pygame Channel to play, usually, a click sound
        sfx::sound file
            Specifies the "click sound"
    """
    # ------------------------------------------------------------------------------------------------------------------
    c.main_menu_song = main
    c.pick_mode_song = mode
    c.game_song = game
    c.death_song = death
    fade.fadeout(ms)
    c.change_song = change
    sfx_c.play(sfx)  # Click Sound
    # ------------------------------------------------------------------------------------------------------------------


def play_songs():
    """ Switches songs when prompted; based off states, modes, and/or Rick Roll
    Notes:
        pg.mixer.channel.play(Sound, loops=0, maxtime=0, fade_ms=0)
    """
    # ------------------------------------------------------------------------------------------------------------------
    # Music
    if c.music_e and c.state != 0:
        if c.change_song:  # Boolean Activates to Change Song
            # Main Menu, Options, How to Play, Credits Music
            if c.main_menu_song:
                if SA.snek_box:
                    c.channel1.play(cat, -1, 0, 2000)
                else:
                    c.channel0.play(cardigan, -1, 0, 2000)
            # Choose Mode
            elif c.pick_mode_song and not SA.snek_box:
                c.channel1.play(diamond_sword, -1, 0, 2000)
            # Game Song
            elif c.game_song:
                if not c.rick_roll:
                    if c.m_base_e:
                        c.channel2.play(congratulations, -1, 0, 2000)
                    elif c.m_daniel_e:
                        c.channel2.play(terrible, -1, 0, 2000)
                    elif c.m_soviet_e:
                        c.channel2.play(moskau, -1, 0, 2000)
                    elif c.m_covid_e:
                        c.channel2.play(coronavirus, -1, 0, 2000)
                elif c.rick_roll:
                    c.channel1.play(rick_roll, -1)
            elif c.death_song:
                c.channel1.play(astronomia)
        # --------------------------------------------------------------------------------------------------------------
        if c.state != 0:
            c.change_song = False  # Reset Boolean If State Not 0
    # ------------------------------------------------------------------------------------------------------------------
    else:  # Pause Channel When Music is Disabled
        c.change_song = True  # Reset Value So
    # ------------------------------------------------------------------------------------------------------------------


def set_volume():
    """Sets the volume of already declared pygame music mixer channels"""
    # ------------------------------------------------------------------------------------------------------------------
    # Music Channel and Audio Control
    c.channel0.set_volume(m_MS_options.music_volume)
    c.channel1.set_volume(m_MS_options.music_volume)
    c.channel2.set_volume(m_MS_options.music_volume)
    # Enable Music
    if c.music_e:
        c.channel0.unpause()
        c.channel1.unpause()
        c.channel2.unpause()
    # Mute Music
    else:
        c.channel0.pause()
        c.channel1.pause()
        c.channel2.pause()
        c.change_song = True  # Reset song choice when un-muted
    # ------------------------------------------------------------------------------------------------------------------
    # Sound Effect Channels & Volume Control
    if c.sfx_e:
        c.channel3.set_volume(m_MS_options.sfx_volume)
        c.channel4.set_volume(m_MS_options.sfx_volume)
        c.channel5.set_volume(m_MS_options.sfx_volume)
    # Mute Sound Effects - Only pausing doesn't work - music bugs and stops
    else:
        c.channel3.set_volume(0)
        c.channel4.set_volume(0)
        c.channel5.set_volume(0)
    # ------------------------------------------------------------------------------------------------------------------


def audio_mixer():
    """Parent audio function used to be called in the main loop"""
    play_songs()
    set_volume()
