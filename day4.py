# Day 4
# Part 1
input = "input/day4.txt"

with open(input) as f:
    lines = f.read().split("\n")

total = 0

for line in lines:
    numbers = line.split(":")[1].split("|")
    winningNum = numbers[0].split()
    ownNums = numbers[1].split()
    tempTotal = 0
    for number in winningNum:
        if number in ownNums and tempTotal == 0:
            tempTotal += 1
        elif number in ownNums:
            tempTotal *= 2
    
    total += tempTotal

print(total)

# Part 2

scratchDict = {}
for line in lines:
    cardNums, numbers = line.split(":")
    cardNums = int(cardNums.split()[1])
    winningNum, ownNums = numbers.split("|")
    winningNum = winningNum.split()
    ownNums = ownNums.split()
    tempTotal = 0
    for number in winningNum:
        if number in ownNums:
            tempTotal += 1
    scratchDict[cardNums] = tempTotal

print(scratchDict)

totalCards = [1]

for key in scratchDict:
    print(totalCards)
    print("key:",key)
    for x in range(scratchDict[key]):
        print("key +x:", key+x)
        if len(totalCards) > key+x:
            print("num to add:", totalCards[key-1])
            print("in")
            totalCards[key+x] += totalCards[key-1]

        else:
            print("out")
            print("length:", len(totalCards))
            print(key-1)
            print("num to add:", totalCards[key-1]+1)
            totalCards.append(totalCards[key-1]+1)
    if scratchDict[key] == 0 and len(totalCards) <= key:
        totalCards.append(1)

while len(totalCards) > len(lines):
    totalCards.pop()
        

print(totalCards)
print(sum(totalCards))

print(scratchDict)

# ans: 8736439 - too high