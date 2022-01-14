from re import S


class GameStats():
    '''Statistic fo 'Bagno Invazion!'.'''

    def __init__(self, ai_settings):
        '''Data initialization'''
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        '''Statistic data initialization up to game changes'''
        self.ship_left = self.ai_settings.ship_limit