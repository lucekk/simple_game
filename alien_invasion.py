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
    # MAking space ship
    ship = Ship(screen)
    # Background color
    bg_color = (230, 230, 230)
    # Main loop start
    while True:
        gf.check_events()
    
        # Refreshing screen in every iteration of loop
        screen.fill(ai_settings.bg_color)
        ship.blitme

        # Displaing last modyfid screen
        pygame.display.flip()

run_game()        