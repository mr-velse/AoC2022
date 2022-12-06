two_data = open("3", "r")
lines = two_data.readlines()

total = 0
badgeTotal = 0

trioIdx = 0
toCheck = []

for line in lines:
    length = len(line)
    half = int(length / 2)
    
    current = 0
    index = -1
    while index == -1:
        index = line.find(line[current], half)
        current = current + 1
    
    priority = ord(line[index])
    if line[index].islower():
        priority = priority - 96
    else:
        priority = priority - 38

    total += priority

    # badges

    if trioIdx == 0:
        toCheck = line
    else: # check the other two
        toRemove = []
        for badgeCandidate in toCheck:
            badgeCount = line.count(badgeCandidate)
            if badgeCount == 0:
                toRemove.append(badgeCandidate)
        for removeCandidate in toRemove:
            toCheck = toCheck.replace(removeCandidate, "")

    trioIdx += 1
    if trioIdx == 3:
        # should be one remaining
        badgePriority = ord(toCheck[0])
        if toCheck[0].islower():
            badgePriority -= 96
        else:
            badgePriority -= 38
        print(badgePriority)

        badgeTotal += badgePriority
        print(toCheck)
        trioIdx = 0
        toCheck = []



print(total)

print(badgeTotal)

two_data.close()