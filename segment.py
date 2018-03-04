import pygame

from settings import Settings

settings = Settings()

class Segment(pygame.sprite.Sprite):
    def __init__(self, speed, pos, screen):
        super().__init__()
        self.speed = speed # перемещение по x и по y
        self.image = pygame.transform.scale(pygame.image.load("./data/foto/centipede_body.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vertical_shift = 50
        self.horizontal_speed = speed[0] # сначала змейка движется влево
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def speed_change(self):
        new_speed = []
        if self.speed[1]!=0:
            return [self.speed[0], 0]
        if self.rect.left<=0:
            new_speed = [self.horizontal_speed, self.vertical_shift]
        elif self.rect.right>=settings.screen_width:
            new_speed = [-self.horizontal_speed, self.vertical_shift]
        if (self.rect.top <= 0 and self.vertical_shift < 0) or (self.rect.bottom >= settings.screen_height and self.vertical_shift > 0):
            self.vertical_shift *= -1
        if new_speed==[]:
            return self.speed
        else:
            return new_speed

    def update(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        new_speed = self.speed_change()
        if new_speed[0] != self.speed[0]:
            self.rotate()
        self.speed = new_speed

    def collision(self):
        new_speed = [-self.horizontal_speed, self.vertical_shift]
        self.speed = new_speed

    def rotate(self):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = old_center