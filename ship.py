import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''Inizalizing space ship and its position'''
        super(Ship ,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Space ship loading, downloading its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every new space ship appear at bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Center point of spaceship is float
        self.center = float(self.rect.centerx)

        # Spaceship moveing
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updateing rect object due to self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''Displaing space ship in actual position'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center ship on the bottom of screen'''
        self.center = self.screen_rect.centerx