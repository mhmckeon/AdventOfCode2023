# Day 8
# Part 1
input = "input/day8.txt"
with open(input) as f:
    lines = f.read().split("\n")

directions = ""
directionTF = True
dictDirection = {}
for line in lines:
    if directionTF == False:
        location, LeftRight = line.split(" = ")
        Left, Right = LeftRight.strip("()").split(", ")
        dictDirection[location] = [Left, Right]
    else:
        if not line:
            directionTF = False
        else:
            directions += line

directions =directions.replace("R","1")
directions =directions.replace("L","0")
directionStore = directions

start = dictDirection["AAA"]
steps = 0
counter = 0
playGame = True
while playGame == True:
    counter += 1
    if counter == 10000000:
        print("broken")
        break
    for direction in directions:
        if start[0] == "ZZZ" and direction == "0":
            print(steps+1)
            playGame = False
            break
        if start[1] == "ZZZ" and direction == "1":
            print(steps+1)
            playGame = False
            break
        if direction == "0":
            start = dictDirection[start[0]]
        else:
            start = dictDirection[start[1]]
        steps += 1



# Part 2 - incomplete

dictKeys = dictDirection.keys()
newStarts = [dictDirection[key] for key in dictKeys if key[2] == "A"]
print(newStarts)

newStarts = newStarts[4:5]

counter = 0
steps = 0
endCount = 0


counter = 0
import time
start = time.time()

playGame = True
while playGame == True:
    for direction in directions:
        if endCount == len(newStarts):
            print("final steps",steps)
            playGame = False
            break
        endCount = 0
        for index, newStart in enumerate(newStarts):
            # if newStart[0][2] == "Z" and direction == "0":
            #     endCount += 1
            if newStart[1][2] == "Z" and direction == "1":
                endCount +=  1
            if direction == "0":
                newStarts[index] = dictDirection[newStart[0]]
            else:
                newStarts[index] = dictDirection[newStart[1]]
        steps += 1
        counter += 1
        
end = time.time()

print(time.time()- start)

timer = (end - start) / 60 / 60
print(timer)

# 0 = 20777
# 1 = 19199
# 2 = 18673
# 3 = 16043
# 4 = 12361
# 5 = 15517
numbers = [20777, 19199, 18673, 16043, 12361, 15517]

#LCM calculator
