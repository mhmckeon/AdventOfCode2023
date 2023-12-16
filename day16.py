# Day 16
# Part 1
input = "input/day16.txt"
with open(input) as f:
    lines = f.read().split("\n")


class tile:
    totalTouched = 0

    def __init__(self, tileType):
        self.tileType = tileType
        self.touched = False
        self.directionsDone = {"north":False, "south":False, "east":False, "west":False} 
        if tileType == "|" or tileType == "-":
            self.triggered = False

    def lightUp(self):
        if self.touched == False:
            tile.totalTouched += 1
            self.touched = True 
    


class beam:
    def __init__(self, start, direction):
        self.start = start
        self.position = start
        self.direction = direction
        self.finished = False

    def move(self, grid):
        if self.direction == "north":
            self.position = (self.position[0],self.position[1]+1)
            if self.position[1] >= len(grid): # change to just greater than if issues
                self.finished = True
            
        elif self.direction == "south":
            self.position = (self.position[0],self.position[1]-1)
            if self.position[1] < 0:
                self.finished = True

        elif self.direction == "east":
            self.position = (self.position[0] + 1,self.position[1])
            if self.position[0] >= len(grid[0]):
                self.finished = True
                
        elif self.direction == "west":
            self.position = (self.position[0] - 1,self.position[1])
            if self.position[0] < 0:
                self.finished = True
