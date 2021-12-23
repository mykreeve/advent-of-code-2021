import heapq
import copy

filename = "input/day23input.txt"
file = open(filename, "r")
file = file.readlines()

rooms = [[], [], [], []]

for index, f in enumerate(file):
    if index in [2, 3]:
        place = 0
        for ch in f:
            if ch not in ['#', '\n', ' ']:
                rooms[place].append(ch)
                place += 1

orig_rooms = copy.deepcopy(rooms)

corridor = ['.', '.', '0', '.', '1', '.', '2', '.', '3', '.', '.']

queue = []
visited = []

heapq.heappush(
    queue, (0, corridor, rooms))

targets = ['A', 'B', 'C', 'D']

move_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def can_leave_rooms(score, corridor, rooms):
    # are there any amphis in rooms which can move into corridor or another room?
    options = []
    for room_index, r in enumerate(rooms):
        # amphi in pos 1 in room, and needs to move
        if r[0] in ['A', 'B', 'C', 'D']:
            can_move = True
            # amphi already in right room, but need to check if other amphi needs to move!
            if room_index == targets.index(r[0]):
                can_move = False
                # amphi in right room, but needs to get out of the way
                if r[1] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[1]):
                    can_move = True
            if can_move:
                # can amphi move into corridor
                options_to_move_to = []
                entering_corridor_pos = corridor.index(str(room_index))
                # move left?
                test_pos = entering_corridor_pos - 1
                can_go_left = True
                distance = 2
                while test_pos >= 0 and can_go_left:
                    if corridor[test_pos] in ['.', '0', '1', '2']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_left = False
                    test_pos -= 1
                    distance += 1
                # move right?
                test_pos = entering_corridor_pos + 1
                can_go_right = True
                distance = 2
                while test_pos <= 10 and can_go_right:
                    if corridor[test_pos] in ['.', '1', '2', '3']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_right = False
                    test_pos += 1
                    distance += 1
                for o in options_to_move_to:
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_index][0] = '.'
                    new_corridor = copy.deepcopy(corridor)
                    new_corridor[o[1]] = r[0]
                    new_score = copy.deepcopy(score)
                    new_score += (move_costs[r[0]] * o[0])
                    options.append((new_score, new_corridor, new_rooms))
                # can amphi move into its room?
                target_room_number = targets.index(r[0])
                if rooms[target_room_number][0] == '.':
                    # is corridor in between empty?
                    entering_corridor_pos = corridor.index(str(room_index))
                    exiting_corridor_pos = corridor.index(
                        str(target_room_number))
                    corridor_empty = True
                    distance = 2
                    if entering_corridor_pos < exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    elif entering_corridor_pos > exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos, -1):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    # if inner slot in room isn't empty, move to outer one... (and must already contain same)
                    if corridor_empty and rooms[target_room_number][1] == r[0]:
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][0] = '.'
                        new_rooms[target_room_number][0] = r[0]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[0]] * distance)
                        options.append((new_score, new_corridor, new_rooms))
                    # if inner slot in room is empty, go there instead
                    if corridor_empty and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][0] = '.'
                        new_rooms[target_room_number][1] = r[0]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[0]] * (distance+1))
                        options.append((new_score, new_corridor, new_rooms))
        # amphi in pos 2 in room, and able to get out
        if r[1] in ['A', 'B', 'C', 'D'] and r[0] == '.':
            should_move = True
            # amphi already in right room
            if room_index == targets.index(r[1]):
                should_move = False
            if should_move:
                # can amphi move into corridor
                options_to_move_to = []
                entering_corridor_pos = corridor.index(str(room_index))
                # move left?
                test_pos = entering_corridor_pos - 1
                can_go_left = True
                distance = 3
                while test_pos >= 0 and can_go_left:
                    if corridor[test_pos] in ['.', '0', '1', '2']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_left = False
                    test_pos -= 1
                    distance += 1
                # move right?
                test_pos = entering_corridor_pos + 1
                can_go_right = True
                distance = 3
                while test_pos <= 10 and can_go_right:
                    if corridor[test_pos] in ['.', '1', '2', '3']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_right = False
                    test_pos += 1
                    distance += 1
                for o in options_to_move_to:
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_index][1] = '.'
                    new_corridor = copy.deepcopy(corridor)
                    new_corridor[o[1]] = r[1]
                    new_score = copy.deepcopy(score)
                    new_score += (move_costs[r[1]] * o[0])
                    options.append((new_score, new_corridor, new_rooms))
                # can amphi move into its room?
                target_room_number = targets.index(r[1])
                if rooms[target_room_number][0] == '.':
                    # is corridor in between empty?
                    entering_corridor_pos = corridor.index(str(room_index))
                    exiting_corridor_pos = corridor.index(
                        str(target_room_number))
                    corridor_empty = True
                    distance = 3
                    if entering_corridor_pos < exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    elif entering_corridor_pos > exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos, -1):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    # if inner slot in room isn't empty, move to outer one...
                    if corridor_empty and rooms[target_room_number][1] == r[1]:
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][1] = '.'
                        new_rooms[target_room_number][0] = r[1]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[1]] * distance)
                        options.append((new_score, new_corridor, new_rooms))
                    # if inner slot in room is empty, go there instead
                    if corridor_empty and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][1] = '.'
                        new_rooms[target_room_number][1] = r[1]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[1]] * (distance+1))
                        options.append((new_score, new_corridor, new_rooms))
    return options


