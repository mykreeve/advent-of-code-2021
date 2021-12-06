from datetime import datetime
import copy

filename = "input/day05input.txt"
file = open(filename, "r")
file = file.readlines()

pipes = []
grid = {}

for f in file:
    line = f.replace('\n', '').replace(' -> ', ',').split(',')
    pipe = ((int(line[0]), int(line[1])), ((int(line[2]), int(line[3]))))
    pipes.append(pipe)


def find_orientation(pipe):
    if pipe[0][0] == pipe[1][0]:
        return 'v'
    elif pipe[0][1] == pipe[1][1]:
        return 'h'
    return 'd'


def update_grid(grid, loc):
    if loc not in grid:
        grid[loc] = 1
    else:
        grid[loc] += 1
    return grid


for p in pipes:
    dir = find_orientation(p)
    if dir in ['h', 'v']:
        if dir == 'h':
            lowest = min(p[0][0], p[1][0])
            highest = max(p[0][0], p[1][0])
            for x in range(lowest, highest+1):
                grid = update_grid(grid, (x, p[0][1]))
        elif dir == 'v':
            lowest = min(p[0][1], p[1][1])
            highest = max(p[0][1], p[1][1])
            for y in range(lowest, highest+1):
                grid = update_grid(grid, (p[0][0], y))

count = 0
for l in grid:
    if grid[l] > 1:
        count += 1

print(count)

grid = {}

for p in pipes:
    dir = find_orientation(p)
    if dir == 'h':
        lowest = min(p[0][0], p[1][0])
        highest = max(p[0][0], p[1][0])
        for x in range(lowest, highest+1):
            grid = update_grid(grid, (x, p[0][1]))
    elif dir == 'v':
        lowest = min(p[0][1], p[1][1])
        highest = max(p[0][1], p[1][1])
        for y in range(lowest, highest+1):
            grid = update_grid(grid, (p[0][0], y))
    elif dir == 'd':
        xdir = p[0][0] - p[1][0]
        ydir = p[0][1] - p[1][1]
        if xdir == ydir:
            if p[0][0] < p[1][0]:
                newp = p
            else:
                newp = (p[1], p[0])
            lowest = min(newp[0][0], newp[1][0])
            highest = max(newp[0][0], newp[1][0])
            for x in range(0, highest+1-lowest):
                grid = update_grid(grid, (newp[0][0]+x, newp[0][1]+x))
        else:
            if p[0][0] < p[1][0]:
                newp = p
            else:
                newp = (p[1], p[0])
            lowest = min(newp[0][0], newp[1][0])
            highest = max(newp[0][0], newp[1][0])
            for x in range(0, highest+1-lowest):
                grid = update_grid(grid, (newp[0][0]+x, newp[0][1]-x))

count = 0
for l in grid:
    if grid[l] > 1:
        count += 1

print(count)
