from tools import tools_3
import numpy as np

def calculate(grid, maxdepth, alpha, beta, is_it_max):

    if maxdepth == 0:
        return tools_3.heuristic(grid)

    if not tools_3.canMove(grid):
        return tools_3.heuristic(grid)

    if is_it_max:
        value = -np.inf
        [successors, moving] = tools_3.getPossibleMoves(grid)
        for child in successors:
            value = max(value,calculate(child,maxdepth-1,alpha,beta,False))
            if value >= beta:
                return value
            alpha = max(alpha,value)
        return value

    else:
        cells = [i for i, x in enumerate(grid) if x == 0]
        successors = []

        for c in cells:
            gridcopy = list(grid)
            gridcopy[c]=2
            successors.append(gridcopy)
            gridcopy = list(grid)
            gridcopy[c]=4
            successors.append(gridcopy)
            value = np.inf

        for child in successors:
            value = min(value,calculate(child,maxdepth-1,alpha,beta,True))
            if value <= alpha:
                return value
            beta = min(beta,value)
        return value
