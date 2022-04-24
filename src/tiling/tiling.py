import numpy as np

from src.images.images import Images


class Tiling:
    """
    Class, that contains play-board. It is split into squares and each cell contains one the following flags:
    0 - empty cell
    1 - wall
    2 - enemy
    3 - hero
    """
    def __init__(self, width, height):
        # Cell size
        self.size = Images.get_image_size()

        # Playing board dimensions. Matrix dimensions has to be odd for maze generation algorithm
        self.dim_x = (width // self.size - 1) // 2 * 2 + 1
        self.dim_y = (height // self.size - 1) // 2 * 2 + 1

        # Shifts from the left and right borders, since number of blocks in the line can be non-integral
        self.shift_x = (width - self.dim_x * self.size) / 2
        self.shift_y = (height - self.dim_y * self.size) / 2

        self.cells = np.ones((self.dim_x, self.dim_y))

    def get_tiling(self):
        return self.cells

    def get_wall_cells(self):
        return np.argwhere(self.cells == 1)

    def get_non_wall_cells(self):
        return np.argwhere(self.cells != 1)

    def get_empty_cells(self):
        return np.argwhere(self.cells == 0)

    def get_dimensions(self):
        return self.dim_x, self.dim_y

    def get_shifts(self):
        return self.shift_x, self.shift_y

    def get_size(self):
        return self.size

    def check_collision(self, ind_x, ind_y):
        """
        Method returns true if there is no collision: (ind_x, ind_y) - is empty
        """
        if self.cells[ind_x, ind_y] == 0:
            return True
        else:
            return False

    def add_to_tiling(self, ind_x, ind_y, flag):
        self.cells[ind_x, ind_y] = flag

    def move_in_tiling(self, prev_x, prev_y, new_x, new_y, flag):
        self.cells[prev_x, prev_y] = 0
        self.cells[new_x, new_y] = flag
