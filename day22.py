from collections import Counter
import collections
import re
import fileinput
from datetime import datetime
import copy

rules = []

filename = "input/day22input.txt"
file = open(filename, "r")
file = file.readlines()
for f in file:
    f = f.replace('\n', '').replace(' x=', ',').replace(
        '..', ',').replace(',y=', ',').replace(',z=', ',').split(',')
    rules.append((f[0], int(f[1]), int(f[2]), int(
        f[3]), int(f[4]), int(f[5]), int(f[6])))


filename = "input/day22input.txt"
on_off_lst = []
reboot_steps = []

for lines in open(filename):
    on_off, steps = lines[:3].strip(), [lines.replace(
        "\n", "").replace("on ", "").replace("off ", "")]
    on_off_lst += [on_off]
    reboot_steps += steps


valid_reboot_steps = []
for i in range(len(reboot_steps)):
    temp_x, temp_y, temp_z = reboot_steps[i].split(",")
    x = temp_x[temp_x.find("=")+1:].split("..")
    y = temp_y[temp_y.find("=") + 1:].split("..")
    z = temp_z[temp_z.find("=") + 1:].split("..")
    if int(x[0]) < -50 or int(x[1]) > 50 or int(y[0]) < -50 or int(y[1]) > 50 or int(z[0]) < -50 or int(z[1]) > 50:
        continue
    else:
        valid_reboot_steps += [[x, y, z]]

memo = {}
for i in range(len(valid_reboot_steps)):
    for a in range(int(valid_reboot_steps[i][0][0]), int(valid_reboot_steps[i][0][1])+1, 1):
        for b in range(int(valid_reboot_steps[i][1][0]), int(valid_reboot_steps[i][1][1])+1, 1):
            for c in range(int(valid_reboot_steps[i][2][0]), int(valid_reboot_steps[i][2][1])+1, 1):
                if (a, b, c) in memo:
                    if memo[a, b, c] == "on" and on_off_lst[i] == "off":
                        memo[a, b, c] = "off"
                    elif memo[a, b, c] == "off" and on_off_lst[i] == "on":
                        memo[a, b, c] = "on"
                else:
                    memo[a, b, c] = on_off_lst[i]


print(Counter(memo.values())['on'])


cubes = collections.Counter()
for line in open("input/day22input.txt", "r"):
    nsgn = 1 if line.split()[0] == "on" else -1
    nx0, nx1, ny0, ny1, nz0, nz1 = map(int, re.findall("-?\d+", line))

    update = collections.Counter()
    for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
        ix0 = max(nx0, ex0)
        ix1 = min(nx1, ex1)
        iy0 = max(ny0, ey0)
        iy1 = min(ny1, ey1)
        iz0 = max(nz0, ez0)
        iz1 = min(nz1, ez1)
        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn
    if nsgn > 0:
        update[(nx0, nx1, ny0, ny1, nz0, nz1)] += nsgn
    cubes.update(update)

print(sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
          for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()))
