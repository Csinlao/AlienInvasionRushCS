class Settings:
    '''
    A class to store all settings for Alien Invasion.
    '''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (135, 206, 235)

        # Ship settings
        self.ship_speed = 10
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 10
        self.bullet_height = 70
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1