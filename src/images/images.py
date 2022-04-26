import random
import pygame


class Images:
    path_enemies = ["enemy1.png", "enemy2.png", "enemy3.png"]
    path_hero = "hero.png"
    path_wall = "wall.jpg"
    images_dir = "src/resources/"

    size = pygame.image.load(images_dir + path_wall).get_width()

    @staticmethod
    def get_image_hero():
        return pygame.image.load(Images.images_dir + Images.path_hero)

    @staticmethod
    def get_image_enemy():
        random_enemy = random.choice(Images.path_enemies)
        return pygame.image.load(Images.images_dir + random_enemy)

    @staticmethod
    def get_image_wall():
        return pygame.image.load(Images.images_dir + Images.path_wall)

    @staticmethod
    def get_image_size():
        return Images.size
