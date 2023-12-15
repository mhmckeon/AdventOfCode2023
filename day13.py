with open("input/day13.txt") as f:
    lines = f.read().split("\n\n")

patterns = []
for line in lines:
    patterns.append(line.split("\n"))

def patternCheck(patterns):
    total, totalDict = 0, dict()
    for num, pattern in enumerate(patterns):
        for x in range(1,len(pattern)):
            if pattern[x] == pattern[x-1]:
                side1 = pattern[:x]
                side2 = pattern[x:]
                if len(side1) < len(side2):
                    temp = list(zip(side1[::-1], side2))
                else:
                    temp = list(zip(side2, side1[::-1]))
                for z in temp:
                    if z[0] != z[1]:
                        break
                else:
                    total += x
                    totalDict[num] = x
    return total, totalDict

totalRows, rowsDict =patternCheck(patterns)

columns = []
for pattern in patterns:
    cols = list(zip(*pattern))
    for newind, col in enumerate(cols):
        cols[newind] = "".join(col)
    columns.append(cols)

totalCols, colsDict = patternCheck(columns)

print(totalCols, totalRows)
print((colsDict), (rowsDict))
overall = (totalRows*100) + totalCols
print(overall) 

# 29328 too low 

def patternCheck2(pattern):
    for x in range(1,len(pattern)):
        if pattern[x] == pattern[x-1]:
            side1 = pattern[:x]
            side2 = pattern[x:]
            if len(side1) < len(side2):
                temp = list(zip(side1[::-1], side2))
            else:
                temp = list(zip(side2, side1[::-1]))
            for z in temp:
                if z[0] != z[1]:
                    break
            else:
                return x
    return False
                   
total = 0
for pattern in patterns:
    found = False
    while not found:
        # change one symbol
        # # # # # # # # # #
        found = patternCheck2(pattern)
        
        if not found:
            cols = list(zip(*pattern))
            for newind, col in enumerate(cols):
                cols[newind] = "".join(col)
            columns.append(cols)
            found = patternCheck2(cols)

    total += found
        


totalRows =patternCheck2(patterns)
columns = []
for pattern in patterns:
    cols = list(zip(*pattern))
    for newind, col in enumerate(cols):
        cols[newind] = "".join(col)
    columns.append(cols)

totalCols = patternCheck2(columns, colsDict)
print(totalCols)
print(totalRows)

overall = (totalRows*100) + totalCols
print(overall) 

# 1500 too low
# 44813 too high



print(list(rowsDict.keys()))

print(list(colsDict.keys()))