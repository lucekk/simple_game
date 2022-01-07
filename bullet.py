import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Spaceship bullets manegment'''

    def __init__(self, ai_settings, screen, ship):
        '''Making bulet object at actual spaceship position'''
        super().__init__()
        self.screen = screen

        # Making bullet rectangle in (0,0) point and definig proper positon
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_hight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
    
        # Bullet position defined by float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_collor
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        '''Moving of the bullet'''
        # Udating bullet posistion
        self.y -= self.speed_factor
        # Updating bullt rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        '''Displaing bullet'''
        pygame.draw.rect(self.screen, self.color, self.rect)