import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Single alien in the fleet'''

    def __init__(self, ai_settings, screen):
        '''Single alien inizialitation and position'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Alien image loading and definig its atribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Alien positioning
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Conteinig position
        self.x = float(self.rect.x)

    def check_edges(self):
        '''return True if aliens are at the edge'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''Moving left/right'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        '''Alien displaying'''
        self.screen.blit(self.image, self.rect)