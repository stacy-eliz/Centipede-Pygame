import pygame

class GUI:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self, surface):
        for element in self.elements:
            render = getattr(element, "render", None)
            if callable(render):
                element.render(surface)

    def update(self):
        for element in self.elements:
            update = getattr(element, "update", None)
            if callable(update):
                element.update()

    def get_event(self, event):
        for element in self.elements:
            get_event = getattr(element, "get_event", None)
            if callable(get_event):
                element.get_event(event)

class Button(pygame.sprite.Sprite):
    def __init__(self, rect, text):
        super().__init__()
        if text=='start':
            self.image = pygame.image.load("./data/foto/start.png")
        elif text=='exit':
            self.image = pygame.image.load("./data/foto/exit.png")
        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.pressed = False

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
                return self.pressed

class Label(pygame.sprite.Sprite):
    def __init__(self, text, group, settings):
        super().__init__(group)
        if text=='name_game':
            self.image = pygame.image.load("./data/foto/name_game.png")
            self.rect = self.image.get_rect()
            self.rect.x = settings.screen_width//2-self.rect.width//2 # по центру экрана
            self.rect.y = 100
        elif text=='centipede':
            self.image = pygame.transform.scale(pygame.image.load("./data/foto/centipede.png"), (200, 200))
            self.rect = self.image.get_rect()
            self.rect.x = settings.screen_width//2-self.rect.width//2 # по центру экрана
            self.rect.y = 150