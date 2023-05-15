from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random()
        self.next_block = self.get_random()
        self.game_over = True
        self.lvl_point = 0
        self.score = 0
        self.music = random.randint(1, 3)

    def update_score(self, rows_cleared):
        if rows_cleared == 1:
            self.score += 100
        elif rows_cleared == 2:
            self.score += 200
        elif rows_cleared == 3:
            self.score += 300
        elif rows_cleared == 4:
            self.score += 400
        elif rows_cleared == 5:
            self.score += 500
        elif rows_cleared == 6:
            self.score += 600

    def get_random(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock()

    def lock(self):
        tiles = self.current_block.get_cell_pos()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared)
        if self.block_fits() == False:
            self.game_over = True
            print("Game stopped: Game over. Press Enter to play again.")
        self.lvl_point += 1
        self.score += 1
        print("To next lvl", self.lvl_point, "/ 20")

    def block_fits(self):
        tiles = self.current_block.get_cell_pos()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random()
        self.next_block = self.get_random()
        self.score = 0
        if self.music == 1:
            pygame.mixer.music.load("Sounds/music_A.wav")
        elif self.music == 2:
            pygame.mixer.music.load("Sounds/music_B.wav")
        elif self.music == 3:
            pygame.mixer.music.load("Sounds/music_C.wav")
        pygame.mixer.music.play(-1)

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rot()

    def block_inside(self):
        tiles = self.current_block.get_cell_pos()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        if self.game_over == True:
            pass
        else:
            self.grid.draw(screen)
            self.current_block.draw(screen, 21, 21)

            if self.next_block.id == 3:
                self.next_block.draw(screen, 285, 430)
            elif self.next_block.id == 4:
                self.next_block.draw(screen, 285, 410)
            else:
                self.next_block.draw(screen, 300, 410)