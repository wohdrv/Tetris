import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.colors =  Colors.get_cell_colors()

    def print_grid(self):
        print("The grid with num. values:")
        for row in range(self.rows):
            for column in range(self.cols):
                print(self.grid[row][column], end = " ")
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.rows and column >= 0 and column < self.cols:
            return True
        return False

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for column in range(self.cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.cols):
            self.grid[row][column] = 0

    def row_down(self, row, rows):
        for column in range(self.cols):
            self.grid[row+rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.rows -1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.rows):
            for column in range(self.cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +21, row*self.cell_size +21, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)