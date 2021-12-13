from datetime import datetime
import copy

filename = "input/day12input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()
routes = {}
for f in file:
    f = f.replace('\n', '').split('-')
    if f[0] not in routes:
        routes[f[0]] = [f[1]]
    else:
        routes[f[0]].append(f[1])
    if f[1] not in routes:
        routes[f[1]] = [f[0]]
    else:
        routes[f[1]].append(f[0])

finder = [['start']]
final_routes = 0


def get_current_location(f):
    return f[len(f)-1]


while len(finder) > 0:
    eval = finder.pop()
    loc = get_current_location(eval)
    if loc == 'end':
        final_routes += 1
    else:
        for l in routes[loc]:
            if (l.isupper()) or (l not in eval):
                tempeval = copy.deepcopy(eval)
                tempeval.append(l)
                finder.append(tempeval)


done = datetime.now()
print("Answer to part 1:", final_routes)
print("Time taken:", done - now)

now = datetime.now()
finder = [{'route': ['start'], 'smallvisit': ''}]
final_routes = 0


def get_current_location(f):
    return f[len(f)-1]


while len(finder) > 0:
    eval = finder.pop()
    loc = get_current_location(eval['route'])
    if loc == 'end':
        final_routes += 1
    else:
        for l in routes[loc]:
            if (l.isupper()) or (l not in eval['route']) or (l.islower() and eval['smallvisit'] == '') and (l != 'start'):
                tempeval = copy.deepcopy(eval)
                if (l in eval['route']) and (l.islower()) and (eval['smallvisit'] == ''):
                    tempeval['smallvisit'] = l
                tempeval['route'].append(l)
                finder.append(tempeval)

done = datetime.now()
print("Answer to part 2:", final_routes)
print("Time taken:", done - now)