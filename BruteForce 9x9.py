





def displayGrid(grid):
    for i in range(9):
        print (grid[i])
    

def findEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row,col
    return None

def isValid(grid, value, row, col):
    for i in range(9):
        if grid[row][i] == value:
            return False
    
    for i in range(9):
        if grid[i][col] == value:
            return False
    
    squareRow = row - row % 3
    squareCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + squareRow][j + squareCol] == value:
                return False
    
    return True

def solveGrid(grid):
    check = findEmpty(grid)
    if not check:
        displayGrid(grid)
        return True
    else:
        row, col = check
    
    for i in range (9):
        if isValid(grid, i+1, row, col):
            grid[row][col] = i+1

            if solveGrid(grid):
                return True
            
            grid[row][col] = 0
    
    return False

    



initialGrid = [[0, 0, 8, 2, 0, 0, 9, 0, 3],
              [3, 4, 2, 0, 9, 5, 0, 0, 7],
              [1, 9, 7, 0, 0, 0, 0, 0, 4],
              [0, 0, 5, 3, 1, 2, 4, 7, 9],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [2, 0, 0, 0, 7, 4, 5, 0, 0],
              [0, 2, 0, 0, 0, 1, 0, 0, 5],
              [0, 7, 0, 0, 0, 6, 8, 9, 1],
              [8, 0, 0, 4, 3, 0, 7, 0, 6]]

print("Initial Grid")
displayGrid(initialGrid)
print()
print("Solved Grid")
solveGrid(initialGrid)