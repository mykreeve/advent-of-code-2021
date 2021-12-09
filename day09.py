from datetime import datetime
import copy

filename = "input/day09input.txt"
file = open(filename, "r")
file = file.readlines()

land = {}

now = datetime.now()
for y, f in enumerate(file):
    f = f.replace('\n', '')
    for x, ch in enumerate(f):
        land[(x, y)] = int(ch)
        maxx = x
        maxy = y


def is_smaller_than_neighbours(x, y, land):
    if (x-1, y) in land and land[(x-1, y)] <= land[(x, y)]:
        return False
    if (x+1, y) in land and land[(x+1, y)] <= land[(x, y)]:
        return False
    if (x, y-1) in land and land[(x, y-1)] <= land[(x, y)]:
        return False
    if (x, y+1) in land and land[(x, y+1)] <= land[(x, y)]:
        return False
    return True


score = 0
for y in range(maxy+1):
    for x in range(maxx+1):
        if is_smaller_than_neighbours(x, y, land):
            score += (1 + land[(x, y)])

done = datetime.now()
print("Answer to part 1:", score)
print("Time taken:", done - now)

now = datetime.now()

for y in range(maxy+1):
    for x in range(maxx+1):
        if land[(x, y)] != 9:
            land[(x, y)] = 'B'

basins = []


def remove_basin(x, y, land):
    size = 0
    tests = [(x, y)]
    while len(tests) > 0:
        copy_tests = copy.deepcopy(tests)
        tests = []
        for t in copy_tests:
            if land[t] == 'B':
                land[t] = ''
                size += 1
            if (t[0]-1, t[1]) in land and land[(t[0]-1, t[1])] == 'B':
                tests.append((t[0]-1, t[1]))
            if (t[0]+1, t[1]) in land and land[(t[0]+1, t[1])] == 'B':
                tests.append((t[0]+1, t[1]))
            if (t[0], t[1]-1) in land and land[(t[0], t[1]-1)] == 'B':
                tests.append((t[0], t[1]-1))
            if (t[0], t[1]+1) in land and land[(t[0], t[1]+1)] == 'B':
                tests.append((t[0], t[1]+1))
    return (land, size)


for y in range(maxy+1):
    for x in range(maxx+1):
        if land[(x, y)] == 'B':
            (land, size) = remove_basin(x, y, land)
            basins.append(size)

basins.sort(reverse=True)

done = datetime.now()
print("Answer to part 2:", basins[0] * basins[1] * basins[2])
print("Time taken:", done - now)
