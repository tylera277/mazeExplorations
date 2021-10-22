def makeGrid(grid, wires):
    import numpy as np

    coordInBoxes = np.zeros((len(wires), 4))
    fieldY = (2 * grid[0]) + 2
    fieldX = (2 * grid[1]) + 2
    playingField = np.zeros((fieldY, fieldX))

    for i in range(len(wires)):
        x1b = (2 * wires[i][0]) + 1
        y1b = (2 * wires[i][1]) + 1
        x2b = (2 * wires[i][2]) + 1
        y2b = (2 * wires[i][3]) + 1

        coordInBoxes[i] = [x1b, y1b, x2b, y2b]
    #print(coordInBoxes)

    # trying to mark off the unpassable areas
    # for j in range(len(coordInBoxes)):
    print('yep:', int(coordInBoxes[1][0]))

    for j in range(len(coordInBoxes)):
        x1b_ = int(coordInBoxes[j][0])
        y1b_ = int(coordInBoxes[j][1])
        x2b_ = int(coordInBoxes[j][2])
        y2b_ = int(coordInBoxes[j][3])

        if x1b_ != x2b_:
            for k in range(x1b_, x2b_ + 1):
                playingField[y1b_][k] = 1
        if y1b_ != y2b_:
            for l in range(y1b_, y2b_ + 1):
                playingField[l][x1b_] = 1

        # top and bottom horizontal
        for m in range(0, fieldX):
            playingField[0][m] = 1
            playingField[1][m] = 1
            playingField[fieldY - 1][m] = 1

        for n in range(0, fieldY - 1):
            playingField[n][0] = 1
            playingField[n][1] = 1
            playingField[n][fieldX - 1] = 1

    return playingField