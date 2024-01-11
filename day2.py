# Day 2 
import re

input = "input/day2.txt"

with open(input) as f:
    lines = f.read().split("\n")

testinput = []
input = []
currentList = input

# Splits the input into two lists
option2 = False
for line in lines:
    if option2 != False:
        input.append(line)
    else:
        if line == "input":
            option2 = True
            continue
        testinput.append(line)



# Part 1
total = 0
totalAllowed = {"red":12, "green":13, "blue":14}

for line in currentList:
    game = line.split(":")
    game, sets = int(game[0][4:]), game[1].split(";")
    addToTotal = True
    for item in sets:
        item = item.split(", ")
        for word in item:
            tempword = re.sub('\d', '', word).strip()
            if tempword in list(totalAllowed.keys()):
                if totalAllowed[tempword] < int(re.sub("\D", "", word)):
                    addToTotal = False
                    break
    if addToTotal == True:
        total += game

print(total)

# Part 2
total = 0

for line in currentList:
    totalAllowed = {"red":1, "green":1, "blue":1}
    game = line.split(":")
    game, sets = int(game[0][4:]), game[1].split(";")
    for item in sets:
        item = item.split(", ")
        for word in item:
            tempword = re.sub('\d', '', word).strip()
            if tempword in list(totalAllowed.keys()):
                if totalAllowed[tempword] < int(re.sub("\D", "", word)):
                    totalAllowed[tempword] = int(re.sub("\D", "", word))
    
    total += (totalAllowed["red"]*totalAllowed["green"]*totalAllowed["blue"])

print(total)