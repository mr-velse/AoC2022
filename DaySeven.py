data = open("7", "r")
lines = data.readlines()

space = 70000000
req = 30000000
used = 0

puzzleOne = 0
puzzleTwo = 0

level = 0
folders = {}
current = ["/"]

folders[current[-1]] = 0

for line in lines:
    tokens = line.split()
    if tokens[0].isnumeric():
        used += int(tokens[0])

toFree = req - (space - used)

# find the smallest folder bigger than toFree
puzzleTwo = used # i.e. everything
    
for line in lines:
    # as we descend the tree, we build a dictionary of folders and accumulate the size of them
    # once we ascend, we can determine if they meet the criteria (puzzle one, under size 100000)
    tokens = line.split()

    if tokens[0] == "$": # command
        if tokens[1] == "cd": # change direction
            if tokens[2] == "..": # up
                folderSpace = folders[current[-1]]
                if folderSpace < puzzleTwo and folderSpace > toFree:
                    puzzleTwo = folderSpace

                if folderSpace < 100000:
                    puzzleOne += folders[current[-1]]

                folders.pop(current[-1]) # remove last item
                current.pop()
                level -= 1
            elif tokens[2] == "/": # top
                level = 0
            else: # enter a folder
                level += 1
                current.append(current[-1] + tokens[2] + "/")
                folders[current[-1]] = 0
    elif tokens[0].isnumeric(): # file
        for folder in folders: # add this file amount to all folders in scope
            folders[folder] += int(tokens[0])

for folder in folders: # check any folders not popped for deletion candidacy (puzzle two)
    folderSpace = folders[folder]
    if folderSpace < puzzleTwo and folderSpace >= toFree:
        puzzleTwo = folderSpace

print(puzzleOne)
print(puzzleTwo)

data.close()