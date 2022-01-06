import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initializing the game and making screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Space invazion!')
    # Making space ship
    ship = Ship(ai_settings, screen)
    # Background color
    bg_color = (230, 230, 230)
    # Main loop start
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()        