# Day 6
# Part 1
input = "input/day6.txt"

with open(input) as f:
    lines = f.read().split("\n")

times = []
distance = []
for index, line in enumerate(lines):
    lines[index] = line.split(":")[1].split()
    
print(lines[0])
for num in lines[0]:
    times.append(int(num))
for dist in lines[1]:
    distance.append(int(dist))

total = 0
for x in range(len(times)):
    count = 0
    for mili in range(times[x]):
        if mili * (times[x]-mili) > distance[x]:
            count+=1
    print(count)
    if total == 0:
        total += count
    else:
        total *= count

print(total)

# Part 2 initial 
import time
start = time.time()
with open(input) as f:
    lines = f.read().split("\n")


for index, line in enumerate(lines):
    lines[index] = line.split(":")[1].split()

newtime = int("".join(lines[0]))
distance = int("".join(lines[1]))
print(newtime, distance)
count = 0
for mili in range(newtime):
    if mili * (newtime-mili) > distance:
        count+=1
print(count)
print("finished!")

stop = time.time()
print("Day 2 un-optimized",stop-start)

# Part 2 optimised
start = time.time()

with open(input) as f:
    lines = f.read().split("\n")

for index, line in enumerate(lines):
    lines[index] = line.split(":")[1].split()

newtime = int("".join(lines[0]))
distance = int("".join(lines[1]))
newtime2 = round(newtime / 2)
print(newtime)
print(newtime2)

print(newtime2, distance)

count = 0
for mili in range(newtime2+1):
    if mili * (newtime-mili) > distance:
        count+=1

print(count*2-1)
print("finished!")

stop = time.time()
print("Day 2 optimised:", stop-start)
