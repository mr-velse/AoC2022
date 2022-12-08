data = open("8", "r")
lines = data.readlines()

puzzleOne = 0
puzzleTwo = 0

grid = []

maxRow = 0
maxCol = 0

for line in lines:
    grid.append([])
    
    for c in line:
        if c.isnumeric():
            grid[-1].append(int(c))
    
maxRow = len(grid[0])
maxCol = len(grid)

for x in range(maxRow):
    for y in range(maxCol):
        scenic = 0
        currentScenic = 0
        incPuzzleOne = False

        # so for each x/y cord we must go up/down/left/right until we go out of bounds or find a taller tree
        val = grid[x][y]
        # as soon as it is visible, we increment the visible counter and exit
        visible = True
        for xi in range(x + 1, maxRow): # right
            scenic += 1 # initially just increment this
            if grid[xi][y] >= val:
                visible = False
                break
        if visible == True:
            incPuzzleOne = True

        visible = True
        for xi in range(x - 1, -1, -1): # left
            currentScenic += 1 # then use thus temporary version
            if grid[xi][y] >= val:
                visible = False
                break
        if visible == True:
            incPuzzleOne = True
        scenic *= currentScenic
        currentScenic = 0
        
        visible = True
        for yi in range(y + 1, maxCol): # down
            currentScenic += 1 # then use thus temporary version
            if grid[x][yi] >= val:
                visible = False
                break
        if visible == True:
            incPuzzleOne = True
        scenic *= currentScenic
        currentScenic = 0

        visible = True
        for yi in range(y - 1, -1, -1): # up
            currentScenic += 1 # then use thus temporary version
            if grid[x][yi] >= val:
                visible = False
                break
        if visible == True:
            incPuzzleOne = True
        scenic *= currentScenic
        
        if incPuzzleOne == True:
            puzzleOne += 1
        if scenic > puzzleTwo:
            puzzleTwo = scenic

print(puzzleOne)
print(puzzleTwo)

data.close()