two_data = open("2", "r")
lines = two_data.readlines()

scores = {
    "A X" : 4, # Rock / Rock / Draw
    "A Y" : 8, # Rock / Paper / Win
    "A Z" : 3, # Rock / Scissors / Loss
    "B X" : 1, # Paper / Rock / Loss
    "B Y" : 5, # Paper / Paper / Draw
    "B Z" : 9, # Paper / Scissors / Win
    "C X" : 7, # Scissors / Rock / Win
    "C Y" : 2, # Scissors / Paper / Loss
    "C Z" : 6, # Scissors / Scissors / Draw
}

strategies = {
    "A X" : 3, # Rock / Lose (Scissors)
    "A Y" : 4, # Rock / Draw (Rock)
    "A Z" : 8, # Rock / Win (Paper)
    "B X" : 1, # Paper / Lose (Rock)
    "B Y" : 5, # Paper / Draw (Paper)
    "B Z" : 9, # Paper / Win (Scissors)
    "C X" : 2, # Scissors / Lose (Paper)
    "C Y" : 6, # Scissors / Draw (Scissors)
    "C Z" : 7, # Scissors / Win (Rock)
}

score = 0
strategy = 0
for line in lines:
    stripped = line.strip("\n") # get rid of any new lines
    score += scores[stripped]
    strategy += strategies[stripped]

print("Puzzle One: " + str(score))
print("Puzzle Two: " + str(strategy))

two_data.close()