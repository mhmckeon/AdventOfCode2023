with open("input/day17.txt") as f:
    lines = f.read().split("\n")

moves = [[line.split()[0], int(line.split()[1])] for line in lines]

grid = set()

currentX = 0
currentY = 0
for move in moves:
    if move[0] == "R":
        currentX += move[1]
        grid.add((currentX, currentY))
    elif move[0] == "L":
        currentX -= move[1]
        grid.add((currentX, currentY))
    elif move[0] == "D":
        currentY += move[1]
        grid.add((currentX, currentY))
    elif move[0] == "U":
        currentY -= move[1]
        grid.add((currentX, currentY))

grid = list(grid)
grid.sort(key=lambda x:x[0])
xMin = grid[0][0]
xMax = grid[-1][0]

grid.sort(key= lambda x:(x[1]))
ymin = grid[0][1]
ymax = grid[-1][1]

print("x", xMin, xMax)
print("y",ymin,ymax)


newGrid = [["." for _ in range(xMin, xMax)] for _ in range(ymin,ymax+1)]

currentX = 0
currentY = 0
for move in moves:
    if move[0] == "R":
        for x in range(move[1]):
            newGrid[currentY][currentX] = "#"
            currentX += 1
    elif move[0] == "L":
        for x in range(move[1]):
            newGrid[currentY][currentX] = "#"
            currentX -= 1
    elif move[0] == "D":
        for x in range(move[1]):
            newGrid[currentY][currentX] = "#"
            currentY += 1
    elif move[0] == "U":
        for x in range(move[1]):
            newGrid[currentY][currentX] = "#"
            currentY -= 1

for line in newGrid:
    print(line)
