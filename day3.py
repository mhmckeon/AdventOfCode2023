# Day 3
input = "input/day3.txt"

with open(input) as f:
    lines = f.read().split("\n")


partNumbers = set()
total = 0
charSet = set()

for index, line in enumerate(lines):
    lineIndex = 0
    print(index,lineIndex)
    for char in line:
        coordinateList = [
        (index-1, lineIndex-1),
        (index-1, lineIndex),
        (index-1, lineIndex+1),
        (index, lineIndex-1),
        (index, lineIndex),
        (index, lineIndex+1),
        (index+1, lineIndex-1),
        (index+1, lineIndex),
        (index+1, lineIndex+1)
        ]
        if not char.isdigit() and char != ".":
            charSet.add(char)
            endTuple = set()
            for location in coordinateList:
                try:
                    if location[0] < 0 or location[1] < 0:
                        continue
                    if (lines[location[0]][location[1]]).isdigit():
                        xCoordlower, xCoordUpper = location[1], location[1]+1

                        xCoord = location[1]-1                            
                        while True:
                            if xCoord < 0:
                                xCoordlower = xCoord + 1
                                break
                            if (lines[location[0]][xCoord]).isdigit():
                                xCoord -= 1
                            else:
                                xCoordlower = xCoord +1
                                break
                        xCoord = location[1]+1
                        while True:
                            if xCoord == len(line):
                                xCoordUpper = xCoord
                                break
                            if (lines[location[0]][xCoord]).isdigit():
                                xCoord += 1
                            else:
                                xCoordUpper = xCoord
                                break
                        endTuple = (location[0],xCoordlower,xCoordUpper)
                        if endTuple not in partNumbers:
                            partNumbers.add(endTuple)
                            print(lines[location[0]][xCoordlower:xCoordUpper], endTuple)
                            total += int(lines[location[0]][xCoordlower:xCoordUpper])
                except:
                    pass
        lineIndex += 1

print(partNumbers)
print(total)

print(charSet)

# Part 2
print("----------------------------------------------------")

partNumbers = set()
total = 0
charSet = set()
endTuple = set()
endSet = set()

print(lines[1][10:12])
print(len(lines[0]))

for index, line in enumerate(lines):
    lineIndex = 0
    print(index,lineIndex)
    for char in line:
        coordinateList = [
        (index-1, lineIndex-1),
        (index-1, lineIndex),
        (index-1, lineIndex+1),
        (index, lineIndex-1),
        (index, lineIndex),
        (index, lineIndex+1),
        (index+1, lineIndex-1),
        (index+1, lineIndex),
        (index+1, lineIndex+1)
        ]
        if char == "*":
            print(line, lineIndex, index)
            charSet.add(char)
            endSet = set()
            endTuple = []
            for location in coordinateList:
                if location[0] < 0 or location[1] < 0:
                    continue
                if (lines[location[0]][location[1]]).isdigit():
                    xCoordlower, xCoordUpper = location[1], location[1]+1

                    xCoord = location[1]-1                            
                    while True:
                        if xCoord < 0:
                            xCoordlower = xCoord + 1
                            break
                        if (lines[location[0]][xCoord]).isdigit():
                            xCoord -= 1
                        else:
                            xCoordlower = xCoord +1
                            break
                    xCoord = location[1]+1
                    while True:
                        if xCoord == len(line):
                            xCoordUpper = xCoord
                            break
                        if (lines[location[0]][xCoord]).isdigit():
                            xCoord += 1
                        else:
                            xCoordUpper = xCoord
                            break
                    print(lines[location[0]][xCoordlower:xCoordUpper])
                    if (location[0],xCoordlower, xCoordUpper) not in endSet:
                        endSet.add((location[0],xCoordlower, xCoordUpper))
                        endTuple.append(int(lines[location[0]][xCoordlower:xCoordUpper]))

        print(endTuple)
        if len(endSet) == 2:
            total += (int(endTuple[0]) * int(endTuple[1]))
            endSet.clear()
            endTuple.clear()
        lineIndex += 1

print(total)