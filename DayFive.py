data = open("5", "r")
lines = data.readlines()

puzzleOne = ""
puzzleTwo = ""

crates = []

cratesParsed = False

for line in lines:
    # parse crates - crates are alpha, start at position  then every 4. columns are numeric.
    length = len(line)
    idx = 1
    crateColumn = 0
    if not cratesParsed:
        while idx < length:
            if len(crates) <= crateColumn: # first time through, create the stacks
                crates.append([])

            if line[idx].isalpha(): # crate
                crates[crateColumn][:0] = line[idx]
            elif line[idx].isnumeric(): #
                cratesParsed = True
            idx += 4
            crateColumn += 1
    else:
        # parse the moves
        commands = line.split()
        if len(commands) >= 6:
            # we actually only need to know [1] (quantity) [3] (origin) and [5] (destination)
            quantity = int(commands[1])
            src = int(commands[3]) - 1
            dest = int(commands[5]) - 1

            #for i in range(quantity):
            #    toMove = crates[src].pop()
            #    crates[dest].append(toMove)

            crates[dest] += crates[src][-quantity:]
            crates[src] = crates[src][:-quantity]

for c in crates:
    puzzleOne += c[-1]


print(puzzleOne)
print(puzzleTwo)

data.close()