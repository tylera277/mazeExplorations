


from checkVicinity import checkTop, checkLeft, checkRight, checkBot

def ceaseCheck(board, agents, currentOrient):
    """
    Function which checks whether an agent should stop moving b/c its trapped
    """
    for i in range(len(agents)):

        # Running north into a cul-de-sac with three boxes on the top of one
        if currentOrient[i] == 'N' and checkLeft(board, agents[i]) == 1 and \
           checkTop(board, agents[i]) == 1 and checkRight(board, agents[i]) == 1:

            currentOrient[i] = 'O'

        # Running south into " "
        if currentOrient[i] == 'S' and checkLeft(board, agents[i]) == 1 and \
           checkBot(board, agents[i]) == 1 and checkRight(board, agents[i]) == 1:

            currentOrient[i] = 'O'

        # Running east into " "
        if currentOrient[i] == 'E' and checkBot(board, agents[i]) == 1 and \
           checkTop(board, agents[i]) == 1 and checkRight(board, agents[i]) == 1:

            currentOrient[i] = 'O'

        # Running west into " "
        if currentOrient[i] == 'W' and checkLeft(board, agents[i]) == 1 and \
           checkTop(board, agents[i]) == 1 and checkBot(board, agents[i]) == 1:

            currentOrient[i] = 'O'

    return currentOrient


def wallCheck(board, agents, currentOrient, numOfAgents):
    """
    Checks whether agent is running into a wall, if it is, it changes its direction, or stops
    it if there is no path in its orientation direction left.
    """

    for i in range(numOfAgents):

        if currentOrient[i] == 'S':
            if checkRight(board, agents[i]) == 0 and checkBot(board, agents[i]) == 0 and \
               checkTop(board, agents[i]) == 0:

                numOfAgents += 1
                agents[numOfAgents - 1] = agents[i]
                currentOrient[numOfAgents - 1] = 'S'
                currentOrient[i] = 'E'

            if checkBot(board, agents[i]) == 1:
                if checkRight(board, agents[i]) == 1 and checkLeft(board, agents[i]) == 1:
                    currentOrient[i] = 'O'  # cease condition; nowhere to go
                elif checkRight(board, agents[i]) == 1:
                    currentOrient[i] = 'W'  # redirection; its in a corner
                elif checkLeft(board, agents[i]) == 1:
                    currentOrient[i] = 'E'  # redirection; its in a corner
                else:
                    numOfAgents += 1
                    agents[numOfAgents - 1] = agents[i]
                    currentOrient[numOfAgents - 1] = 'W'
                    currentOrient[i] = 'E'


        if currentOrient[i] == 'N':

            if checkTop(board, agents[i]) == 1:
                if checkRight(board, agents[i]) == 1 and checkLeft(board, agents[i]) == 1:
                    currentOrient[i] = 'O'  # cease condition
                elif checkRight(board, agents[i]) == 1:
                    currentOrient[i] = 'W'  # redirection
                elif checkLeft(board, agents[i]) == 1:
                    currentOrient[i] = 'E'  # redirection
                else:
                    numOfAgents += 1
                    agents[numOfAgents-1] = agents[i]
                    currentOrient[numOfAgents-1] = 'E'
                    currentOrient[i] = 'W'


        if currentOrient[i] == 'W':



            if checkLeft(board, agents[i]) == 1:
                if checkTop(board, agents[i]) == 1 and checkBot(board, agents[i]) == 1:
                    currentOrient[i] = 'O'  # cease condition
                elif checkTop(board, agents[i]) == 1:
                    currentOrient[i] = 'S'  # redirection
                elif checkBot(board, agents[i]):
                    currentOrient[i] = 'N'  # redirection
                else:
                    numOfAgents += 1
                    agents[numOfAgents - 1] = agents[i]
                    currentOrient[numOfAgents - 1] = 'S'
                    currentOrient[i] = 'N'

        if currentOrient[i] == 'E':
            if checkBot(board, agents[i]) == 0 and checkRight(board, agents[i]) == 0 \
                    and checkLeft(board, agents[i]) == 0:
                numOfAgents += 1
                agents[numOfAgents - 1] = agents[i]
                currentOrient[numOfAgents - 1] = 'E'
                currentOrient[i] = 'S'
            if checkTop(board, agents[i]) == 0 and checkRight(board, agents[i]) == 0 \
                    and checkLeft(board, agents[i]) == 0:
                numOfAgents += 1
                agents[numOfAgents - 1] = agents[i]
                currentOrient[numOfAgents - 1] = 'E'
                currentOrient[i] = 'N'

            if checkRight(board, agents[i]) == 1:
                if checkTop(board, agents[i]) == 1 and checkBot(board, agents[i]) == 1:
                    currentOrient[i] = 'O'  # cease condition
                elif checkTop(board, agents[i]) == 1:
                    currentOrient[i] = 'S'  # redirection
                elif checkBot(board, agents[i]) == 1:
                    currentOrient[i] = 'N'  # redirection
                else:
                    numOfAgents += 1
                    agents[numOfAgents - 1] = agents[i]
                    currentOrient[numOfAgents - 1] = 'S'
                    currentOrient[i] = 'N'

    return currentOrient, numOfAgents