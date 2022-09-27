# Tile 1: ■
# Tile 2: □
import imp
import random
from colorama import Fore, Back, Style

# Reference:
# print(Fore.RED + '■')
# print(Fore.BLUE + '■')
# print(Fore.YELLOW + '■')
# print(Style.RESET_ALL)
# print('back to normal now')

class Board:
    def __init__(self, width, height):
        self.board = []
        self.randomized = False
        self.width = width
        self.height = height
        
        array = []
        for x in range(height):
            row = []
            for y in range(width):
                row.append("■")
            array.append(row)
        self.board = array
        
    def regenerateBoard(self):        
        array = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append("■")
            array.append(row)
        self.board = array
    
    def sortData(self, startingPoints, x, y):
        for element in startingPoints:
            if element['x'] == x and element['y'] == y:
                return False
            else:
                pass
        return True
    
    def randomize(self, numOfElements = 3, baseStartingPoints = 1):
        elements = ["A", "B", "C", "D", "E", "F", ""]
        self.randomized = True
        
        if numOfElements > len(elements):
            raise Exception("Board can only at max have " + str(len(elements)) + " elements!")
        else:
            startingPoints = []

            #choose some starting points
            numOfStartingPoints = numOfElements * baseStartingPoints
            for item in range(numOfStartingPoints):
                while True:
                    x = random.randint(0, self.width-1)
                    y = random.randint(0, self.height-1)

                    if(self.sortData(startingPoints, x, y)):
                        startingPoints.append({'x': x, 'y': y})
                        break
                    
            #set those starting points
            for index, item in enumerate(startingPoints):
                index = index % numOfElements
                self.board[item['y']][item['x']] = elements[index]
                        
            #start filling the rest of the board
            slotsLeft = self.width * self.height - numOfStartingPoints
            
            targetIndex = 0

            for x in range(1000):
                for yCoord in range(len(self.board)):
                    for xCoord in range(len(self.board[yCoord])):
                        direction = random.randint(1,4)
                        if self.board[yCoord][xCoord] == elements[targetIndex]:
                            if direction == 1 and self.testSpot(yCoord-1, xCoord, elements[targetIndex]):
                                slotsLeft-=1
                                targetIndex+=1
                            if direction == 2 and self.testSpot(yCoord+1, xCoord, elements[targetIndex]):
                                slotsLeft-=1
                                targetIndex+=1
                            if direction == 3 and self.testSpot(yCoord, xCoord-1, elements[targetIndex]):
                                slotsLeft-=1
                                targetIndex+=1
                            if direction == 4 and self.testSpot(yCoord, xCoord+1, elements[targetIndex]):
                                slotsLeft-=1
                                targetIndex+=1
                            
                            if targetIndex == numOfElements:
                                targetIndex = 0
                        if targetIndex == numOfElements:
                                targetIndex = 0
                        else:
                            targetIndex += 1
            
            if slotsLeft != 0:
                self.regenerateBoard()
                self.randomize(numOfElements)                
    
    def testSpot(self, rowIndex, itemIndex, token):
        try:
            if self.board[rowIndex][itemIndex] == "■":
                self.board[rowIndex][itemIndex] = token
                return True
            else:
                return False
        except:
            return False
    
    def displayBoard(self):
        if not self.randomized:
            raise Exception("Board must be randomized before being displayed!")
        else:
            for row in self.board:
                for item in row:
                    color = ""
                    if item == "A":
                        color = Fore.RED
                    elif item == "B":
                        color = Fore.BLUE
                    elif item == "C":
                        color = Fore.GREEN
                    elif item == "D":
                        color = Fore.YELLOW
                    elif item == "E":
                        color = Fore.CYAN
                    elif item == "F":
                        color = Fore.MAGENTA
                    else:
                        color = Fore.RED
                    print(color + "▉▉", end="")
                print("")
            print(Style.RESET_ALL)
            

board = Board(25, 25)
board.randomize(6, 4)
board.displayBoard()