import abc
import random
import pygame

from src.images.images import Images


class Entity(pygame.sprite.Sprite, abc.ABC):
    """
    Class corresponding for every entity in the maze, except for wall.
    Some methods are denoted abstract, because they can be only called in children of the class
    """
    def __init__(self, tiling):
        super().__init__()
        self.tiling = tiling
        self.ind_x = None
        self.ind_y = None
        self.rect = None
        self.flag = None

    def find_position(self):
        empty_cells = self.tiling.get_empty_cells()
        return random.choice(empty_cells)

    @abc.abstractmethod
    def set_position(self, ind_x, ind_y):
        self.tiling.add_to_tiling(ind_x, ind_y, self.flag)
        self.ind_x = ind_x
        self.ind_y = ind_y
        self.update_rect()

    @abc.abstractmethod
    def update_rect(self):
        size = self.tiling.get_size()
        shift_x, shift_y = self.tiling.get_shifts()
        self.rect.x = self.ind_x * size + shift_x
        self.rect.y = self.ind_y * size + shift_y


class Character(Entity, abc.ABC):
    """
    Class corresponding to the hero and enemies
    """
    def __init__(self, tiling):
        super().__init__(tiling)
        self.view = 1  # 0 - character looks to the left, 1 - character looks to the right
        self.flag = None
        self.image = None
        self.rect = None

    @abc.abstractmethod
    def move_left(self):
        if self.view == 1:
            self.image = pygame.transform.flip(self.image, True, False)
            self.view = 0

        if self.tiling.check_collision(self.ind_x - 1, self.ind_y):
            self.tiling.move_in_tiling(self.ind_x, self.ind_y, self.ind_x - 1, self.ind_y, self.flag)
            self.ind_x -= 1
            self.update_rect()

    @abc.abstractmethod
    def move_right(self):
        if self.view == 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.view = 1

        if self.tiling.check_collision(self.ind_x + 1, self.ind_y):
            self.tiling.move_in_tiling(self.ind_x, self.ind_y, self.ind_x + 1, self.ind_y, self.flag)
            self.ind_x += 1
            self.update_rect()

    @abc.abstractmethod
    def move_up(self):
        if self.tiling.check_collision(self.ind_x, self.ind_y - 1):
            self.tiling.move_in_tiling(self.ind_x, self.ind_y, self.ind_x, self.ind_y - 1, self.flag)
            self.ind_y -= 1
            self.update_rect()

    @abc.abstractmethod
    def move_down(self):
        if self.tiling.check_collision(self.ind_x, self.ind_y + 1):
            self.tiling.move_in_tiling(self.ind_x, self.ind_y, self.ind_x, self.ind_y + 1, self.flag)
            self.ind_y += 1
            self.update_rect()


class Hero(Character):
    def __init__(self, tiling):
        super().__init__(tiling)
        self.image = Images.get_image_hero()
        self.rect = self.image.get_rect()
        self.flag = 3

        ind_x, ind_y = self.find_position()
        self.set_position(ind_x, ind_y)

    def move_left(self):
        super().move_left()

    def move_right(self):
        super().move_right()

    def move_up(self):
        super().move_up()

    def move_down(self):
        super().move_down()

    def set_position(self, ind_x, ind_y):
        super().set_position(ind_x, ind_y)

    def update_rect(self):
        super().update_rect()


class Enemy(Character):
    def __init__(self, tiling):
        super().__init__(tiling)
        self.image = Images.get_image_enemy()
        self.rect = self.image.get_rect()
        self.flag = 2

        ind_x, ind_y = self.find_position()
        self.set_position(ind_x, ind_y)

    def move_left(self):
        super().move_left()

    def move_right(self):
        super().move_right()

    def move_up(self):
        super().move_up()

    def move_down(self):
        super().move_down()

    def set_position(self, ind_x, ind_y):
        super().set_position(ind_x, ind_y)

    def update_rect(self):
        super().update_rect()
