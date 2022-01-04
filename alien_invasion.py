import sys

import pygame

def run_game():
    # Initializing the game and making screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Space invazion!')
    # Background color
    bg_color = (230, 230, 230)
    # Main loop start
    while True:

        # Waiting for keybord or mouse click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    #Refreshing screen in every iteration of loop
    screen.fill(bg_color)

    # Displaing last modyfid screen
    pygame.display.flip()

run_game()        