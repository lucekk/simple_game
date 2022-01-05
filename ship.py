class Ship():

    def __init__(self, screen):
        '''Inizalizing space ship and its position'''
        self.screen = screen

        # Space ship loading, downloading its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every new space ship appear at bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Displaing space ship in actual position'''
        self.screen.blit(self.image, self.rect)