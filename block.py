import pygame
from colors import Colors
from pos import Pos

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rot_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_pos(self):
        tiles = self.cells[self.rot_state]
        moved_tiles = []
        for pos in tiles:
            pos = Pos(pos.row + self.row_offset, pos.column + self.column_offset)
            moved_tiles.append(pos)
        return  moved_tiles

    def rotate(self):
        self.rot_state += 1
        if self.rot_state == len(self.cells):
            self.rot_state = 0

    def undo_rot(self):
        self.rot_state -= 1
        if self.rot_state == 0:
            self.rot_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_pos()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)