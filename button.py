import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        '''Inizialization button atribute'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Button size
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creating button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.ceter = self.screen_rect.center

        # Button msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Displaing mesage insdie rendered image and cntering text'''
        self.msg_image = self.front.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Dispaling empty button and measge on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
