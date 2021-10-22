


def checkTop(board, pos):
    posX = pos[1]
    posY = pos[0]

    if board[posY - 1][posX] == 1:
        return 1
    else:
        return 0


def checkBot(board, pos):
    posX = pos[1]
    posY = pos[0]

    if board[posY + 1][posX] == 1:
        return 1
    else:
        return 0


def checkLeft(board, pos):
    posX = pos[1]
    posY = pos[0]

    if board[posY][posX - 1] == 1:
        return 1
    else:
        return 0


def checkRight(board, pos):
    posX = pos[1]
    posY = pos[0]

    if board[posY][posX + 1] == 1:
        return 1
    else:
        return 0