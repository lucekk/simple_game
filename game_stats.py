from re import S


class GameStats():
    '''Statistic fo 'Bagno Invazion!'.'''

    def __init__(self, ai_settings):
        '''Data initialization'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # Starting game in active state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        '''Statistic data initialization up to game changes'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1