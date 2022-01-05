import sys

import pygame

def check_events():
    '''controling'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move right
                ship.rect.centerex += 1    

def update_screen():
    '''Updating/Changing screens'''
    # Refreshing screen in every iteration of loop
    screen.fill(ai_settings.bg_color)
    ship.blitme

    # Displaing last modyfid screen
    pygame.display.flip()