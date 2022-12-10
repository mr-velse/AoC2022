def needsMove(t1, t2):
    diffx = abs(t1[0] - t2[0])
    diffy = abs(t1[1] - t2[1])
    return diffx > 1 or diffy > 1

def resolveMove(t1, t2):
    if needsMove(t1, t2):
        dx = t1[0] - t2[0]
        dy = t1[1] - t2[1]
        diffx = abs(t1[0] - t2[0])
        diffy = abs(t1[1] - t2[1])
        if diffx == diffy:
            addx = int(dx / diffx)
            addy = int(dy / diffy)
            return (t2[0] + addx, t2[1] + addy)
        elif diffx > diffy: # take t1's y and move towards in x
            if dx > 0:
                return (t2[0] + 1, t1[1])
            else:
                return (t2[0] - 1, t1[1])
        else:
            if dy > 0:
                return (t1[0], t2[1] + 1)
            else:
                return (t1[0], t2[1] - 1)  
    return t2

def simulate(items, knots):
    tails = []
    tails.append((0,0))

    rope = []

    for k in range(knots):
        rope.append((0,0))

    for i in items:
        match i[0]:
            case "U":
                for x in range(i[1]):
                    rope[0] = (rope[0][0], rope[0][1] + 1) # adjust pos for direction
                    current = rope[0]
                    for t in range(1, knots):
                        rope[t] = resolveMove(current, rope[t])
                        current = rope[t]
                    tails.append(rope[-1])
            case "D":
                for x in range(i[1]):
                    rope[0] = (rope[0][0], rope[0][1] - 1)
                    current = rope[0]
                    for t in range(1, knots):
                        rope[t] = resolveMove(current, rope[t])
                        current = rope[t]
                    tails.append(rope[-1])
            case "L":
                for x in range(i[1]):
                    rope[0] = (rope[0][0] - 1, rope[0][1])
                    current = rope[0]
                    for t in range(1, knots):
                        rope[t] = resolveMove(current, rope[t])
                        current = rope[t]
                    tails.append(rope[-1])
            case "R":
                for x in range(i[1]):
                    rope[0] = (rope[0][0] + 1, rope[0][1])
                    current = rope[0]
                    for t in range(1, knots):
                        rope[t] = resolveMove(current, rope[t])
                        current = rope[t]
                    tails.append(rope[-1])
    return len(set(tails))

data = open("9", "r")
lines = data.readlines()

puzzleOne = 0
puzzleTwo = 0

items = []

for line in lines:
    l = line.split()
    items.append((l[0], int(l[1])))

puzzleOne = simulate(items, 2) 
puzzleTwo = simulate(items, 10)  

print(puzzleOne)
print(puzzleTwo)

data.close()