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

    def blitme(self):
        '''Alien displaying'''
        self.screen.blit(self.image, self.rect)