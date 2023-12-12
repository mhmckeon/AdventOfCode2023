# Day 10
# Part 1
input = "input/day10.txt"
with open(input) as f:
    lines = f.read().split("\n")


def startFinder(lines):
    for i, line in enumerate(lines):
        if line.find("S") != -1:
            return (line.find("S"), i)
        

def potentialStarts(S):
    if S[0] == 0 and S[1] == 0:
        return [(S[0]+1,S[1]),(S[0],S[1]+1)]
    elif S[0] == 0:
        return [(S[0]+1,S[1]),(S[0],S[1]+1),(S[0],S[1]-1)]
    elif S[1] == 0:
        return [(S[0]-1,S[1]),(S[0]+1,S[1]),(S[0],S[1]+1)]
    elif S[0] > 0 and S[1] > 0:
        return [(S[0]-1,S[1]),(S[0]+1,S[1]),(S[0],S[1]+1),(S[0],S[1]-1)]
     

def coordinatefinder(location):
    lineLocated = lines[location[1]]
    indexIn = lineLocated[location[0]]
    return (indexIn)
        
stepCount = 1
start = startFinder(lines)
potentialStartsList = potentialStarts(start)
path = set()
success = False

potentialPaths = []

potentialStartsList = [potentialStartsList[-1]]

for current in potentialStartsList:
    path = set()
    path.add(start)
    path.add(current)
    stepCount = 0
    while current != start and success == False:
        figure = coordinatefinder(current)
        try:
            if figure == ".":
                break
            elif figure == "L":
                if not (current[0]+1,current[1]) in path:   # if needs to move right
                    path.add((current[0]+1,current[1]))
                    stepCount += 1
                    current = (current[0]+1,current[1])
                else:                                       # if needs to move up
                    path.add((current[0],current[1]-1))
                    stepCount += 1
                    current = (current[0],current[1]-1)
                
            elif figure == "J":
                if not (current[0]-1,current[1]) in path:   # if needs to move left
                    path.add((current[0]-1,current[1]))
                    stepCount += 1
                    current = (current[0]-1,current[1])
                else:                                       # if needs to move up
                    path.add((current[0],current[1]-1))
                    stepCount += 1
                    current = (current[0],current[1]-1)
            elif figure == "7":
                if not (current[0]-1,current[1]) in path:   # if needs to move left
                    path.add((current[0]-1,current[1]))
                    stepCount += 1
                    current = (current[0]-1,current[1])
                else:                                       # if needs to move down
                    path.add((current[0],current[1]+1))
                    stepCount += 1
                    current = (current[0],current[1]+1)
            elif figure == "F":
                if not (current[0],current[1]+1) in path:   # if needs to move down
                    path.add((current[0],current[1]+1))
                    stepCount += 1
                    current = (current[0],current[1]+1)
                else:                                       # if needs to move right
                    path.add((current[0]+1,current[1]))
                    stepCount += 1
                    current = (current[0]+1,current[1])
            elif figure == "-":
                if not (current[0]-1,current[1]) in path:   # if needs to move left
                    path.add((current[0]-1,current[1]))
                    stepCount += 1
                    current = (current[0]-1,current[1])
                else:                                       # if needs to move right
                    path.add((current[0]+1,current[1]))
                    stepCount += 1
                    current = (current[0]+1,current[1])
            elif figure == "|":
                if not (current[0],current[1]+1) in path:   # if needs to move down
                    path.add((current[0],current[1]+1))
                    stepCount += 1
                    current = (current[0],current[1]+1)
                else:                                       # if needs to move up
                    path.add((current[0],current[1]-1))
                    stepCount += 1
                    current = (current[0],current[1]-1)

            if stepCount ==2:
                path.remove(start)
        except:
            print("Broke loop due to hitting edge")
            print(figure)
            print(current)
            success = False
            break
    if current == start:
        
        potentialPaths.append((stepCount+1)/2)
        
print(potentialPaths)
print(len(path))


# Part 2
pathGroups =[]
for x in range(len(lines)):
    pathGroups.append([])
    for coord in path:
        if coord[1] == x:
            pathGroups[x].append(coord)

# pathGroups = [[(1,0), (1,1),(3,2),(2,1),(0,0),(3,1)]]

for x, paths in enumerate(pathGroups):
    if len(paths) > 1:
        newPath = []
        for item in paths:
            newPath.append(item[0])
        newPath.sort()
        # paths.sort(key=lambda x: (x[0], x[1]))
        pathGroups[x] = newPath
        

print(pathGroups)

