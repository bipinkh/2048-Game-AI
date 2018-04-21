import time
from random import randint

from tools.ComputerAI_3 import ComputerAI
from tools.Displayer_3 import Displayer
from tools.PlayerAI_3 import PlayerAI

from tools.Grid_3 import Grid

defaultInitialTiles = 2     # number of numbered tiles in the beginning
defaultProbability = 0.9

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(PLAYER_TURN, COMPUTER_TURN) = (0, 1)

# Time Limit Before Losing
timeLimit = 1.0
allowance = 0.05

class GameManager:
    def __init__(self, size = 4):
        self.grid = Grid(size)                  #initializes board
        self.possibleNewTiles = [2, 4]          #possible values for new tiles
        self.probability = defaultProbability
        self.initTiles  = defaultInitialTiles   #default number of starting tiles
        self.computerAI = None                  #move for computerAI
        self.playerAI   = None                  #move for playerAI
        self.displayer  = None
        self.over       = False                 #game status

    def setComputerAI(self, computerAI):
        self.computerAI = computerAI

    def setPlayerAI(self, playerAI):
        self.playerAI = playerAI

    def setDisplayer(self, displayer):
        self.displayer = displayer

    def updateAlarm(self, currTime):
        if currTime - self.prevTime > timeLimit + allowance:
            print("time out :", currTime - self.prevTime)
            self.over = True
        else:
            while time.clock() - self.prevTime < timeLimit + allowance:
                pass

            self.prevTime = time.clock()

    def start(self):
        for i in range(self.initTiles):
            self.insertRandonTile()     #initialize board with 2 random numbered tiles

        self.displayer.display(self.grid)

        # Player AI Goes First
        turn = PLAYER_TURN
        maxTile = 0         #maximum tileValue

        self.prevTime = time.clock()

        # loop until there is possible chance of tile movement and player/computer is not over

        while not self.isGameOver() and not self.over:
            # Copy to Ensure AI Cannot Change the Real Grid to Cheat
            gridCopy = self.grid.clone()

            move = None

            if turn == PLAYER_TURN:
                print("Player's Turn:", end="")
                move = self.playerAI.getMove(gridCopy)
                print(actionDic[move])

                # Validate Move
                if move != None and move >= 0 and move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                        # Update maxTile
                        maxTile = self.grid.getMaxTile()
                    else:
                        print("Invalid PlayerAI Move")
                        self.over = True
                else:
                    print("Invalid PlayerAI Move - 1")
                    self.over = True
            else:
                print("Computer's turn:")
                move = self.computerAI.getMove(gridCopy)

                # Validate Move
                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid Computer AI Move")
                    self.over = True

            if not self.over:
                self.displayer.display(self.grid)

            # Exceeding the Time Allotted for Any Turn Terminates the Game
            self.updateAlarm(time.clock())
            turn = 1 - turn

        print(maxTile)

    def isGameOver(self):
        return not self.grid.canMove()

    def getNewTileValue(self):      #based on probabaility, say either 2 or 4
        if randint(0,99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1];

    def insertRandonTile(self):
        tileValue = self.getNewTileValue()             # filling value : 2 or 4
        cells = self.grid.getAvailableCells()          # all empty cells
        cell = cells[randint(0, len(cells) - 1)]       # choose any cell at random
        self.grid.setCellValue(cell, tileValue)        # place the tileValue

def main():
    gameManager = GameManager()
    playerAI  	= PlayerAI()
    computerAI  = ComputerAI()
    displayer 	= Displayer()

    gameManager.setDisplayer(displayer)
    gameManager.setPlayerAI(playerAI)
    gameManager.setComputerAI(computerAI)

    gameManager.start()

if __name__ == '__main__':
    main()
