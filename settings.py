class Settings():
    '''Class for game settings'''

    def __init__(self):
        '''Inizalizing game setings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # value of fleet-direction - 1 means right, -1 means left
        self.fleet_direction = 1