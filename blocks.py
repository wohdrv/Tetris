from block import Block
from pos import Pos

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Pos(0, 2), Pos(1, 0), Pos(1, 1), Pos(1, 2)],
            1: [Pos(0, 1), Pos(1, 1), Pos(2, 1), Pos(2, 2)],
            2: [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(2, 0)],
            3: [Pos(0, 0), Pos(0, 1), Pos(1, 1), Pos(2, 1)]
        }
        self.move(0, 3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Pos(0, 0), Pos(1, 0), Pos(1, 1), Pos(1, 2)],
            1: [Pos(0, 1), Pos(0, 2), Pos(1, 1), Pos(2, 1)],
            2: [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(2, 2)],
            3: [Pos(0, 1), Pos(1, 1), Pos(2, 0), Pos(2, 1)]
        }
        self.move(0, 3)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(1, 3)],
            1: [Pos(0, 2), Pos(1, 2), Pos(2, 2), Pos(3, 2)],
            2: [Pos(2, 0), Pos(2, 1), Pos(2, 2), Pos(2, 3)],
            3: [Pos(0, 1), Pos(1, 1), Pos(2, 1), Pos(3, 1)]
        }
        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Pos(0, 0), Pos(0, 1), Pos(1, 0), Pos(1, 1)]
        }
        self.move(0, 4)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Pos(0, 1), Pos(0, 2), Pos(1, 0), Pos(1, 1)],
            1: [Pos(0, 1), Pos(1, 1), Pos(1, 2), Pos(2, 2)],
            2: [Pos(1, 1), Pos(1, 2), Pos(2, 0), Pos(2, 1)],
            3: [Pos(0, 0), Pos(1, 0), Pos(1, 1), Pos(2, 1)]
        }
        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Pos(0, 1), Pos(1, 0), Pos(1, 1), Pos(1, 2)],
            1: [Pos(0, 1), Pos(1, 1), Pos(1, 2), Pos(2, 1)],
            2: [Pos(1, 0), Pos(1, 1), Pos(1, 2), Pos(2, 1)],
            3: [Pos(0, 1), Pos(1, 0), Pos(1, 1), Pos(2, 1)]
        }
        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Pos(0, 0), Pos(0, 1), Pos(1, 1), Pos(1, 2)],
            1: [Pos(0, 2), Pos(1, 1), Pos(1, 2), Pos(2, 1)],
            2: [Pos(1, 0), Pos(1, 1), Pos(2, 1), Pos(2, 2)],
            3: [Pos(0, 1), Pos(1, 0), Pos(1, 1), Pos(2, 0)]
        }
        self.move(0, 3)