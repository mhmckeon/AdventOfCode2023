# Day 9
# Part 1
input = "input/day9.txt"
with open(input) as f:
    lines = f.read().split("\n")

total = 0
for line in lines:
    line = line.split(" ")
    eol, tempList = [int(line[-1])], None
    while tempList == None or len(tempList) != tempList.count(0):
        tempList = [int(line[x])-int(line[x-1]) for x in range(1,len(line))]
        eol.append(tempList[-1])
        line = tempList
    total += (sum(eol))

print("Part 1:", total)

# Part 2
total = 0
for line in lines:
    line = line.split(" ")[::-1]
    eol, tempList = [int(line[-1])], None
    while tempList == None or len(tempList) != tempList.count(0):
        tempList = [int(line[x])-int(line[x-1]) for x in range(1,len(line))]
        eol.append(tempList[-1])
        line = tempList
    total += (sum(eol))

print("Part 2:",total)