import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, shooter):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = shooter.rect.centerx
        self.rect.top = shooter.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self): #обновляет позицию пули
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self): #отрисовка пули на экране
        pygame.draw.rect(self.screen, self.color, self.rect)