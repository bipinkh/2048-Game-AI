#AI of computer
# for simplicity Computer AI is kept so dumb that it will select a random cell for Move from all available empty cells

from random import randint

from tools.BaseAI_3 import BaseAI


class ComputerAI(BaseAI):
    def getMove(self, grid):
        cells = grid.getAvailableCells()

        return cells[randint(0, len(cells) - 1)] if cells else None
