
from PIL import Image

import numpy as np

def convertPic2Blocks(mazePictureFile):
    """
    This function takes in a picture of a maze and outputs a grid of blocks,
    equivalent to that maze.
    """

    mazePicture = Image.open('{}'.format(mazePictureFile))

    pixel_map = mazePicture.load()
    width, height = mazePicture.size

    horizontal = []
    vertical = []

    # +this cleans up the picture so that the color shades are either
    # completely black or completely white
    for i in range(width):
        for j in range(height):
            r, g, b, p = mazePicture.getpixel((i, j))

            if (r and g and b) > 240:
                pixel_map[i, j] = (255, 255, 255)

            elif (r and g and b) < 239:
                pixel_map[i, j] = (0, 0, 0)
                horizontal.append(i)
                vertical.append(j)

    # Determining the edges and corners of the maze
    leftEdge = min(horizontal)
    rightEdge = max(horizontal)

    topEdge = min(vertical)
    bottomEdge = max(vertical)

    #print(topEdge,bottomEdge)
    botLeftCorner = [leftEdge, bottomEdge]
    botRightCorner = [rightEdge, bottomEdge]




    blockPixelWidth = 90
    linePixelWidth = 15



    recreatedBlockMaze = np.zeros((15, 15))

    horizCount = 0

    for i in range(leftEdge+int(linePixelWidth/2), rightEdge+int(linePixelWidth/2), int(blockPixelWidth/2)):
        vertCount = 1
        horizCount += 1
        for j in range(topEdge+int(linePixelWidth/2), bottomEdge+int(linePixelWidth/2), int(blockPixelWidth/2)):
            r, g, b, p = mazePicture.getpixel((i, j))
            pixel_map[i, j] = (255, 0, 0)
            if (r and g and b) == 0:
                recreatedBlockMaze[vertCount][horizCount] = 1

            vertCount += 1

    mazePicture.show()

    return recreatedBlockMaze