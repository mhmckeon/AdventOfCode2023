# Day 15
# Part1

words = open("input/day15.txt").read().split(",")


def hashWord(char):
    value=0
    for x in char:
        value = ((ord(x)+value)*17)%256
    return value

total = 0
for word in words:
    total += hashWord(word)

print("Part 1:",total)

dictBoxes = {}
# Part 2
for word in words:
    if word.count("=") == 1:
        duo = (word.split("="))
        box = hashWord(duo[0])
        if box in dictBoxes.keys():
            added = False
            for x in dictBoxes:
                for ind, lense in enumerate(dictBoxes[x]):
                    if lense[0] == duo[0]:
                        dictBoxes[x][ind] = duo
                        added = True
                        break
            if not added:
                dictBoxes[box] += [duo]
        else:
            dictBoxes[box] = [duo]
                         
    else:
        duo = (word.split("-"))
        box = hashWord(duo[0])
        for x in dictBoxes:
            for ind, lense in enumerate(dictBoxes[x]):
                if lense[0] == duo[0]:
                    dictBoxes[x].remove(dictBoxes[x][ind])


total = 0
for box in dictBoxes:
    num = box + 1
    for ind, lense in enumerate(dictBoxes[box]):
        lense = int(lense[1])
        total += num * (1 + ind) * lense

print("Part 2:",total)
