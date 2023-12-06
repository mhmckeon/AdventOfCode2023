# Day 5
# Part 1
input = "input/day5.txt"

with open(input) as f:
    lines = f.read().split("\n")

lines[0] = lines[0][7:]
lines = [line for line in lines if len(line) > 0]
seeds = lines[0].split()
lines = lines[1:]

maps = [[],[],[],[],[],[],[]]

index = -1
for line in lines:
    if line[0].isalpha():
        index += 1
    else:
        maps[index].append(line)

def checkRange(find, listofNums):
    findTheNum = None
    for numbers in listofNums:
        numbers = numbers.split()
        destination = int(numbers[0])
        finder = int(numbers[1])
        rangeToUse = int(numbers[2])
        if find >= finder and find <= finder + rangeToUse:
            return find - finder + destination
    return findTheNum

lowestEnd = None


# for seed in seeds:
#     seed = int(seed)
#     for map in maps:
#         check = checkRange(seed, map)
#         if check != None:
#             seed = check
#     if lowestEnd == None or seed < lowestEnd:
#         lowestEnd = seed

print(lowestEnd)
   
# Day 2

def newcheckRange(find, listofNums):
    findTheNum = None
    for numbers in listofNums:
        numbers = numbers.split()
        finder = int(numbers[0])
        destination = int(numbers[1])
        rangeToUse = int(numbers[2])
        if find >= finder and find <= finder + rangeToUse:
            return destination - finder + find
    return findTheNum



# method 2
# seedList = []
# maps.reverse()
# numberFound = False
# number = 46
# while numberFound == False:
#     seed = number
#     for map in maps:
#         check = newcheckRange(seed, map)
#         if check != None:
#             seed = check
#     for x in range(1,len(seeds),2):
#         start = int(seeds[x-1])
#         stop = int(seeds[x]) + start
#         if seed >= start and seed <= stop:
#             seedList.append(number)
    
#     if number == 1000000:
#         break
#     number += 1

# print(1)
# print(seedList)
# print(min(seedList))






# # works for sample - not optimised enough for full
# lowestEnd = None
# for x in range(1,len(seeds),2):
#     start = int(seeds[x-1])
#     stop = int(seeds[x])
#     print(start, start + stop)
#     for y in range(start, (start +stop)):
#         seed = y
#         print(y)
#         for map in maps:
#             check = checkRange(seed, map)
#             if check != None:
#                 seed = check
#         print("Cuurrent lowest",lowestEnd)
#         print("current seed:", seed)
#         if lowestEnd == None or seed < lowestEnd:
#             lowestEnd = seed
# print(lowestEnd)


# 1852510996 # too high



# Day 5 Part 2 Attempt 3
newMaps = []
for map in maps:
    tempMap = []
    for x in range(len(map)):
        dest, source, rangeToUse = map[x].split()
        tempMap.append([int(dest), int(source), int(rangeToUse)])
    newMaps.append(tempMap)

print(newMaps)


seedRanges = []

for x in range(1,len(seeds),2):
    start = int(seeds[x-1])
    stop = int(seeds[x])
    seedRanges.append([start,start+stop-1])

print(f"Seed ranges: {seedRanges}")


def rangeCheckAllIn(range,map):
    lower, upper = range
    ranges = []
    counter = 0
    while True:
        for item in map:
            if lower > upper:
                return ranges

            if lower > (item[1] + item[2]-1) or upper < item[1]:
                counter += 1
                if counter > len(map):
                    ranges.append([lower,upper])
                    return ranges
                continue
            counter = 0
            # checks all in
            if lower >= item[1] and upper <= (item[1]+item[2]-1): # if error, check if these should be <= >=
                lower = lower - item[1] + item[0]
                upper = upper - item[1] + item[0]
                ranges.append([lower,upper])
                return ranges            
            # then checks for just lower
            elif lower >= item[1] and lower <= item[1]+item[2]-1:
                tempLower = lower - item[1] + item[0]
                tempUpper = item[0] + item[2]-1          # check adding in -1 if error with input
                ranges.append([tempLower, tempUpper])
                lower = item[1] + item[2]
            # then checks just upper
            elif upper >= item[1] and upper <= item[1] + item[2]-1:
                tempUpper = upper - item[1] + item[0]
                tempLower = item[0]
                ranges.append([tempLower, tempUpper])
                upper = item[1]-1
           

endRange = []
topLevelInput = seedRanges.copy()
nextLevelInput = []
level = 0
while level < 7:
    if level == 5:
        pass
    print(f"level is {level}")
    print(f"Seed is {topLevelInput}")
    print(f"map is {newMaps[level]}")
    for seed in topLevelInput:
        output = rangeCheckAllIn(seed,newMaps[level])
        for item in output:
            nextLevelInput.append(item)
    print(f"After level {level}")
    print(f"New seeds are {nextLevelInput}")
        
    topLevelInput = nextLevelInput.copy()
    nextLevelInput.clear()
    if level == 6:
        print(topLevelInput)
    level += 1

minimum = None
for item in topLevelInput:
    if minimum == None or item[0] < minimum:
        print(item)
        minimum = item[0]

print("min is", minimum)
if minimum <  24261546:
    print(True)
#  too high - 24261546
# print(rangeCheckAllIn([46, 56],[[60, 56, 37], [56, 93, 4]]))
print("Finished")
# [57,70]

# for seedrange in seedRanges:
#     lower = seedrange[0]
#     upper = seedrange[1]
#     listOfRanges = [[lower, upper]]
#     newListOfRanges = []
#     for map in maps:
        
print(max([x for x in range(69,70,1)]))