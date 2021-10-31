

from makeBoard import makeGrid
from checkVicinity import checkTop, checkBot, checkRight, checkLeft
from mazePicture import convertPic2Blocks
from positionChecks import wallCheck

from PIL import Image


picture = 'simpleMaze1.png'
board = convertPic2Blocks(picture)





import numpy as np
startPoint = [4, 1]
endPoint = [10, 12]

agents = np.zeros((20, 2))

moveNum = np.zeros((100, 1))
currentOrient = np.zeros((100, 1), dtype='str')

agents[0][0] = int(startPoint[0])
agents[0][1] = int(startPoint[1])
moveNum[1] = 0

numbOfAgents = 1
status = 0

print(board)
#print(endPoint)

currentOrient[0] = 'E'
k=0
while True:
#while k < 15:


    status = 0

    # +Checks whether agent is running into a wall, if it is, it changes its direction, or stops
    # it if there is no path in its orientation direction left.
    currentOrient, numbOfAgents = wallCheck(board, agents, currentOrient, numbOfAgents)

    for i in range(numbOfAgents+1):

        if agents[i][0] == endPoint[0] and agents[i][1] == endPoint[1]:
            print('End Of Maze Reached')
            exit()


        # safeguard to stop agents from running past boundaries; will get rid of soon
        if agents[i][0] <= 0 or agents[i][0] >= 14:
            currentOrient[i]= 'O'
        if agents[i][1] <= 0 or agents[i][1] >= 14:
            currentOrient[i] = 'O'




        # Depending on the agents orientation, this moves it one block in that direction.
        # Or if orientation = 'O', it doesnt move the agent.
        if currentOrient[i] == 'N':
            agents[i][0] -= 1
        if currentOrient[i] == 'E':
            agents[i][1] += 1
        if currentOrient[i] == 'S':
            agents[i][0] += 1
        if currentOrient[i] == 'W':
            agents[i][1] -= 1
        if currentOrient[i] == 'O':
            pass



    k += 1

    print(agents[0], agents[1], agents[2],agents[3],agents[4],agents[5],agents[6],agents[7],agents[8],agents[9])




