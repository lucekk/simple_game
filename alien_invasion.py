import sys

import pygame

def run_game():
    # Initializing the game and making screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Space invazion!')

    # Main loop start
    while True:

        # Waiting for keybord or mouse click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    # Displaing last modyfid screen
    pygame.display.flip()

run_game()        