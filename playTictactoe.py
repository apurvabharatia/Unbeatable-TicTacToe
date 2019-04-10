def movesLeft(grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == '_':
                return True
    return False

def evaluate(grid):
    for row in range(3):
        if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:
            if grid[row][0] == 'x':
                return 10
            elif grid[row][0] == 'o':
                return -10

    for col in range(3):
        if grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col]:
            if grid[0][col] == 'x':
                return 10
            elif grid[0][col] == 'o':
                return -10

    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        if grid[0][0] == 'x':
            return 10
        elif grid[0][0] == 'o':
            return -10

    if grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[0][2] == 'x':
            return 10
        elif grid[0][2] == 'o':
            return -10
    return 0


def minimax(grid, depth, minimizersMove):

    score = evaluate(grid)
    if score == 10:
        return score

    if score == -10:
        return score

    if not movesLeft(grid):
        return 0


    if minimizersMove:
        best = float('-inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] == '_':
                    grid[row][col] = 'x'
                    best = max(best, minimax(grid, depth + 1, not minimizersMove))
                    grid[row][col] = '_'
    else:
        best = float('inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] == '_':
                    grid[row][col] = 'o'
                    best = min(best, minimax(grid, depth + 1, not minimizersMove))
                    grid[row][col] = '_'
    return best

def findBestMove(grid):

    """ Traverse the grid and return result of minimax for each move """
    bestVal = float('-inf')
    bestMove = ['_', '_']
    for row in range(3):
        for col in range(3):
            if grid[row][col] == '_':
                grid[row][col] = 'x'
                currentMove = minimax(grid, 0, False)

                grid[row][col] = '_'
                if currentMove > bestVal:
                    bestMove[0] = row
                    bestMove[1] = col
                    bestVal = currentMove
    return bestMove

grid = [['_' for row in range(3)] for col in range(3)]
def printGrid():
    print(grid[0])
    print(grid[1])
    print(grid[2])


def askForOpponentsMove():
    print("Your move, human : ")
    opponentRowMove = input("Please enter row value (0, 1 or 2) ")
    opponentColMove = input("Please enter column value (0, 1 or 2) ")
    opponentRowMove = int(opponentRowMove)
    opponentColMove = int(opponentColMove)
    return opponentRowMove, opponentColMove

grid[0][0] = 'x'
printGrid()

while(True):
    opponentRowMove, opponentColMove = askForOpponentsMove()
    if grid[opponentRowMove][opponentColMove] != '_':
        print("Invalid move")
        opponentRowMove, opponentColMove = askForOpponentsMove()
    grid[opponentRowMove][opponentColMove] = 'o'
    printGrid()
    row, col = findBestMove(grid)
    grid[row][col] = 'x'
    print("\nMy move :")
    printGrid()
    if evaluate(grid) == 10:
        print("Game over!")
        printGrid()
        gameOver = True
        break
    print('\n')
