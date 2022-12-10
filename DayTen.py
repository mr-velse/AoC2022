data = open("10", "r")
lines = data.readlines()

puzzleOne = 0
puzzleTwo = ""

X = 1 # register
commands = []

for line in lines:
    l = line.split()
    if l[0] == "noop":
        commands.append([l[0]])
    else:
        commands.append([l[0], int(l[1])])

clock = 0

canExecute = True
pipeline = [] 
while canExecute:
    # add a command to the pipeline
    if len(commands) > 0 and len(pipeline) == 0:
        command = commands[0]
        commands = commands[1:] # remove first command from list
        if command[0] == "noop":
            pipeline.append([command, 1])
        else:
            pipeline.append([command, 2])

    scanline = []
    for i in range(40):
        scanline.append('.')
    for i in range(X - 1, X + 2):
        if i < 40 and i >= 0:
            scanline[i] = '#'
    modclock = clock % 40
    if modclock == 0:
        puzzleTwo += "\n"
    puzzleTwo += scanline[modclock]

    clock += 1 # at this point we end the cycle

    match clock: # 'during' is key here. calculate this before resolving command
        case 20:
            puzzleOne += (20 * X)
        case 60:
            puzzleOne += (60 * X)
        case 100:
            puzzleOne += (100 * X)
        case 140:
            puzzleOne += (140 * X)
        case 180:
            puzzleOne += (180 * X)
        case 220:
            puzzleOne += (220 * X)

    # decrement all commands in pipeline
    for p in pipeline:
        p[1] = p[1] - 1
        if p[1] == 0:
            if p[0][0] == "addx": # add
                X += p[0][1]
    
    pipeline = [p for p in pipeline if p[1] != 0] # remove any entries with a pipeline val of 0
    canExecute = len(pipeline) > 0 or len(commands) > 0

print(puzzleOne)
print(puzzleTwo)

data.close()