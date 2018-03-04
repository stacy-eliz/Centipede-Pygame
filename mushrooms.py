import pygame

class Mushrooms(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load("./data/foto/mushroom.png"), (50, 50))

    def __init__(self, mushrooms, x, y):
        super().__init__(mushrooms)
        self.image = Mushrooms.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)