def can_leave_corridor(score, corridor, rooms):
    options = []
    for pos, c in enumerate(corridor):
        if c not in ['.', '0', '1', '2', '3'] and c in ['A', 'B', 'C', 'D']:
            # found an amphi in the corridor
            # is there space in its room?
            target_room_number = targets.index(c)
            if rooms[target_room_number][0] == '.':
                # there is space in its room. Is corridor empty?
                exiting_corridor_pos = corridor.index(
                    str(target_room_number))
                distance = 1
                corridor_empty = True
                if exiting_corridor_pos < pos:
                    for p in range(pos-1, exiting_corridor_pos, -1):
                        if corridor[p] not in ['.', '0', '1', '2', '3']:
                            corridor_empty = False
                        distance += 1
                else:
                    for p in range(pos+1, exiting_corridor_pos, 1):
                        if corridor[p] not in ['.', '0', '1', '2', '3']:
                            corridor_empty = False
                        distance += 1
                if corridor_empty:
                    # if possible, move into outer room position
                    if rooms[target_room_number][1] == '.':
                        new_corridor = copy.deepcopy(corridor)
                        new_corridor[pos] = '.'
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[target_room_number][1] = c
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[c] * (distance + 2))
                        options.append((new_score, new_corridor, new_rooms))
                    # otherwise, only move into inner room position if outer position is the same type
                    elif rooms[target_room_number][1] == c:
                        new_corridor = copy.deepcopy(corridor)
                        new_corridor[pos] = '.'
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[target_room_number][0] = c
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[c] * (distance + 1))
                        options.append((new_score, new_corridor, new_rooms))
    return options


while len(queue) > 0:
    score, corridor, rooms = heapq.heappop(queue)
    if (corridor, rooms) not in visited:
        visited.append((corridor, rooms))
        if rooms == [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]:
            print(score)
        options = can_leave_rooms(score, corridor, rooms)
        more_options = can_leave_corridor(score, corridor, rooms)
        for o in options:
            nscore, ncorridor, nrooms = o
            if (ncorridor, nrooms) not in visited and (nscore, ncorridor, nrooms) not in queue:
                heapq.heappush(queue, (nscore, ncorridor, nrooms))
        for o in more_options:
            nscore, ncorridor, nrooms = o
            if (ncorridor, nrooms) not in visited and (nscore, ncorridor, nrooms) not in queue:
                heapq.heappush(queue, (nscore, ncorridor, nrooms))
        # print(score, len(queue), len(visited))


