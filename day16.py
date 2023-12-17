# Day 16
# Part 1
input = "input/day16.txt"
with open(input) as f:
    GRID = f.read().split("\n")

GRIDLENGTH = len(GRID)
GRIDWIDTH = len(GRID[0])

class Tile:
    totalTouched = 0

    def __init__(self, tileType):
        self.tileType = tileType
        self.touched = False
        self.directionsDone = {"north":False, "south":False, "east":False, "west":False} 
        if tileType == "|" or tileType == "-":
            self.triggered = False

    def lightUp(self):
        if self.touched == False:
            Tile.totalTouched += 1
            self.touched = True 
    
    def __repr__(self):
        return self.tileType
    
    def __str__(self) -> str:
        return self.tileType
    


class Beam:
    def __init__(self, start, direction):
        """_summary_ moves along in direction from start coordinates

        Args:
            start (list): two integers in a list 
            direction (string): "north", "south", "east", "west"
        """
        self.start = start
        self.position = start
        self.direction = direction
        self.finished = False
        GRID[self.position[1]][self.position[0]].lightUp() # lights up start tile

    def newBeams(self, tileType):
        beam1, beam2 = None, None
        # splitters
        if tileType == "|":
            if self.position[1]+ 1 < GRIDLENGTH:
                beam1 = Beam([self.position[0],self.position[1]], "south")
            if self.position[1] - 1 >= 0:
                beam2 = Beam([self.position[0],self.position[1]], "north")
        elif tileType == "-":
            if self.position[0]+ 1 < GRIDWIDTH:
                beam1 = Beam([self.position[0],self.position[1]], "east")
            if self.position[0] - 1 >= 0:
                beam2 = Beam([self.position[0],self.position[1]], "west")
        # mirrors \\
        elif tileType == "\\" and self.direction == "east":
            if self.position[1] + 1 < GRIDLENGTH:
                beam2 = Beam([self.position[0],self.position[1]], "south")
        elif tileType == "\\" and self.direction == "west":
            if self.position[1]- 1 >= 0:
                beam1 = Beam([self.position[0],self.position[1]], "north")
        elif tileType == "\\" and self.direction == "north":
            if self.position[0] - 1 >= 0:
                beam2 = Beam([self.position[0],self.position[1]], "west")
        elif tileType == "\\" and self.direction == "south":
            if self.position[0]+ 1 < GRIDWIDTH:
                beam1 = Beam([self.position[0],self.position[1]], "east")
        # mirrors / 
        elif tileType == "/" and self.direction == "east":
            if self.position[1]- 1 >= 0:
                beam1 = Beam([self.position[0],self.position[1]], "north")
        elif tileType == "/" and self.direction == "west":
            if self.position[1] + 1 < GRIDLENGTH:
                beam2 = Beam([self.position[0],self.position[1]], "south")   
        elif tileType == "/" and self.direction == "south":
            if self.position[0] - 1 >= 0:
                beam2 = Beam([self.position[0],self.position[1]], "west")
        elif tileType == "/" and self.direction == "north":
            if self.position[0]+ 1 < GRIDWIDTH:
                beam1 = Beam([self.position[0],self.position[1]], "east")          

        if all(item is not None for item in [beam1, beam2]):
            return [beam1, beam2]
        elif beam1 != None:
            return [beam1]
        elif beam2 != None:
            return [beam2]
        else:
            # print("no more tiles this way")
            return True

    def __repr__(self) -> str:
        return str(self.position)

    def move(self):
        currentTile = GRID[self.position[1]][self.position[0]]
        currentTile.directionsDone[self.direction] = True
        currentTile.lightUp()
        if self.direction == "north":
            while True:
                self.position = (self.position[0],self.position[1]-1)
                if self.position[1] < 0: 
                    self.finished = True
                    return True
                currentTile = GRID[self.position[1]][self.position[0]]
                currentTile.lightUp()
                if currentTile.tileType == "-":
                    self.finished = True
                    return self.newBeams(currentTile.tileType)
                elif currentTile.tileType in ["/", "\\"]:
                    self.finished = True
                    return self.newBeams(currentTile.tileType)

        elif self.direction == "south":
            while True:
                self.position = (self.position[0],self.position[1]+1)
                if self.position[1] >= GRIDLENGTH:
                    self.finished = True
                    return True
                currentTile = GRID[self.position[1]][self.position[0]]
                currentTile.lightUp()
                if currentTile.tileType == "-":
                    self.finished = True
                    return self.newBeams(currentTile.tileType)
                elif currentTile.tileType in ["\\", "/"]:
                    self.finished = True
                    return self.newBeams(currentTile.tileType)

        elif self.direction == "east":
            while True:
                self.position = (self.position[0] + 1,self.position[1])
                if self.position[0] >= GRIDWIDTH:
                    self.finished = True
                    return True
                currentTile = GRID[self.position[1]][self.position[0]]
                currentTile.lightUp()
                if currentTile.tileType == "|":
                    self.finished = True
                    return self.newBeams(currentTile.tileType)
                elif currentTile.tileType in ["\\", "/"]:
                    self.finished = True
                    return self.newBeams(currentTile.tileType)

        elif self.direction == "west":
            while True:
                self.position = (self.position[0] - 1,self.position[1])
                if self.position[0] < 0:
                    self.finished = True
                    return True
                currentTile = GRID[self.position[1]][self.position[0]]
                currentTile.lightUp()
                if currentTile.tileType == "|":
                    self.finished = True
                    return self.newBeams(currentTile.tileType)
                elif currentTile.tileType in ["\\", "/"]:
                    self.finished = True
                    return self.newBeams(currentTile.tileType)


