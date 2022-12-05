one_data = open("1", "r")
lines = one_data.readlines()

runningCalories = 0
mostCalories = 0
second = 0
third = 0

for line in lines:
    if line == "\n":
        if runningCalories > mostCalories:
            third = second
            second = mostCalories
            mostCalories = runningCalories # new winner
        elif runningCalories > second:
            third = second
            second = runningCalories
        elif runningCalories > third:
            third = runningCalories
        
        runningCalories = 0 # reset this
    else:
        number = int(line)
        runningCalories += number

print(mostCalories)
print(mostCalories + second + third)

one_data.close()