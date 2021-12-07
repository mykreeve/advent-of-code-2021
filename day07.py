from datetime import datetime
import math

filename = "input/day07input.txt"
file = open(filename, "r")
file = file.readlines()

for f in file:
    f = f.replace('\n', '').split(',')

now = datetime.now()
crabs = []
for c in f:
    crabs.append(int(c))


def get_fuel_required(list, dest):
    fuel = 0
    for l in list:
        fuel += abs(l-dest)
    return fuel


lowest = None
for a in range(max(crabs)):
    f = get_fuel_required(crabs, a)
    if not lowest:
        lowest = f
    elif f < lowest:
        lowest = f
    else:
        break

done = datetime.now()
print("Answer to part 1:", lowest)
print("Time taken:", done - now)


now = datetime.now()
def get_factorial_fuel(list, dest):
    fuel = 0
    for l in list:
        a = abs(l-dest)
        fuel += int(((a)*(a+1))/2)
    return fuel


lowest = None
for a in range(max(crabs)):
    f = get_factorial_fuel(crabs, a)
    if not lowest:
        lowest = f
    elif f < lowest:
        lowest = f
    else:
        break

done = datetime.now()
print("Answer to part 2:", lowest)
print("Time taken:", done - now)
