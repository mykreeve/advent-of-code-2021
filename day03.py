from datetime import datetime
import copy

filename = "input/day03input.txt"
file = open(filename, "r")
file = file.readlines()

numbers = []
for f in file:
    n = f.replace('\n', '')
    numbers.append(n)

now = datetime.now()
counter = {}
gamma = ''
epsilon = ''
for n in numbers:
    for pos, c in enumerate(n):
        if pos not in counter:
            counter[pos] = {}
        if c not in counter[pos]:
            counter[pos][c] = 1
        else:
            counter[pos][c] += 1
for c in counter:
    best = None
    bestVal = 0
    for n in counter[c]:
        if counter[c][n] > bestVal:
            best = n
            bestVal = counter[c][n]
    gamma += best
for g in gamma:
    if g == '0':
        epsilon += '1'
    else:
        epsilon += '0'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

done = datetime.now()
print("Answer to part 1:", gamma * epsilon)
print("Time taken:", done - now)


def get_most_common_at_position(input, position, equal_return):
    vals = {}
    for n in input:
        if n[position] not in vals:
            vals[n[position]] = 1
        else:
            vals[n[position]] += 1
    best = None
    bestVal = 0
    for v in vals:
        if vals[v] > bestVal:
            bestVal = vals[v]
            best = v
        elif vals[v] == bestVal:
            best = equal_return
    return best

def get_least_common_at_position(input, position, equal_return):
    vals = {}
    for n in input:
        if n[position] not in vals:
            vals[n[position]] = 1
        else:
            vals[n[position]] += 1
    least = None
    leastVal = 999999
    for v in vals:
        if vals[v] < leastVal:
            leastVal = vals[v]
            least = v
        elif vals[v] == leastVal:
            least = equal_return
    return least

def filter_by_value_position(input, value, position):
    retained = []
    for i in input:
        if i[position] == value:
            retained.append(i)
    return retained


now = datetime.now()
find_oxygen = copy.deepcopy(numbers)
for n in range(len(numbers[0])):
    value = get_most_common_at_position(find_oxygen, n, '1')
    find_oxygen = filter_by_value_position(find_oxygen, value, n)
    if (len(find_oxygen)) == 1:
        find_oxygen = find_oxygen[0]

stop = False
find_co2 = copy.deepcopy(numbers)
for n in range(len(numbers[0])):
    value = get_least_common_at_position(find_co2, n, '0')
    find_co2 = filter_by_value_position(find_co2, value, n)
    if (len(find_co2)) == 1:
        find_co2 = find_co2[0]
        stop = True
        if stop:
            break

done = datetime.now()
print("Answer to part 2:", int(find_oxygen, 2) * int(find_co2, 2))
print("Time taken:", done - now)