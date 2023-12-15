
class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        s = f"X: {self.x}, Y: {self.y}"
        return s
    
    def getLocation(self):
        return (self.x, self.y)
    
    def manhattan_dist2(self, place, xExpand, yExpand):
        newLoc = place.getLocation()
        xCross = 0
        for x in xExpand:
            if x in range(min(self.x,newLoc[0]),max(self.x,newLoc[0])):
                xCross += 1
        yCross = 0
        for x in yExpand:
            if x in range(min(self.y,newLoc[1]),max(self.y,newLoc[1])):
                yCross += 1
        newX = abs(self.x - newLoc[0])
        newY = abs(self.y - newLoc[1])
        return newX + newY + (xCross*999999) + (yCross * 999999)
    
    def manhattan_dist(self, place):
        newLoc = place.getLocation()
        newX = abs(self.x +1 - newLoc[0]-1)
        newY = abs(self.y+1 - newLoc[1]-1)
        return newX + newY
    
# Day 11
# Part 1 - done by expanding the graph
with open("input/day11.txt") as f:
    lines = f.read().split("\n")

needsExpandingY = set()
needsExpandingX = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            needsExpandingX.add(x)
            needsExpandingY.add(y)

xExpand = set([x for x in range(len(lines[0]))])
xExpand= sorted(list(xExpand.difference(needsExpandingX)), reverse=True)

for x in xExpand:
    for y, line in enumerate(lines):
        lines[y] = line[0:x] + "." + line[x:]

yExpand = set([x for x in range(len(lines))])
yExpand= sorted(list(yExpand.difference(needsExpandingY)), reverse=True)

for y in yExpand:
    newLine = []
    newLine += lines[0:y]
    newLine += lines[y:y+1]
    newLine += lines[y:] 
    lines = newLine

locations = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            locations.append(Location(x, y))


total = 0
for x in range(len(locations)):
    for y in range(x+1, len(locations)):
        total += locations[x].manhattan_dist(locations[y])

print("Total 1:",total)

# Part 2 - done by changing the algorithm in manhattan distance (2)
with open("input/day11.txt") as f:
    lines = f.read().split("\n")

needsExpandingY = set()
needsExpandingX = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            needsExpandingX.add(x)
            needsExpandingY.add(y)

xExpand = set([x for x in range(len(lines[0]))])
xExpand= sorted(list(xExpand.difference(needsExpandingX)), reverse=True)

yExpand = set([x for x in range(len(lines))])
yExpand= sorted(list(yExpand.difference(needsExpandingY)), reverse=True)


locations = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            locations.append(Location(x, y))

total = 0
for x in range(len(locations)):
    for y in range(x+1, len(locations)):
        total += locations[x].manhattan_dist2(locations[y], xExpand, yExpand)
print("total 2:", total)
