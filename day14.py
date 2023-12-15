# Day 14 P1 
with open("input/day14.txt") as f:
    lines = f.read().split("\n")

lines = list(zip(*lines))

def tilt(lines):
    for ind, line in enumerate(lines):
        line =list(line)
        count = 0
        while True:
            if count > len(line):
                break
            for x in range(len(lines)):
                if line[x] == ".":
                    if x < len(lines)-1:
                        if line[x+1] == "O":
                            line[x] = "O"
                            line[x+1] = "."
                            count = 0
                count += 1
        lines[ind] = line
    return lines

def countWeight(input):
    input = list(input)
    lineInput = input.copy()
    total = 0
    for ind, line in enumerate(lineInput):
        lineInput[ind] = list(line)
        line = line[::-1]
        for num, x in enumerate(line,start=1):
            if x == "O":
                total += num
    return total

print(countWeight(tilt(lines)))
print()
# Day 14 P2
with open("input/day14.txt") as f:
    lines = f.read().split("\n")
lines = list(zip(*lines))


allLayouts = set(tuple(lines.copy()))
pattern = []
total = 0
for turn in range(1001):
    lines = tilt(lines)
    lines = list(zip(*lines))
    lines = tilt(lines)
    lines = list(zip(*lines))
    for ind, line in enumerate(lines):
        lines[ind] = list(line)[::-1]
    lines = tilt(lines)
    for ind, line in enumerate(lines):
        lines[ind] = list(line)[::-1]
    lines = list(zip(*lines))
    for ind, line in enumerate(lines):
        lines[ind] = list(line)[::-1]
    lines = tilt(lines)
    for ind, line in enumerate(lines):
        lines[ind] = list(line)[::-1]
    lines = list(zip(*lines))

    if tuple(lines.copy()) in allLayouts:
        break
    pattern.append(tuple(lines.copy()))
    allLayouts.add(tuple(lines.copy()))

print(turn)
first = pattern.index(tuple(lines.copy()))

grid = pattern[(1000000000 - first) % (turn - first) + first-1]

print(countWeight(grid))




