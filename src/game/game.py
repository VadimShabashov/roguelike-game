import random
from collections import deque
import pygame

from src.entity.entity import Hero, Enemy
from src.map.map import Map
from src.tiling.tiling import Tiling


class Game:
    """
    Class, which contains game entities and event executor
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiling = None
        self.map = None
        self.hero = None
        self.enemies = None

        self.initialization()

    def initialization(self, flag=0):
        self.tiling = Tiling(self.width, self.height)
        self.map = Map(self.tiling, flag)
        self.hero = Hero(self.tiling)
        self.enemies = pygame.sprite.Group()
        self.add_enemies()

    def add_enemies(self):
        number_enemies = random.randint(3, 8)
        for i in range(number_enemies):
            self.enemies.add(Enemy(self.tiling))

    def event_executor(self, event):
        """
        Method, which process events in the event_queue.
        """
        event_queue = deque([event])

        while event_queue:
            current_event = event_queue.popleft()
            if current_event.entity == 0:
                if current_event.action == 0:
                    self.hero.move_left()
                elif current_event.action == 1:
                    self.hero.move_right()
                elif current_event.action == 2:
                    self.hero.move_up()
                else:
                    self.hero.move_down()
            elif current_event.entity == 1:
                if current_event.action == 0:
                    self.map.save_map()
                else:
                    self.initialization(flag=1)
            elif current_event.entity == 2:
                if current_event.action == 0:
                    self.initialization()

    def get_sprite_groups(self):
        return [pygame.sprite.Group(self.hero), self.enemies, self.map.get_walls()]
