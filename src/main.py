import sys
import pygame

from src.game.game import Game
from src.event.event import Event


class Window:
    def __init__(self):
        # Sizes can be arbitrary, but for beautiful map it is recommended to choose multiples of the block sizes
        self.width = 1395
        self.height = 945

        pygame.init()
        # Add title
        pygame.display.set_caption("Cool roguelike-game")
        # Add Surface object, where other objects are added for visualization
        self.screen = pygame.display.set_mode([self.width, self.height])

        self.game = Game(self.width, self.height)

        #
        # self.game.map.save_map()

    def update_screen(self):
        sprite_groups = self.game.get_sprite_groups()

        # Set background color (command erases previous images from screen)
        self.screen.fill((0, 0, 0))

        for group in sprite_groups:
            group.update()
            group.draw(self.screen)

        pygame.display.flip()

    def show(self):
        while True:
            self.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game.event_executor(Event(0, 2))
                    elif event.key == pygame.K_DOWN:
                        self.game.event_executor(Event(0, 3))
                    elif event.key == pygame.K_LEFT:
                        self.game.event_executor(Event(0, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.game.event_executor(Event(0, 1))
                    elif event.key == pygame.K_s:
                        self.game.event_executor(Event(1, 0))
                    elif event.key == pygame.K_l:
                        self.game.event_executor(Event(1, 1))
                    elif event.key == pygame.K_n:
                        self.game.event_executor(Event(2, 0))

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    window = Window()
    window.show()