def can_leave_bigger_rooms(score, corridor, rooms):
    # are there any amphis in rooms which can move into corridor or another room?
    options = []
    for room_index, r in enumerate(rooms):
        # amphi in pos 1 in room, and needs to move
        if r[0] in ['A', 'B', 'C', 'D']:
            can_move = True
            # amphi already in right room, but need to check if other amphi needs to move!
            if room_index == targets.index(r[0]):
                can_move = False
                # amphi in right room, but needs to get out of the way
                if r[1] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[1]) or r[2] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[2]) or r[3] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[3]):
                    can_move = True
            if can_move:
                # can amphi move into corridor
                options_to_move_to = []
                entering_corridor_pos = corridor.index(str(room_index))
                # move left?
                test_pos = entering_corridor_pos - 1
                can_go_left = True
                distance = 2
                while test_pos >= 0 and can_go_left:
                    if corridor[test_pos] in ['.', '0', '1', '2']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_left = False
                    test_pos -= 1
                    distance += 1
                # move right?
                test_pos = entering_corridor_pos + 1
                can_go_right = True
                distance = 2
                while test_pos <= 10 and can_go_right:
                    if corridor[test_pos] in ['.', '1', '2', '3']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_right = False
                    test_pos += 1
                    distance += 1
                for o in options_to_move_to:
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_index][0] = '.'
                    new_corridor = copy.deepcopy(corridor)
                    new_corridor[o[1]] = r[0]
                    new_score = copy.deepcopy(score)
                    new_score += (move_costs[r[0]] * o[0])
                    options.append((new_score, new_corridor, new_rooms))
                # can amphi move into its room?
                target_room_number = targets.index(r[0])
                if rooms[target_room_number][0] == '.':
                    # is corridor in between empty?
                    entering_corridor_pos = corridor.index(str(room_index))
                    exiting_corridor_pos = corridor.index(
                        str(target_room_number))
                    corridor_empty = True
                    distance = 2
                    if entering_corridor_pos < exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    elif entering_corridor_pos > exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos, -1):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    # if inner slot in room isn't empty, move to outer one... (and must already contain same)
                    if corridor_empty and rooms[target_room_number][3] == r[0] and rooms[target_room_number][2] == r[0] and rooms[target_room_number][1] == r[0]:
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][0] = '.'
                        new_rooms[target_room_number][0] = r[0]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[0]] * distance)
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[0] and rooms[target_room_number][2] == r[0] and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][0] = '.'
                        new_rooms[target_room_number][1] = r[0]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[0]] * (distance+1))
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[0] and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][0] = '.'
                        new_rooms[target_room_number][2] = r[0]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[0]] * (distance+2))
                        options.append((new_score, new_corridor, new_rooms))
                    # if inner slot in room is empty, go there instead
                    if corridor_empty and rooms[target_room_number][3] == '.' and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][0] = '.'
                        new_rooms[target_room_number][3] = r[0]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[0]] * (distance+3))
                        options.append((new_score, new_corridor, new_rooms))
        # amphi in pos 2 in room, and able to get out
        if r[1] in ['A', 'B', 'C', 'D'] and r[0] == '.':
            can_move = True
            # amphi already in right room, but need to check if other amphi needs to move!
            if room_index == targets.index(r[1]):
                can_move = False
                # amphi in right room, but needs to get out of the way
                if r[2] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[2]) or r[3] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[3]):
                    can_move = True
            if can_move:
                # can amphi move into corridor
                options_to_move_to = []
                entering_corridor_pos = corridor.index(str(room_index))
                # move left?
                test_pos = entering_corridor_pos - 1
                can_go_left = True
                distance = 3
                while test_pos >= 0 and can_go_left:
                    if corridor[test_pos] in ['.', '0', '1', '2']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_left = False
                    test_pos -= 1
                    distance += 1
                # move right?
                test_pos = entering_corridor_pos + 1
                can_go_right = True
                distance = 3
                while test_pos <= 10 and can_go_right:
                    if corridor[test_pos] in ['.', '1', '2', '3']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_right = False
                    test_pos += 1
                    distance += 1
                for o in options_to_move_to:
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_index][1] = '.'
                    new_corridor = copy.deepcopy(corridor)
                    new_corridor[o[1]] = r[1]
                    new_score = copy.deepcopy(score)
                    new_score += (move_costs[r[1]] * o[0])
                    options.append((new_score, new_corridor, new_rooms))
                # can amphi move into its room?
                target_room_number = targets.index(r[1])
                if rooms[target_room_number][0] == '.':
                    # is corridor in between empty?
                    entering_corridor_pos = corridor.index(str(room_index))
                    exiting_corridor_pos = corridor.index(
                        str(target_room_number))
                    corridor_empty = True
                    distance = 3
                    if entering_corridor_pos < exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    elif entering_corridor_pos > exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos, -1):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    # if inner slot in room isn't empty, move to outer one...
                    if corridor_empty and rooms[target_room_number][3] == r[1] and rooms[target_room_number][2] == r[1] and rooms[target_room_number][1] == r[1]:
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][1] = '.'
                        new_rooms[target_room_number][0] = r[1]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[1]] * distance)
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[1] and rooms[target_room_number][2] == r[1] and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][1] = '.'
                        new_rooms[target_room_number][1] = r[1]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[1]] * (distance+1))
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[1] and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][1] = '.'
                        new_rooms[target_room_number][2] = r[1]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[1]] * (distance+2))
                        options.append((new_score, new_corridor, new_rooms))
                    # if inner slot in room is empty, go there instead
                    if corridor_empty and rooms[target_room_number][3] == '.' and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][1] = '.'
                        new_rooms[target_room_number][3] = r[1]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[1]] * (distance+3))
                        options.append((new_score, new_corridor, new_rooms))
        # amphi in pos 3 in room, and able to get out
        if r[2] in ['A', 'B', 'C', 'D'] and r[0] == '.' and r[1] == '.':
            can_move = True
            # amphi already in right room, but need to check if other amphi needs to move!
            if room_index == targets.index(r[2]):
                can_move = False
                # amphi in right room, but needs to get out of the way
                if r[3] in ['A', 'B', 'C', 'D'] and room_index != targets.index(r[3]):
                    can_move = True
            if can_move:
                # can amphi move into corridor
                options_to_move_to = []
                entering_corridor_pos = corridor.index(str(room_index))
                # move left?
                test_pos = entering_corridor_pos - 1
                can_go_left = True
                distance = 4
                while test_pos >= 0 and can_go_left:
                    if corridor[test_pos] in ['.', '0', '1', '2']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_left = False
                    test_pos -= 1
                    distance += 1
                # move right?
                test_pos = entering_corridor_pos + 1
                can_go_right = True
                distance = 4
                while test_pos <= 10 and can_go_right:
                    if corridor[test_pos] in ['.', '1', '2', '3']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_right = False
                    test_pos += 1
                    distance += 1
                for o in options_to_move_to:
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_index][2] = '.'
                    new_corridor = copy.deepcopy(corridor)
                    new_corridor[o[1]] = r[2]
                    new_score = copy.deepcopy(score)
                    new_score += (move_costs[r[2]] * o[0])
                    options.append((new_score, new_corridor, new_rooms))
                # can amphi move into its room?
                target_room_number = targets.index(r[2])
                if rooms[target_room_number][0] == '.':
                    # is corridor in between empty?
                    entering_corridor_pos = corridor.index(str(room_index))
                    exiting_corridor_pos = corridor.index(
                        str(target_room_number))
                    corridor_empty = True
                    distance = 4
                    if entering_corridor_pos < exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    elif entering_corridor_pos > exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos, -1):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    # if inner slot in room isn't empty, move to outer one...
                    if corridor_empty and rooms[target_room_number][3] == r[2] and rooms[target_room_number][2] == r[2] and rooms[target_room_number][1] == r[2]:
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][2] = '.'
                        new_rooms[target_room_number][0] = r[2]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[2]] * distance)
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[2] and rooms[target_room_number][2] == r[2] and rooms[target_room_number][2] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][2] = '.'
                        new_rooms[target_room_number][1] = r[2]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[2]] * (distance+1))
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[2] and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][2] = '.'
                        new_rooms[target_room_number][2] = r[2]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[2]] * (distance+2))
                        options.append((new_score, new_corridor, new_rooms))
                    # if inner slot in room is empty, go there instead
                    if corridor_empty and rooms[target_room_number][3] == '.' and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][2] = '.'
                        new_rooms[target_room_number][3] = r[2]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[2]] * (distance+3))
                        options.append((new_score, new_corridor, new_rooms))
        # amphi in pos 4 in room, and able to get out
        if r[3] in ['A', 'B', 'C', 'D'] and r[0] == '.' and r[1] == '.' and r[2] == '.':
            can_move = True
            # amphi already in right room
            if room_index == targets.index(r[3]):
                can_move = False
            if can_move:
                # can amphi move into corridor
                options_to_move_to = []
                entering_corridor_pos = corridor.index(str(room_index))
                # move left?
                test_pos = entering_corridor_pos - 1
                can_go_left = True
                distance = 5
                while test_pos >= 0 and can_go_left:
                    if corridor[test_pos] in ['.', '0', '1', '2']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_left = False
                    test_pos -= 1
                    distance += 1
                # move right?
                test_pos = entering_corridor_pos + 1
                can_go_right = True
                distance = 5
                while test_pos <= 10 and can_go_right:
                    if corridor[test_pos] in ['.', '1', '2', '3']:
                        if corridor[test_pos] == '.':
                            options_to_move_to.append((distance, test_pos))
                    else:
                        can_go_right = False
                    test_pos += 1
                    distance += 1
                for o in options_to_move_to:
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_index][3] = '.'
                    new_corridor = copy.deepcopy(corridor)
                    new_corridor[o[1]] = r[3]
                    new_score = copy.deepcopy(score)
                    new_score += (move_costs[r[3]] * o[0])
                    options.append((new_score, new_corridor, new_rooms))
                # can amphi move into its room?
                target_room_number = targets.index(r[3])
                if rooms[target_room_number][0] == '.':
                    # is corridor in between empty?
                    entering_corridor_pos = corridor.index(str(room_index))
                    exiting_corridor_pos = corridor.index(
                        str(target_room_number))
                    corridor_empty = True
                    distance = 5
                    if entering_corridor_pos < exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    elif entering_corridor_pos > exiting_corridor_pos:
                        for p in range(entering_corridor_pos, exiting_corridor_pos, -1):
                            if corridor[p] not in ['.', '0', '1', '2', '3']:
                                corridor_empty = False
                            distance += 1
                    # if inner slot in room isn't empty, move to outer one...
                    if corridor_empty and rooms[target_room_number][3] == r[3] and rooms[target_room_number][2] == r[3] and rooms[target_room_number][1] == r[3]:
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][3] = '.'
                        new_rooms[target_room_number][0] = r[3]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[3]] * distance)
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[3] and rooms[target_room_number][2] == r[3] and rooms[target_room_number][2] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][3] = '.'
                        new_rooms[target_room_number][1] = r[3]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[3]] * (distance+1))
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == r[3] and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][3] = '.'
                        new_rooms[target_room_number][2] = r[3]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[3]] * (distance+2))
                        options.append((new_score, new_corridor, new_rooms))
                    # if inner slot in room is empty, go there instead
                    if corridor_empty and rooms[target_room_number][3] == '.' and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[room_index][3] = '.'
                        new_rooms[target_room_number][3] = r[3]
                        new_corridor = copy.deepcopy(corridor)
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[r[3]] * (distance+3))
                        options.append((new_score, new_corridor, new_rooms))
    return options


