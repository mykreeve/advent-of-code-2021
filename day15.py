from datetime import datetime
import heapq

filename = "input/day15input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()
grid = {}

for (y, row) in enumerate(file):
    for (x, ch) in enumerate(row.replace('\n', '')):
        grid[(x, y)] = int(ch)
        maxx = x
        maxy = y


def add_options_to_queue(score, pos, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in directions:
        new_loc = (pos[0]+d[0], pos[1]+d[1])
        if new_loc not in visited and new_loc in grid:
            visited.append(new_loc)
            heapq.heappush(
                queue, (score + grid[new_loc], new_loc, visited))


score = 0
pos = (0, 0)
visited = []
queue = []

add_options_to_queue(score, pos, visited)

while pos != (maxx, maxy):
    # print(len(queue))
    (score, pos, visited) = heapq.heappop(queue)
    add_options_to_queue(score, pos, visited)

done = datetime.now()
print("Answer to part 1:", score)
print("Time taken:", done - now)
now = datetime.now()

for y in range(maxy+1):
    for x in range(maxx+1):
        for i in range(1, 5):
            val = grid[(x, y)] + i
            if val >= 10:
                val -= 9
            grid[(((maxx+1)*i)+x, y)] = val
            newmaxx = ((maxx+1)*i)+x

for y in range(maxy+1):
    for x in range(newmaxx+1):
        for i in range(1, 5):
            val = grid[(x, y)] + i
            if val >= 10:
                val -= 9
            grid[(x, ((maxy+1)*i) + y)] = val
            newmaxy = ((maxy+1)*i) + y

score = 0
pos = (0, 0)
visited = []
queue = []

add_options_to_queue(score, pos, visited)

while pos != (newmaxx, newmaxy):
    (score, pos, visited) = heapq.heappop(queue)
    add_options_to_queue(score, pos, visited)

done = datetime.now()
print("Answer to part 2:", score)
print("Time taken:", done - now)
