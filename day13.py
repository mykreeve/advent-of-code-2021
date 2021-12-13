from datetime import datetime
import copy

filename = "input/day13input.txt"
file = open(filename, "r")
file = file.readlines()

points = []
folds = []

now = datetime.now()

for f in file:
    if ',' in f:
        f = f.replace('\n', '').split(',')
        points.append((int(f[0]), int(f[1])))
    elif f != '\n':
        f = f.replace('\n', '').replace('fold along ', '').split('=')
        folds.append((f[0], int(f[1])))


def do_fold(points, fold):
    new_points = []
    if fold[0] == 'x':
        for p in points:
            # print(p)
            if p[0] > fold[1]:
                dist_from_fold = p[0]-fold[1]
                new_points.append((fold[1] - dist_from_fold, p[1]))
            else:
                new_points.append(p)
    if fold[0] == 'y':
        for p in points:
            # print(p, fold[1])
            if p[1] > fold[1]:
                dist_from_fold = p[1]-fold[1]
                # print(dist_from_fold)
                # print((p[0], fold[1] - dist_from_fold))
                new_points.append((p[0], fold[1] - dist_from_fold))
                # input('.')
            else:
                new_points.append(p)
    return new_points


def remove_dupes(points):
    new_points = []
    for p in points:
        if p not in new_points:
            new_points.append(p)
    return new_points


first = True

while len(folds) != 0:
    fold = folds.pop(0)
    points = do_fold(points, fold)
    points = remove_dupes(points)
    if first:
        done = datetime.now()
        print("Answer to part 1:", len(points))
        print("Time taken:", done - now)
        now = datetime.now()
        first = False

maxx = 0
maxy = 0

for p in points:
    if p[0] > maxx:
        maxx = p[0]
    if p[1] > maxy:
        maxy = p[1]

done = datetime.now()
print("Answer to part 2:")
for y in range(maxy+1):
    for x in range(maxx+1):
        if (x, y) in points:
            print('#', end='')
        else:
            print('.', end='')
    print()

print("Time taken:", done - now)
