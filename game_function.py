import sys
import pygame
import random

from bullet import Bullet
from mushrooms import Mushrooms

def check_keydown_events(event, settings, screen, player, bullets):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, player, bullets)

def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False

def check_events(settings, screen, player, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, player, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def update_screen(settings, screen, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            bullet.kill()

def fire_bullet(settings, screen, shooter, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, shooter)  # создание пули
        bullets.add(new_bullet)

def make_mushrooms(settings, mushrooms, k_mushroom):
    for i in range(k_mushroom):
        y = random.randrange(2, settings.y_mushroom_range) * 50
        while True:
            flag = True
            x = random.randrange(50, settings.screen_width - 100)  # вычитаем удвоенную ширину картинки гриба
            for mushroom in mushrooms:
                if pygame.Rect(x, y, 50, 50).colliderect(mushroom):
                    flag = False
            if flag:
                break
        new_mushroom = Mushrooms(mushrooms, x, y)
        mushrooms.add(new_mushroom)
    return mushrooms