data = open("4", "r")
lines = data.readlines()

puzzleOne = 0
puzzleTwo = 0

for line in lines:
    pairs = line.split(",")
    elfOne = pairs[0].split("-") # how to turn these into ints at this stage?
    elfTwo = pairs[1].split("-")

    elfOneMin = int(elfOne[0])
    elfOneMax = int(elfOne[1])
    elfTwoMin = int(elfTwo[0])
    elfTwoMax = int(elfTwo[1])

    if elfOneMin <= elfTwoMin and elfOneMax >= elfTwoMax:
        puzzleOne += 1
    elif elfTwoMin <= elfOneMin and elfTwoMax >= elfOneMax:
        puzzleOne += 1

    if elfOneMin > elfTwoMax:
        continue
    if elfTwoMin > elfOneMax:
        continue
    if elfOneMax < elfTwoMin:
        continue
    if elfTwoMax < elfOneMin:
        continue

    puzzleTwo += 1

print(puzzleOne)
print(puzzleTwo)

data.close()