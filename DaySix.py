data = open("6", "r")
lines = data.readlines()

puzzleOne = 0
puzzleTwo = 0

stream = ""

for line in lines: # only one but who cares
    for character in line:
        puzzleOne += 1
        stream += character
        if len(stream) == 4:
            if len(set(stream)) == 4:
                break
            else:
                stream = stream[-3:]
    
    stream = ""
    
    for character in line:
        puzzleTwo += 1
        stream += character
        if len(stream) == 14:
            if len(set(stream)) == 14:
                break
            else:
                stream = stream[-13:]

print(puzzleOne)
print(puzzleTwo)

data.close()