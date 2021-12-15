from datetime import datetime
import heapq

filename = "input/day15input.txt"
file = open(filename, "r")
file = file.readlines()

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
        if new_loc in grid and new_loc not in visited:
            visited.append(new_loc)
            heapq.heappush(
                queue, (score + grid[new_loc], new_loc, visited))


score = 0
pos = (0, 0)
visited = []
queue = []

add_options_to_queue(score, pos, visited)

while pos != (maxx, maxy):
    (score, pos, visited) = heapq.heappop(queue)
    add_options_to_queue(score, pos, visited)

print(score)
