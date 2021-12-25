import copy

filename = "input/day25input.txt"
file = open(filename, "r")
file = file.readlines()

floor = {}
for y, f in enumerate(file):
    for x, ch in enumerate(f.replace('\n', '')):
        maxx = x
        maxy = y
        floor[(x, y)] = ch

prev = None
turns = 0


def do_east_moves(floor):
    new_floor = copy.deepcopy(floor)
    for y in range(0, maxy+1):
        for x in range(0, maxx+1):
            move_to = (x+1, y)
            if move_to[0] > maxx:
                move_to = (0, y)
            if floor[(x, y)] == '>':
                if floor[move_to] == '.':
                    new_floor[(x, y)] = '.'
                    new_floor[move_to] = '>'
    return new_floor


def do_south_moves(floor):
    new_floor = copy.deepcopy(floor)
    for y in range(0, maxy+1):
        for x in range(0, maxx+1):
            move_to = (x, y+1)
            if move_to[1] > maxy:
                move_to = (x, 0)
            if floor[(x, y)] == 'v':
                if floor[move_to] == '.':
                    new_floor[(x, y)] = '.'
                    new_floor[move_to] = 'v'
    return new_floor


def print_floor(floor):
    for y in range(0, maxy+1):
        for x in range(0, maxx+1):
            print(floor[(x, y)], end='')
        print()


while prev != floor:
    prev = copy.deepcopy(floor)
    floor = do_east_moves(floor)
    floor = do_south_moves(floor)
    print_floor(floor)
    print()
    turns += 1

print(turns)
