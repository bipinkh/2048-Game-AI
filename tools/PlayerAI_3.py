
from tools.BaseAI_3 import BaseAI
from tools import minmax_3
from tools.Grid_3 import Grid
import numpy as np
from tools import tools_3

class PlayerAI(BaseAI):

        def getMove(self, grid):
                board = []
                for i in range(4):
                        board.extend(grid.map[i])
                [successors,moving] = tools_3.getPossibleMoves(board)
                pathcost = -np.inf
                direction = 0
                print (len(successors),len(moving))
                for i in range(len(successors)):
                        successor = successors[i]
                        move = moving[i]
                        maxVal = -np.inf
                        selection = 2
                        if selection == 2:
                            maxdepth = 4
                            maxVal = minmax_3.calculate(successor, maxdepth, -np.inf, np.inf, False)
                            if move == 0 or move == 2:
                                maxVal += 10000
                            print (maxVal,successor,move)
                        if maxVal > pathcost:
                            direction = move
                            pathcost = maxVal
                return direction

if __name__ == '__main__':
        # create instance
        player = PlayerAI()
        # get grid
        grid=Grid()
        #assign initial grid values
        grid.map[0][0] = 2
        grid.map[1][0] = 2
        grid.map[3][0] = 4
        #let's rock the hyperloop
        while True:
                v = player.getMove(grid)
                grid.move(v)



