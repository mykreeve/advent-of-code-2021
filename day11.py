from datetime import datetime
import copy

filename = "input/day11input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()
octopuses = {}
grid_size = len(file)

for y, f in enumerate(file):
    for x, ch in enumerate(f.replace('\n', '')):
        octopuses[(x, y)] = int(ch)

def inc_by_one(grid):
    new_grid = {}
    for y in range(grid_size):
        for x in range(grid_size):
            new_grid[(x, y)] = grid[(x, y)] + 1
    return new_grid


def do_triggers(triggered, grid, count):
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[(x, y)] > 9 and (x, y) not in triggered:
                count += 1
                triggered.append((x, y))
                for n in neighbours:
                    if (x+n[0], y+n[1]) in grid:
                        grid[(x+n[0], y+n[1])] += 1
    return (triggered, grid, count)


def repeats_required(triggered, grid):
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[(x, y)] > 9 and (x, y) not in triggered:
                return True
    return False


def reduce_states_to_zero(grid):
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[(x, y)] > 9:
                grid[(x, y)] = 0
    return grid


def print_grid(grid):
    for y in range(grid_size):
        for x in range(grid_size):
            print(grid[(x, y)], end='')
        print('')
    return grid


count = 0

for step in range(100):
    octopuses = inc_by_one(octopuses)
    triggered = []
    triggered, octopuses, count = do_triggers(triggered, octopuses, count)
    while repeats_required(triggered, octopuses):
        triggered, octopuses, count = do_triggers(triggered, octopuses, count)
    octopuses = reduce_states_to_zero(octopuses)

done = datetime.now()
print("Answer to part 1:", count)
print("Time taken:", done - now)

now = datetime.now()
turn_count = 0
turn = 100
while turn_count != 100:
    turn_count = 0
    octopuses = inc_by_one(octopuses)
    triggered = []
    triggered, octopuses, turn_count = do_triggers(
        triggered, octopuses, turn_count)
    while repeats_required(triggered, octopuses):
        triggered, octopuses, turn_count = do_triggers(
            triggered, octopuses, turn_count)
    octopuses = reduce_states_to_zero(octopuses)
    turn += 1

done = datetime.now()
print("Answer to part 2:", turn)
print("Time taken:", done - now)