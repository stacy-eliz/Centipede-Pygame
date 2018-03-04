import pygame
from segment import Segment
from mushrooms import Mushrooms

class Centipede(pygame.sprite.Group):
    body_list = []

    def __init__(self, speed, pos, screen, length):
        shift = 36
        segment_shift = shift
        x, y = pos[0], pos[1]
        x+=segment_shift
        for j in range(length):
            Centipede.body_list.append(Segment(speed, (x, y), screen))
            x += segment_shift
        super().__init__(Centipede.body_list)

    def delete_segment(self, injured_segment, mushrooms):
        if len(injured_segment) <= 0:
            return None

        for segment in range(len(Centipede.body_list)):
            if Centipede.body_list[segment].rect.colliderect(injured_segment[0].rect):
                mushroom = self.split(segment, mushrooms)
                return mushroom

    def split(self, pos, mushrooms):
        remove_segment = Centipede.body_list[pos]
        new_mushroom = Mushrooms(mushrooms, remove_segment.rect.x, remove_segment.rect.y)
        Centipede.body_list.remove(remove_segment)
        remove_segment.kill()
        return new_mushroom

    def collision(self, collisions):
        for segment in collisions:
             segment.collision()
        return