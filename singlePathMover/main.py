

from makeBoard import makeGrid
from checkVicinity import checkTop, checkBot, checkRight, checkLeft

#wires = [[1, 0, 1, 3], [3, 1, 3, 2], [4, 1, 4, 3], [4, 2, 4, 4],
         #[1, 3, 3, 3], [2, 1, 7, 1], [2, 2, 7, 2], [5, 3, 8, 3]]

#grid = [4, 8]
grid = [5, 3]
wires = [[1,0,1,3],
         [2,1,2,5]]
# this makes the board
board = makeGrid(grid, wires)




print(board)


def electricField(grid, wires):
    startPoint = [2, 2]
    endPoint = [2 * grid[0], 2 * grid[1]]
    

    robotPositionX = startPoint[0]
    robotPositionY = startPoint[1]
    moveNum = 0

    #print(endPoint)
    pos = [robotPositionY, robotPositionX]

    currOrient = 'N'
    if checkRight == 1:
        currOrient = 'S'
    elif checkBot == 1:
        currOrient = 'E'

    while True:

        if (robotPositionY == endPoint[0] and robotPositionX == endPoint[1]):
            return False

        pos = [robotPositionY, robotPositionX]

        if currOrient == 'S':
            if checkBot(board, pos) == 1:
                if checkRight(board, pos) == 1:
                    currOrient = 'W'
                else:
                    currOrient = 'E'

        if currOrient == 'N':
            if checkTop(board, pos) == 1:
                if checkRight(board, pos) == 1:
                    currOrient = 'W'
                else:
                    currOrient = 'E'

        if currOrient == 'W':
            if checkLeft(board, pos) == 1:
                if checkTop(board, pos) == 1:
                    currOrient = 'S'
                else:
                    currOrient = 'N'

        if currOrient == 'E':
            if checkRight(board, pos) == 1:
                if checkTop(board, pos) == 1:
                    currOrient = 'S'
                else:
                    currOrient = 'N'





        if currOrient == 'N':
            robotPositionY -= 1
        if currOrient == 'E':
            robotPositionX += 1
        if currOrient == 'S':
            robotPositionY += 1
        if currOrient == 'W':
            robotPositionX -= 1



        print(pos)
        #print(checkBot(board, pos))
        moveNum += 1
        #return(moveNum/2)


electricField(grid, wires)