for indY, down in enumerate(GRID):
    tempRight = []
    for right in down:
        tempRight.append(Tile(right))
    GRID[indY] = tempRight


ogBeamer = Beam([0,0],"south")
currentBeams = [ogBeamer]

while currentBeams:
    tempBeams = []
    for beam in currentBeams:
        movement = beam.move()
        if movement != True:
            for move in movement:
                tempBeams.append(move)

    for tempBeam in tempBeams:
        tempTile = GRID[tempBeam.position[1]][tempBeam.position[0]]
        if tempTile.directionsDone[tempBeam.direction] == True:
            tempBeams.remove(tempBeam)
    currentBeams = tempBeams.copy()

print("Part 1:",Tile.totalTouched)


# Part 2
def testBeam(currentBeams):
    while currentBeams:
        tempBeams = []
        for beam in currentBeams:
            movement = beam.move()
            if movement != True:
                for move in movement:
                    tempBeams.append(move)
        for tempBeam in tempBeams:
            tempTile = GRID[tempBeam.position[1]][tempBeam.position[0]]
            if tempTile.directionsDone[tempBeam.direction] == True:
                tempBeams.remove(tempBeam)
        currentBeams = tempBeams.copy()
    return Tile.totalTouched


potentialBeams = []
# all Y axis
for y in range(GRIDLENGTH):
    if GRID[y][0].tileType == "\\":
        potentialBeams.append([Beam([0,y],"south")])
    elif GRID[y][0].tileType == "/":
        potentialBeams.append([Beam([0,y],"north")])
    elif GRID[y][0].tileType == "|":
        potentialBeams.append([Beam([0,y],"north"),Beam([0,y],"south")])
    else:
        potentialBeams.append([Beam([0,y],"east")])

    if GRID[y][0].tileType == "\\":
        potentialBeams.append([Beam([GRIDWIDTH-1,y],"north")])
    elif GRID[y][0].tileType == "/":
        potentialBeams.append([Beam([GRIDWIDTH-1,y],"south")])
    elif GRID[y][0].tileType == "|":
        potentialBeams.append([Beam([GRIDWIDTH-1,y],"north"),Beam([0,y],"south")])
    else:
        potentialBeams.append([Beam([GRIDWIDTH-1,y],"west")])
# all X axis
for x in range(GRIDWIDTH):
    if GRID[0][x].tileType == "\\":
        potentialBeams.append([Beam([x,0],"east")])
    elif GRID[0][x].tileType == "/":
        potentialBeams.append([Beam([x,0],"west")])
    elif GRID[0][x].tileType == "-":
        potentialBeams.append([Beam([x,0],"east"),Beam([x,0],"west")])
    else:
        potentialBeams.append([Beam([x,0],"south")])
    if GRID[GRIDLENGTH-1][0].tileType == "\\":
        potentialBeams.append([Beam([x, GRIDLENGTH-1],"west")])
    elif GRID[GRIDLENGTH-1][0].tileType == "/":
        potentialBeams.append([Beam([x, GRIDLENGTH-1],"east")])
    elif GRID[GRIDLENGTH-1][0].tileType == "-":
        potentialBeams.append([Beam([x, GRIDLENGTH-1],"west"),Beam([x, GRIDLENGTH-1],"east")])
    else:
        potentialBeams.append([Beam([x, GRIDLENGTH-1],"north")])


with open(input) as f:
    GRID = f.read().split("\n")

for indY, down in enumerate(GRID):
    tempRight = []
    for right in down:
        tempRight.append(Tile(right))
    GRID[indY] = tempRight


topBeam = None

for tempBeam in potentialBeams:
    Tile.totalTouched = 0
    num = testBeam(tempBeam)
    if topBeam == None or num > topBeam:
        topBeam = num

    with open(input) as f:
        GRID = f.read().split("\n")
    for indY, down in enumerate(GRID):
        tempRight = []
        for right in down:
            tempRight.append(Tile(right))
        GRID[indY] = tempRight

print("Part 2:",topBeam)

