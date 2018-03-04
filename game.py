import pygame
from pygame.sprite import Group
import sys
import itertools
import random

from settings import Settings
from shooter import Shooter
import game_function as gf
from snake import Centipede
from intro import GUI, Button, Label
from particles import Particle

speed = 1
text = None
settings = Settings()
pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Centipede')

all_sprites = Group()
bullets = Group()  # группа для хранения пуль
mushrooms = Group()
shooter_group = Group()
logo = Group()

gui = GUI()
Label('name_game', logo, settings)
Label('centipede', logo, settings)
b1 = Button((settings.screen_width // 2 - 150, settings.screen_height // 2 - 100, 400, 100), 'start')
b2 = Button((settings.screen_width // 2 - 150, settings.screen_height // 2 + 100, 400, 100), 'exit')
gui.add_element(b1)
gui.add_element(b2)

centipede = Centipede([speed, 0], [300, 0], screen, 7)
gf.make_mushrooms(settings, mushrooms, 15)
shooter = Shooter(settings, screen)

cursor = pygame.sprite.Sprite()
cursor.image = pygame.transform.scale(pygame.image.load("./data/foto/arrow.png"), (50, 50))
cursor.rect = cursor.image.get_rect()

shooter_group.add(shooter)
all_sprites.add(shooter)
all_sprites.add(centipede)
no_control_player = [centipede]

image_text_lose = pygame.transform.scale(pygame.image.load("./data/foto/game_over.png"), (900, 800))
rect = image_text_lose.get_rect()
rect.centerx = settings.screen_width//2
rect.centery = settings.screen_height//2

cursor = pygame.sprite.Sprite()
cursor.image = pygame.transform.scale(pygame.image.load("./data/foto/arrow.png"), (50, 50))
cursor.rect = cursor.image.get_rect()

pygame.mouse.set_visible(False)

running1 = True
running2 = True
running3 = True

text = None
def screen_1():
    global running1, running2, running3

    pygame.mixer.music.pause()
    clock = pygame.time.Clock()
    while running1:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                running2 = False
                running3 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.get_event(event):
                    running2 = True
                    running1 = False
                if b2.get_event(event):
                    running1 = False
                    running2 = False
                    running3 = False
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            gui.get_event(event)
        # отрисовываем все GUI-элементы
        gui.render(screen)
        logo.draw(screen)
        # обновляеем все GUI-элементы
        gui.update()
        if pygame.mouse.get_focused():
            screen.blit(cursor.image, cursor.rect)
        clock.tick(50)
        pygame.display.flip()

def screen_2():
    global running1, running2, running, cursor, text, bullet, centipede, no_control_player, music

    music = pygame.mixer.music.load('./data/music/background_music.mp3')
    pygame.mixer.music.play(-1, 0.0)
    clock = pygame.time.Clock()
    while running2:
        gf.check_events(settings, screen, shooter, bullets)

        injured_segments_list = []
        collisions = pygame.sprite.groupcollide(bullets, centipede, True, False)
        for bullet in collisions:
            injured_segments_list.append(collisions[bullet])
        new_mushroom = centipede.delete_segment([segment for segments in injured_segments_list for segment in segments], mushrooms)

        if new_mushroom!=None:
            mushrooms.add(new_mushroom)

        collisions = pygame.sprite.groupcollide(centipede,  mushrooms, False, False)
        centipede.collision(collisions)

        collisions = pygame.sprite.groupcollide(bullets, mushrooms, True, True)
        if collisions:
            # количество создаваемых частиц
            particle_count = 3
            # возможные скорости
            numbers = range(-5, 5)
            for _ in range(particle_count):
                for bullet in collisions:
                    for mushroom in collisions[bullet]:
                        new_circle = Particle((mushroom.rect.x, mushroom.rect.y), random.choice(numbers), random.choice(numbers), all_sprites, screen)

        shooter.update()
        gf.update_screen(settings, screen, bullets)
        gf.update_bullets(bullets)

        status1 = pygame.sprite.spritecollide(shooter, mushrooms, False, pygame.sprite.collide_mask)
        status2 = pygame.sprite.spritecollide(shooter, centipede, False, pygame.sprite.collide_mask)
        if status1 or status2:
            text = 'LOSE'
            running2 = False

        for sprites in list(itertools.chain(no_control_player)):
            if type(sprites) == list:
                for sprite in sprites:
                    sprite.update()
            else:
                sprites.update()

        for sprite in all_sprites:
            sprite.update()
            screen.blit(sprite.image, sprite.rect)

        all_sprites.add(itertools.chain(no_control_player))
        all_sprites.add(itertools.chain(mushrooms))

        if len(centipede) == 0:
            centipede = Centipede([speed, 0], [300, 0], screen, 7)
            all_sprites.add(centipede)
            no_control_player = [centipede, mushrooms]
            gf.make_mushrooms(settings, mushrooms, 3)
            continue

        clock.tick(100)
        pygame.display.flip()

def screen_3():
    global running1, running2, running3, text

    pygame.mixer.music.pause()
    clock = pygame.time.Clock()
    while running3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
        screen.blit(image_text_lose, rect)
        if pygame.mouse.get_focused():
            screen.blit(cursor.image, cursor.rect)
        clock.tick(50)
        pygame.display.flip()

screen_1()
screen_2()
screen_3()