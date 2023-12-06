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

# Part 2

with open(input) as f:
    lines = f.read().split("\n")


times = []
distance = []
for index, line in enumerate(lines):
    lines[index] = line.split(":")[1].split()

time = int("".join(lines[0]))
distance = int("".join(lines[1]))
print(time, distance)
count = 0
for mili in range(time):
    if mili * (time-mili) > distance:
        count+=1
print(count)
print("finished!")

