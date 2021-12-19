from datetime import datetime
import copy


filename = "input/day19input.txt"
file = open(filename, "r")
file = file.readlines()

scanners = []
current = []

for f in file:
    f = f.replace('\n', '')
    if '---' in f:
        if len(current) > 0:
            scanners.append(current)
        current = []
    elif f != '':
        f = f.split(',')
        current.append((int(f[0]), int(f[1]), int(f[2])))
scanners.append(current)

scannerscopy = copy.deepcopy(scanners)


def convert(list):
    opts = []
    for (x, y, z) in list:
        opts.append(
            [(x, y, z),
             (-x, y, z),
             (x, -y, z),
             (x, y, -z),
             (-x, -y, z),
             (-x, y, -z),
             (x, -y, -z),
             (-x, -y, -z),
             (x, z, y),
             (-x, z, y),
             (x, -z, y),
             (x, z, -y),
             (-x, -z, y),
             (-x, z, -y),
             (x, -z, -y),
             (-x, -z, -y),
             (y, x, z),
             (-y, x, z),
             (y, -x, z),
             (y, x, -z),
             (-y, -x, z),
             (-y, x, -z),
             (y, -x, -z),
             (-y, -x, -z),
             (y, z, x),
             (-y, z, x),
             (y, -z, x),
             (y, z, -x),
             (-y, -z, x),
             (-y, z, -x),
             (y, -z, -x),
             (-y, -z, -x),
             (z, x, y),
             (-z, x, y),
             (z, -x, y),
             (z, x, -y),
             (-z, -x, y),
             (-z, x, -y),
             (z, -x, -y),
             (-z, -x, -y),
             (z, y, x),
             (-z, y, x),
             (z, -y, x),
             (z, y, -x),
             (-z, -y, x),
             (-z, y, -x),
             (z, -y, -x),
             (-z, -y, -x)]
        )
    newopts = []
    for j in range(len(opts[0])):
        newopts.append([])
    for i in range(len(opts)):
        for j in range(len(opts[0])):
            newopts[j].append(opts[i][j])
    return newopts


def orient_around(list, pos):
    (x, y, z) = list[pos]
    newlist = []
    for index, item in enumerate(list):
        if index == pos:
            newlist.append((0, 0, 0))
        else:
            newlist.append((item[0]-x, item[1]-y, item[2]-z))
    return newlist


def find_a_pair(scanners):
    for index1, first in enumerate(scanners):
        for index2, second in enumerate(scanners):
            if index1 != index2:
                second = (convert(second))
                backupfirst = copy.deepcopy(first)
                for f in range(len(first)):
                    first = orient_around(backupfirst, f)
                    for index, secitem in enumerate(second):
                        for s in range(len(secitem)):
                            seccheck = orient_around(secitem, s)
                            present = 0
                            for fitem in first:
                                if fitem in seccheck:
                                    present += 1
                            if present > 11:
                                return (index1, index2, first, seccheck, index)


while (len(scanners)) > 1:
    (index1, index2, first, seccheck, index) = find_a_pair(scanners)

    beacons = []
    for f in first:
        beacons.append(f)
    for s in seccheck:
        if s not in beacons:
            beacons.append(s)

    item = scanners[index1]
    item2 = scanners[index2]
    scanners.remove(item)
    scanners.remove(item2)
    scanners.append(beacons)

    print(len(scanners))

print(len(scanners[0]))


# filename = "input/day19inputb.txt"
# file = open(filename, "r")
# file = file.readlines()

# beacons = eval(file[0].replace('\n', ''))


# def reorient_around(list, b):
#     (x, y, z) = b
#     a = x-list[0][0]
#     b = y-list[0][1]
#     c = z-list[0][2]
#     newlist = []
#     for l in list:
#         newlist.append((l[0]+a, l[1]+b, l[2]+c))
#     return list


# for index, s in enumerate(scannerscopy):
#     print(index)
#     options = convert(s)
#     for item in options:
#         for b in beacons:
#             copyitem = reorient_around(copy.deepcopy(item), b)
#             count = 0
#             for b in beacons:
#                 if b in copyitem:
#                     count += 1
#             if count > 11:
#                 print(index, 'found')
