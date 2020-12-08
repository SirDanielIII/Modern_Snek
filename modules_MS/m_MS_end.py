# Daniel Zhuo
# Modern Snek Module - End Screen
# State 8

import pygame as pg

from . import config as c
from . import m_MS_audio_sys as a
from . import m_MS_extra_modules
from . import m_MS_game
from . import m_MS_main_menu
from . import m_MS_menu_fades
from . import m_MS_snek_assets as SA
from .colours import *

# Screens/Surfaces
end_screen = pg.display.set_mode((c.width, c.height), c.surface_flags)
# Background Grid
end_background = pg.Surface((c.width, c.height), c.surface_flags)
end_background.blit(m_MS_main_menu.grid, (0, 0))
# Background Overlay
end_overlay = pg.Surface((c.width, c.height), c.surface_flags).convert_alpha()
pg.draw.rect(end_overlay, pg.Color('#487631'), (0, 0, c.width, c.height))
end_overlay.set_alpha(153)  # 60% Dark Green Overlay
# Pre Blit To Save Performance
end_background.blit(end_overlay, (0, 0))

# Global Variables
go_back = False

# Fonts
f_game_over = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 250)
f_play_again = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 136)
f_subtext = pg.font.Font("resources_MS/Big Noodle Titling.ttf", 65)
# Font Colors
play_again_c = white
main_menu_c = white
quit_game_c = white


# ----------------------------------------------------------------------------------------------------------------------
def end(screen, click, clock, fps, dt):
    """Function to run End Screen menu
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
    global go_back, play_again_c, main_menu_c, quit_game_c
    # ------------------------------------------------------------------------------------------------------------------
    mx, my = pg.mouse.get_pos()  # Get mouse position
    # ------------------------------------------------------------------------------------------------------------------
    # Blit Grid Backgrounds
    end_screen.blit(end_background, (0, 0))  # Grid Background
    end_screen.blit(m_MS_main_menu.header_box, (0, 0))  # Overlay
    # ------------------------------------------------------------------------------------------------------------------
    m_MS_extra_modules.draw_text("GAME OVER", white, f_game_over, end_screen, c.width / 2, 175)
    # ------------------------------------------------------------------------------------------------------------------
    # Highscore
    end_screen.blit(SA.trophy, SA.trophy_rect_end)
    highscore = f_play_again.render(str(c.highscore[0]), True, c.ms_yellow)
    end_screen.blit(highscore, (525, 428))
    # ------------------------------------------------------------------------------------------------------------------
    # Fruit Score
    # Different Fruits
    if c.m_base_e:
        end_screen.blit(SA.fruit_0_end, SA.apple_rect)
    elif c.m_daniel_e:
        end_screen.blit(SA.fruit_1_end, SA.apple_rect)
    elif c.m_soviet_e:
        end_screen.blit(SA.fruit_2_end, SA.apple_rect)
    elif c.m_covid_e:
        end_screen.blit(SA.fruit_3_end, SA.apple_rect)

    score = f_play_again.render(str(c.highscore[1]), True, c.ms_yellow)
    end_screen.blit(score, (225, 428))
    # ------------------------------------------------------------------------------------------------------------------
    # Death Description
    note = f_subtext.render(str(c.death_note), True, c.ms_red)
    end_screen.blit(note, (100, 590))
    # ------------------------------------------------------------------------------------------------------------------
    # Duration
    note = f_play_again.render(str(f"TIME LASTED: {m_MS_game.output_string}"), True, white)
    end_screen.blit(note, (100, 677))
    # ------------------------------------------------------------------------------------------------------------------
    # Buttons
    play_again = pg.Rect(950, 450, c.square_grid * 11, c.square_grid * 4)
    main_menu = pg.Rect(950, 700, c.square_grid * 5, c.square_grid * 2)
    quit_game = pg.Rect(1250, 700, c.square_grid * 5, c.square_grid * 2)
    # Drawing Buttons
    pg.draw.rect(end_screen, c.ms_blue, play_again)
    pg.draw.rect(end_screen, c.ms_blue, main_menu)
    pg.draw.rect(end_screen, c.ms_blue, quit_game)
    # Fonts
    m_MS_extra_modules.draw_text("PLAY AGAIN", play_again_c, f_play_again, end_screen, 1225, 550)
    m_MS_extra_modules.draw_text("MAIN MENU", main_menu_c, f_subtext, end_screen, 1075, 750)
    m_MS_extra_modules.draw_text("QUIT GAME", quit_game_c, f_subtext, end_screen, 1375, 750)

    # Button Collisions
    if play_again.collidepoint((mx, my)):
        play_again_c = c.ms_yellow
        if click:
            go_back = True
            m_MS_game.game_load()  # Reset GameVariables
            m_MS_game.return_screen = 7
            if not c.rick_rolled:
                a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                a.dj(False, False, True, False, c.channel1, 500, True, c.channel3, a.m_click)  # Audio Handler
            else:
                a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    else:
        play_again_c = white

    if main_menu.collidepoint((mx, my)):
        main_menu_c = c.ms_yellow
        if click:
            go_back = True
            m_MS_game.return_screen = 1
            if not c.rick_rolled:
                a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                a.dj(True, False, False, False, c.channel1, 500, True, c.channel3, a.m_click)  # Audio Handler
            else:
                a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
                a.dj(False, False, False, False, c.channel3, 0, False, c.channel3, a.m_click)  # Click Sound
    else:
        main_menu_c = white

    if quit_game.collidepoint((mx, my)):
        quit_game_c = c.ms_yellow
        if click:
            go_back = True
            m_MS_game.return_screen = 6
            a.dj(False, False, False, False, c.channel4, 0, False, c.channel4, a.whoosh)  # Whoosh Sound
            a.dj(False, False, False, False, c.channel1, 500, True, c.channel3, a.m_click)  # Audio Handler
    else:
        quit_game_c = white

    # Blit Screens
    screen.blit(end_screen, (0, 0))
    # ------------------------------------------------------------------------------------------------------------------
    # Fading In
    if not go_back:
        if m_MS_menu_fades.trans_alpha != 0:  # Renders overlay only when fading
            m_MS_menu_fades.dissolve_in(dt, clock, fps)  # Fade in screen
    # ------------------------------------------------------------------------------------------------------------------
    if go_back:
        m_MS_menu_fades.dissolve_out(dt, clock, fps)
        if m_MS_menu_fades.trans_alpha >= 300:
            go_back = False
            c.state = m_MS_game.return_screen

    # ------------------------------------------------------------------------------------------------------------------
    clock.tick(fps)
    # ------------------------------------------------------------------------------------------------------------------
