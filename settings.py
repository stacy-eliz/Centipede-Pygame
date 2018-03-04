class Settings():
    def __init__(self):
        # для экрана
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0,0,0) #0,0,0
        self.player_speed_factor = 1.5 #величина смещения игрока
        # для пуль
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,244,79)
        self.bullets_allowed = 5 # максимум пуль на экране
        # для гриба
        self.y_mushroom_range = (self.screen_height // 50) - 2 # делим на высоту картинки гриба