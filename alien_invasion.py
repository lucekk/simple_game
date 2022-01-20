import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Initializing the game and making screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Bagno invazion!')
    # Making 'play' button
    play_button = Button(ai_settings, screen ,"Dawej mnie to go!")
    # Game statistic
    stats = GameStats(ai_settings)
    # Making space ship
    ship = Ship(ai_settings, screen)
    # Group to contein bullets
    bullets = Group()
    # Group to contein aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop start
    while True:
        gf.check_events(ai_settings, screen, stats, ship, bullets, play_button, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)

run_game()        