def can_leave_bigger_corridor(score, corridor, rooms):
    options = []
    for pos, c in enumerate(corridor):
        if c not in ['.', '0', '1', '2', '3'] and c in ['A', 'B', 'C', 'D']:
            # found an amphi in the corridor
            # is there space in its room?
            target_room_number = targets.index(c)
            if rooms[target_room_number][0] == '.':
                # there is space in its room. Is corridor empty?
                exiting_corridor_pos = corridor.index(
                    str(target_room_number))
                distance = 1
                corridor_empty = True
                if exiting_corridor_pos < pos:
                    for p in range(pos-1, exiting_corridor_pos, -1):
                        if corridor[p] not in ['.', '0', '1', '2', '3']:
                            corridor_empty = False
                        distance += 1
                else:
                    for p in range(pos+1, exiting_corridor_pos, 1):
                        if corridor[p] not in ['.', '0', '1', '2', '3']:
                            corridor_empty = False
                        distance += 1
                if corridor_empty:
                    # if possible, move into outer room position
                    if rooms[target_room_number][3] == c and rooms[target_room_number][2] == c and rooms[target_room_number][1] == c:
                        new_corridor = copy.deepcopy(corridor)
                        new_corridor[pos] = '.'
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[target_room_number][0] = c
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[c] * (distance + 1))
                        options.append((new_score, new_corridor, new_rooms))
                    if rooms[target_room_number][3] == c and rooms[target_room_number][2] == c and rooms[target_room_number][1] == '.':
                        new_corridor = copy.deepcopy(corridor)
                        new_corridor[pos] = '.'
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[target_room_number][1] = c
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[c] * (distance + 2))
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == c and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_corridor = copy.deepcopy(corridor)
                        new_corridor[pos] = '.'
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[target_room_number][2] = c
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[c] * (distance + 3))
                        options.append((new_score, new_corridor, new_rooms))
                    if corridor_empty and rooms[target_room_number][3] == '.' and rooms[target_room_number][2] == '.' and rooms[target_room_number][1] == '.':
                        new_corridor = copy.deepcopy(corridor)
                        new_corridor[pos] = '.'
                        new_rooms = copy.deepcopy(rooms)
                        new_rooms[target_room_number][3] = c
                        new_score = copy.deepcopy(score)
                        new_score += (move_costs[c] * (distance + 4))
                        options.append((new_score, new_corridor, new_rooms))
    return options


