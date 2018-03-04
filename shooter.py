import pygame

class Shooter(pygame.sprite.Sprite):

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.transform.scale(pygame.image.load("./data/foto/shooter.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.player_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.player_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.player_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.player_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blit(self):
        self.screen.blit(self.image, self.rect)