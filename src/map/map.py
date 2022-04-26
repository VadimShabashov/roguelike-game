import json
import random
from collections import deque
import pygame

from src.wall.wall import Wall


class Map:
    def __init__(self, tiling, flag=0):
        """
        Class for grouping the walls and generating the maze.
        flag - if the map has to be loaded from file
        """
        self.tiling = tiling
        self.walls = pygame.sprite.Group()

        if flag:
            self.load_map()
        else:
            self.generate_maze()

        self.convert_to_walls()

    def convert_to_walls(self):
        """
        Convert wall_matrix to group of
        """
        wall_indices = self.tiling.get_wall_cells()

        for ind_x, ind_y in wall_indices:
            self.walls.add(Wall(self.tiling, ind_x, ind_y))

    def find_allowed_cells(self, x, y, flag):
        """
        Method looks for neighbors of the cell (x, y), which contains flag in wall_matrix
        """
        tiling_matrix = self.tiling.get_tiling()
        dim_x, dim_y = self.tiling.get_dimensions()
        empty_neighbors = []

        if (x - 2 > 0) and (tiling_matrix[x - 2, y] == flag):
            empty_neighbors.append((x - 2, y))

        if (x + 2 < dim_x - 1) and (tiling_matrix[x + 2, y] == flag):
            empty_neighbors.append((x + 2, y))

        if (y - 2 > 0) and (tiling_matrix[x, y-2] == flag):
            empty_neighbors.append((x, y - 2))

        if (y + 2 < dim_y - 1) and (tiling_matrix[x, y+2] == flag):
            empty_neighbors.append((x, y + 2))

        return empty_neighbors

    def mark_cell(self, cell_x, cell_y, flag):
        """
        Method marks cell in wall_matrix with flag
        """
        tiling_matrix = self.tiling.get_tiling()
        tiling_matrix[cell_x, cell_y] = flag

    def connect_cell(self, cell_x, cell_y):
        """
        Method connects cell with randomly chosen allowed neighbor
        """
        tiling_matrix = self.tiling.get_tiling()
        path_neighbors = self.find_allowed_cells(cell_x, cell_y, 0)
        if path_neighbors:
            neighbor_x, neighbor_y = random.choice(path_neighbors)  # neighbor to connect with
            tiling_matrix[(cell_x + neighbor_x) // 2, (cell_y + neighbor_y) // 2] = 0

    def generate_maze(self):
        """
        Modified version of randomized Prim’s Algorithm is used
        https://hurna.io/academy/algorithms/maze_generator/prim_s.html
        """
        tiling_matrix = self.tiling.get_tiling()
        start_indices = (1, 1)  # Initial position of the hero
        cells_queue = deque([start_indices])  # Cells to consider for path

        while cells_queue:
            cell_x, cell_y = cells_queue.popleft()
            if tiling_matrix[cell_x, cell_y]:
                self.mark_cell(cell_x, cell_y, 0)  # Mark cell as part of path
                self.connect_cell(cell_x, cell_y)  # Randomly connect cell to already existed path
                neighbors = self.find_allowed_cells(cell_x, cell_y, 1)  # find wall-cell neighbors
                cells_queue.extend(neighbors)

    def get_walls(self):
        return self.walls

    def indices_to_matrix(self, indices):
        tiling_matrix = self.tiling.get_tiling()
        for x, y in indices:
            tiling_matrix[x, y] = 0

    def save_map(self):
        dim_x, dim_y = self.tiling.get_dimensions()
        with open("src/saved_maps/map.json", 'w+') as file:
            json.dump({"board_width": dim_x,
                       "board_height": dim_y,
                       "wall_cells": self.tiling.get_non_wall_cells().tolist()},
                      file)

    def load_map(self):
        dim_x, dim_y = self.tiling.get_dimensions()
        with open("src/saved_maps/map.json", 'r') as file:
            data = json.load(file)
        if (dim_x == data["board_width"]) and (dim_y == data["board_height"]):
            self.indices_to_matrix(data["wall_cells"])
