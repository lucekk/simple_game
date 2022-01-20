from ast import alias
from re import A
from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
import sys
from time import sleep
from xmlrpc.client import TRANSPORT_ERROR
from matplotlib.pyplot import get
from numpy import number
import py
import pygame
from bullet import Bullet
from alien import Alien



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Key push reaction'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True    
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()  



def get_number_rows(ai_settings, ship_height, alien_height):
    '''How many aliens rows culd be on the screen'''
    avalible_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avalible_space_y / (2 * alien_height))
    return number_rows



def get_number_aliens_x(ai_settings, alien_width):
    '''How many aliens could be in the row'''
    avaible_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaible_space_x / (2 * alien_width))
    return number_aliens_x



def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Making aline in puting in the row
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)



def  create_fleet(ai_settings, screen, ship, aliens):
    '''Making a fleet'''
    # Single alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Whole fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



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



def check_events(ai_settings, stats, screen, ship, bullets, play_button, aliens):
    '''controling'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_bitton(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_button(ai_settings, stats, play_button, mouse_x, mouse_y, ship, screen, aliens, bullets):
    '''Starting new game after pressing button and resetings after old game'''
    button_cliked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_cliked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        # New fleet
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_fleet_edges(ai_settings, aliens):
    '''Alien-edge reaction'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break



def change_fleet_direction(ai_settings, aliens):
    '''Getting whole fleet step down and change direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # Reaction alien-ship collision
    if stats.ships_left > 0:
        stats.ship_left -= 1
        #Deleting contests of lists aleiens and bullets
        aliens.empty()
        bullets.empty()
        # New fleet
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
         # Stop
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
   

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''Checking and updating postions of the aliens'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Detecting alien-ship colison
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        print ('Bagniak Cię dopadł! :C')


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''Updating positions of bullets and deleting out of range bullets'''
    # Updating bullets position
    bullets.update()
    
    # Deleting out-of-window bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_colissions(ai_settings, screen, ship, aliens, bullets)



def check_bullet_alien_colissions(ai_settings, screen, ship, aliens, bullets):
    # Checking collisons wirh aliens and removing destroyed alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # New fleet without old bullets
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)



def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    '''Updating/Changing screens'''
    # Refreshing screen in every iteration of loop
    screen.fill(ai_settings.bg_color)
    # Displaing bullets beneth spaceship and enemis layers
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)

    # Displaing button only if game is inactive

    if not stats.game_active:
        play_button.draw_button()

    # Displaing last modyfid screen
    pygame.display.flip()