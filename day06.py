from datetime import datetime
import copy

filename = "input/day06input.txt"
file = open(filename, "r")
file = file.readlines()

lanternfish_initials = [0, 1, 2, 3, 4, 5, 6]
lanternfish_after80 = {}
lanternfish_after256 = {}

now = datetime.now()
def lanternfish_generation(input):
    output = []
    for i in input:
        if i > 0:
            output.append(i-1)
        else:
            output.append(6)
            output.append(8)
    return output


for init in lanternfish_initials:
    gen = 0
    state = [init]
    while gen < 80:
        state = lanternfish_generation(state)
        gen += 1
    lanternfish_after80[init] = len(state)

for f in file:
    f = f.replace('\n', '').split(',')

total_fish = 0
for item in f:
    total_fish += lanternfish_after80[int(item)]

done = datetime.now()
print("Answer to part 1:", total_fish)
print("Time taken:", done - now)


now = datetime.now()
def improved_lanternfish_generation(input):
    output = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in input:
        if i > 0:
            output[i-1] += input[i]
        else:
            output[6] += input[i]
            output[8] += input[i]
    return output


for init in lanternfish_initials:
    gen = 0
    state = {init: 1}
    while gen < 256:
        state = improved_lanternfish_generation(state)
        gen += 1
    counter = 0
    for l in state:
        counter += state[l]
    lanternfish_after256[init] = counter

total_fish = 0
for item in f:
    total_fish += lanternfish_after256[int(item)]

done = datetime.now()
print("Answer to part 2:", total_fish)
print("Time taken:", done - now)