rooms = []

additional = [['D', 'D'], ['C', 'B'], ['B', 'A'], ['A', 'C']]
for index, o in enumerate(orig_rooms):
    rooms.append([o[0], additional[index][0], additional[index][1], o[1]])

# print(rooms)

corridor = ['.', '.', '0', '.', '1', '.', '2', '.', '3', '.', '.']

queue = []
visited = []

heapq.heappush(
    queue, (0, corridor, rooms))

while len(queue) > 0:
    score, corridor, rooms = heapq.heappop(queue)
    if (corridor, rooms) not in visited:
        visited.append((corridor, rooms))
        if rooms == [['A', 'A', 'A', 'A'], ['B', 'B', 'B', 'B'], ['C', 'C', 'C', 'C'], ['D', 'D', 'D', 'D']]:
            print(score)
            exit()
        options = can_leave_bigger_rooms(score, corridor, rooms)
        more_options = can_leave_bigger_corridor(score, corridor, rooms)
        for o in options:
            nscore, ncorridor, nrooms = o
            if (ncorridor, nrooms) not in visited and (nscore, ncorridor, nrooms) not in queue:
                heapq.heappush(queue, (nscore, ncorridor, nrooms))
        for o in more_options:
            nscore, ncorridor, nrooms = o
            if (ncorridor, nrooms) not in visited and (nscore, ncorridor, nrooms) not in queue:
                heapq.heappush(queue, (nscore, ncorridor, nrooms))
        # print(score, len(queue), len(visited), corridor, rooms)
