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
                   
rowTotal = 0
colTotal = 0
for num, pattern in enumerate(patterns):
    found = False
    row = 0
    column = 0
    while not found:
        patt = pattern.copy()
        if patt[column][row] == ".":
            patt[column] = patt[column][:row] + "#" + patt[column][row+1:]
            print(123)
        else:
            print(patt)
            patt[column]=patt[column][:row] + "." + patt[column][row+1:]
            print(patt)
        row+=1
        if row == len(patt[column]):
            row = 0
            column += 1
        if column == len(patt):
            if patternCheck2(pattern):
                rowTotal += patternCheck2(pattern) 
            else:
                cols = list(zip(*patt))
                for newind, col in enumerate(cols):
                    cols[newind] = "".join(col)
                found = patternCheck2(cols)
                colTotal += found

        found = patternCheck2(patt)
        if found:
            if num in rowsDict:
                if rowsDict[num] == found:
                    found = False
                else:
                    rowTotal += found
            else:
                rowTotal += found
        print(1,rowTotal)
        if not found:
            cols = list(zip(*patt))
            for newind, col in enumerate(cols):
                cols[newind] = "".join(col)
            columns.append(cols)
            found = patternCheck2(cols)
            if found:
                if num in colsDict:
                    if colsDict[num] == found:
                        found = False
                    else:
                        colTotal += found
                else:
                    colTotal += 1

print(rowTotal)
print(colTotal)




# 1500 too low
# 44813 too high


