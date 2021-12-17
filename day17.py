from datetime import datetime
import heapq

filename = "input/day17input.txt"
file = open(filename, "r")
file = file.readlines()
f = file[0]
f = f.replace('\n', '').replace('target area: x=',
                                '').replace(', y=', '..').split('..')

targetminx = int(f[0])
targetmaxx = int(f[1])
targetminy = int(f[2])
targetmaxy = int(f[3])
highesty = 0
count = 0

for y in range(-targetminy*2, (targetminy-1)*2, -1):
    for x in range(-targetmaxx*2, targetmaxx*2, 1):
        speed = (x, y)
        loc = (x, y)
        trajectory = [(x, y)]
        entered = False
        if loc[0] >= targetminx and loc[0] <= targetmaxx and loc[1] >= targetminy and loc[1] <= targetmaxy:
            entered = True
        while loc[0] < targetmaxx and loc[1] > targetminy:
            if speed[0] > 0:
                newxspeed = speed[0] - 1
            elif speed[0] < 0:
                newxspeed = speed[0] + 1
            else:
                newxspeed = 0
            newyspeed = speed[1] - 1
            speed = (newxspeed, newyspeed)
            loc = (loc[0] + speed[0], loc[1] + speed[1])
            trajectory.append(loc)
            if loc[0] >= targetminx and loc[0] <= targetmaxx and loc[1] >= targetminy and loc[1] <= targetmaxy:
                entered = True
        if entered:
            count += 1
            for t in trajectory:
                if t[1] > highesty:
                    highesty = t[1]

print('Answer to part 1:',highesty)
print('Answer to part 2:',count)
