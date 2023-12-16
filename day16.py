# Day 16
# Part 1
input = "input/day16.txt"
with open(input) as f:
    lines = f.read().split("\n")

class tile:
    totalTouched = 0

    def __init__(self, type):
        self.type = type
        self.touched = False
        self.directionsDone = {"north":False, "south":False, "east":False, "west":False} 


class beam:
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction

    
