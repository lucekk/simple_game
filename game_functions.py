import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Key push reaction'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True    
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Fire bullet if its allowed''' 
    # Creating new bullet and adding it to the group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    '''Key free reaction'''        
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False   

def check_events(ai_settings, screen, ship):
    '''controling'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    '''Updating positions of bullets and deleting out of range bullets'''
    # Updating bullets position
    bullets.update()
    
    # Deleting out-of-window bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))

def update_screen(ai_settings, screen, ship, bullets):
    '''Updating/Changing screens'''
    # Refreshing screen in every iteration of loop
    screen.fill(ai_settings.bg_color)
    # Displaing bullets beneth spaceship and enemis layers
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme

    # Displaing last modyfid screen
    pygame.display.flip()