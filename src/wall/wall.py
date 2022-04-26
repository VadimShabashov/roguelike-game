import pygame

from src.images.images import Images


class Wall(pygame.sprite.Sprite):
    image = Images.get_image_wall()

    def __init__(self, tiling, ind_x, ind_y):
        super().__init__()
        self.rect = Wall.image.get_rect()
        self.tiling = tiling

        size = self.tiling.get_size()
        shift_x, shift_y = self.tiling.get_shifts()
        self.rect.x = ind_x * size + shift_x
        self.rect.y = ind_y * size + shift_y
