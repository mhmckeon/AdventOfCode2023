# Day 12

with open("input/day12.txt") as f:
    lines = f.read().split("\n")

spaces, nums = [],[]
for line in lines:
    s,n = line.split()
    spaces.append(s)
    n = list(map(int,n.split(",")))
    nums.append(n)

for ind, space in enumerate(spaces):
    space = space.split(".")
    space = [x for x in space if len(x)>0]
    # space = list(filter(lambda x: len(x) > 0, space))
    spaces[ind] = space

print(spaces)
print(nums)







checkAllCount = 0
while True:
    if checkAllCount >= len(spaces):
        break
    checkAllCount = 0 
    for indOut, space in enumerate(spaces):
        print(space)
        print(nums[indOut])
        print(indOut)
        if len(space) == 0 or len(nums[indOut]):
            checkAllCount += 1
            continue
        if len(space[-1]) == nums[indOut][-1]:
            spaces[indOut] = space[:-1]
            nums[indOut] = nums[indOut][:-1]
            checkAllCount = 0
        else:
            checkAllCount += 1

print(nums)
#check the line for max length element
for indOut, space in enumerate(spaces):
    if len(space)>0:
        if max(nums[indOut]) == nums[indOut][0]:
            char = "".join(["#" for _ in range(max(nums[indOut]))])
        else:
            continue
    else:
        continue
    if char in str(space):
        space = str(space)
        minIndex = space.find(char)
        spaces[indOut] = [space[minIndex+len(char)+1:-2]]
        nums[indOut] = nums[indOut][1:]


total = 0
for indOut, space in enumerate(spaces):
    print(space, nums[indOut])
    lineLen = 0
    for ele in space:
        lineLen += len(ele)
    if len(space) == 0:
        total += 1
        print(.1)
    elif (lineLen/sum(nums[indOut])) < 2:
        total += 1
        print(1)
    elif len(space) == len(nums[indOut]): # dont think this is right
        newlist =list(zip(space, nums[indOut]))
        for fir, sec in newlist:
            total += len(fir) // sec
            print(len(fir)//sec)
    else:
        lineLen = 0
        for ele in space:
            lineLen += len(ele)
        for ele in nums[indOut]:
            print(total, ele)
            total += lineLen // ele

print(total)
    


# 3942 too low
# 