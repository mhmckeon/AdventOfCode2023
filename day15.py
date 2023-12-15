# Day 15

words =  open("input/day15.txt").read().split(",")


def hashChar(char, value):
    return ((ord(char)+value)*17)%256

total = 0
for word in words:
    value=0
    for x in word:
        value = hashChar(x, value)
    total += value

print(value)
print(total)