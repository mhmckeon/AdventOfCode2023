# Day 1 Part 1

import string
import re

input = "input/day1.txt"

with open(input) as f:
    lines = f.read().split("\n")

# lines = ["1abc2",
# "pqr3stu8vwx",
# "a1b2c3d4e5f",
# "treb7uchet"]


listOfNumbers = []

for line in lines:
    revline = line[::-1]
    numBeginning = line.lstrip(string.ascii_letters)[0]
    numEnding = revline.lstrip(string.ascii_letters)[0]
    listOfNumbers.append(int(numBeginning+numEnding))
    
print(sum(listOfNumbers))

# Day 1 Part 2
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dictNumber = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}


# lines = ["two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2",
# "zoneight234",
# "7pqrstsixteen"]
# ["98nine8", 
# "53zsvpqnrjtwo5nine5nrdvmg", 
# "54twofive19five4",
# "2one2",
# "1"] 

print(lines[0])
total = 0
listOfNumbers = []
for line in lines:
    highestIndex = -1
    highestIndexNumber = ""
    lowestIndex = -1
    lowestIndexNumber = ""
    
    templine = line
    numbercheck = re.sub('\D', '', templine)

    for number in numbers:
        tempIndexLeft = line.find(number)
        tempIndexRight = line.rfind(number)
        if tempIndexLeft == -1:
            continue
        else:
            if tempIndexLeft < lowestIndex or lowestIndex == -1:
                lowestIndex = tempIndexLeft
                lowestIndexNumber = dictNumber[number]
            if tempIndexRight > highestIndex:
                highestIndex = tempIndexRight
                highestIndexNumber = dictNumber[number]
    

    if len(numbercheck) == 1:
        tempIndex = line.find(numbercheck[0])
        if tempIndex < lowestIndex or lowestIndex == -1:
            lowestIndex = tempIndex
            lowestIndexNumber = numbercheck[0]
        if tempIndex > highestIndex:
            highestIndex = tempIndex
            highestIndexNumber = numbercheck[0]

    elif len(numbercheck) > 1:
        tempIndexLow = line.find(numbercheck[0])
        tempIndexHigh = line.rfind(numbercheck[-1])
        print(tempIndexHigh)
        print(highestIndex)
        print( tempIndexHigh > highestIndex)
        if tempIndexLow < lowestIndex or lowestIndex == -1:
            lowestIndex = tempIndexLow
            lowestIndexNumber = line[lowestIndex]
        if tempIndexHigh > highestIndex:
            highestIndex = tempIndexHigh
            highestIndexNumber = line[highestIndex]
   

    if lowestIndex == highestIndex:
        total += int(lowestIndexNumber + lowestIndexNumber)
        continue

    print(line)
    print(lowestIndexNumber, highestIndexNumber)
    print(int(lowestIndexNumber + highestIndexNumber))
    total += int(lowestIndexNumber + highestIndexNumber)



print(total)
