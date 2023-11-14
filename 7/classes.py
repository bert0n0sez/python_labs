import pygame as pg
import numpy as np

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (255,119,255)

class GameOfLife(object):
    w_width, w_height = 600, 600
    finished = False
    FPS = 60
    screen = pg.display.set_mode((w_width, w_height))

    def __init__(self, filename, grid_size=50) -> None:
        self.grid_size = grid_size
        self.grid = self.init_grid(filename)
        self.input_mode = True

    def init_grid(self, filename):
        return np.loadtxt(filename, dtype='i', delimiter=',')

    def draw_grid(self):
        cell_size = self.w_width // self.grid_size
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pg.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
                if self.grid[x][y] == 1:
                    pg.draw.rect(self.screen, PURPLE, rect)
                else:
                    pg.draw.rect(self.screen, BLACK, rect)

    def update_state(self):
        new_grid = np.zeros((self.grid_size, self.grid_size))

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                left = (j-1) % self.grid_size
                right = (j+1) % self.grid_size
                up = (i-1) % self.grid_size
                down = (i+1) % self.grid_size

                neighbors = [self.grid[i, left], self.grid[i, right],
                            self.grid[up, j], self.grid[down, j],
                            self.grid[up, left], self.grid[up, right],
                            self.grid[down, left], self.grid[down, right]]
                total = sum(neighbors)

                if self.grid[i, j] == 1:
                    new_grid[i, j] = 1 if 2 <= total <= 3 else 0
                else:
                    new_grid[i, j] = 1 if total == 3 else 0

        self.grid = new_grid
    
    def run(self) -> None:
        pg.init()
        pg.display.set_caption('Game of Life')
        clock = pg.time.Clock()

        while not self.finished:
            clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.finished = True

            self.update_state()
            self.draw_grid()

            pg.display.flip()

        pg.quit()


