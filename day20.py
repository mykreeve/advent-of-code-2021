from datetime import datetime
import copy

filename = "input/day20input.txt"
file = open(filename, "r")
file = file.readlines()

data = []
points = []

for index, f in enumerate(file):
    if index == 0:
        lookup = f.replace('\n', '')
    elif f != '\n':
        data.append(f.replace('\n', ''))

for yindex, y in enumerate(data):
    for xindex, ch in enumerate(y):
        if ch == '#':
            points.append((xindex, yindex))


def get_extremes(points):
    maxx = 0
    minx = 9999999999
    maxy = 0
    miny = 9999999999
    for p in points:
        if p[0] > maxx:
            maxx = p[0]
        if p[0] < minx:
            minx = p[0]
        if p[1] > maxy:
            maxy = p[1]
        if p[1] < miny:
            miny = p[1]
    return (minx, maxx, miny, maxy)


order = [(-1, -1), (0, -1), (1, -1), (-1, 0),
         (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

gen = 0
while gen < 50:
    # print('gen', gen)
    newpoints = []
    (minx, maxx, miny, maxy) = get_extremes(points)
    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            newval = ''
            for o in order:
                get_loc = (x+o[0], y+o[1])
                if (get_loc[0] < minx or get_loc[0] > maxx or get_loc[1] > maxy or get_loc[1] < miny) and gen % 2 == 0:
                    newval += '0'
                elif (get_loc[0] < minx or get_loc[0] > maxx or get_loc[1] > maxy or get_loc[1] < miny) and gen % 2 == 1:
                    if lookup[0] == '.':
                        newval += '0'
                    else:
                        newval += '1'
                elif get_loc in points:
                    newval += '1'
                else:
                    newval += '0'
            # print(newval)
            newval = int(newval, 2)
            # print(newval)
            if lookup[newval] == '#':
                newpoints.append((x, y))
    gen += 1
    points = newpoints
    if (gen == 2):
        print(len(points))

print(len(points))
