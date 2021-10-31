


def checkTop(board, pos):
    posX = int(pos[1])
    posY = int(pos[0])

    if board[posY - 1][posX] == 1:
        return 1
    else:
        return 0


def checkBot(board, pos):
    posX = int(pos[1])
    posY = int(pos[0])

    if board[posY + 1][posX] == 1:
        return 1
    else:
        return 0


def checkLeft(board, pos):
    posX = int(pos[1])
    posY = int(pos[0])

    if board[posY][posX - 1] == 1:
        return 1
    else:
        return 0


def checkRight(board, pos):
    posX = int(pos[1])
    posY = int(pos[0])

    if board[posY][posX + 1] == 1:
        return 1
    else:
        return 0