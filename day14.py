from datetime import datetime
import copy

filename = "input/day14input.txt"
file = open(filename, "r")
file = file.readlines()

rules = {}
now = datetime.now()

for f in file:
    if '->' in f:
        f = f.replace('\n', '').split(' -> ')
        rules[f[0]] = f[1]
    elif f != '\n':
        chem = f.replace('\n', '')

chemstruct = {}

for index, c in enumerate(chem):
    if index+1 < len(chem):
        if c not in chemstruct:
            chemstruct[c] = {chem[index+1]: 1}
        else:
            if chem[index+1] not in chemstruct[c]:
                chemstruct[c][chem[index+1]] = 1
            else:
                chemstruct[c][chem[index+1]] += 1
    else:
        chemstruct[c] = {'': 1}


def eval_chemstruct(c):
    counts = {}
    for item in c:
        count = 0
        for l in c[item]:
            count += c[item][l]
        counts[item] = count
    return counts


turn = 0
while turn < 10:
    newchem = {}
    for c in chemstruct:
        for link in chemstruct[c]:
            number = chemstruct[c][link]
            if c not in newchem:
                newchem[c] = {}
            if c+link in rules:
                insert = rules[c+link]
            else:
                insert = ''
            if link and insert not in newchem:
                newchem[insert] = {}
            if insert not in newchem[c]:
                newchem[c][insert] = number
            else:
                newchem[c][insert] += number
            if link and link not in newchem[insert]:
                newchem[insert][link] = number
            elif link:
                newchem[insert][link] += number
    chemstruct = newchem
    turn += 1

eval = eval_chemstruct(chemstruct)

lowest = 9999999999999999
highest = 0

for l in eval:
    if eval[l] > highest:
        highest = eval[l]
    if eval[l] < lowest:
        lowest = eval[l]

done = datetime.now()
print("Answer to part 1:", highest-lowest)
print("Time taken:", done - now)
now = datetime.now()

while turn < 40:
    newchem = {}
    for c in chemstruct:
        for link in chemstruct[c]:
            number = chemstruct[c][link]
            if c not in newchem:
                newchem[c] = {}
            if c+link in rules:
                insert = rules[c+link]
            else:
                insert = ''
            if link and insert not in newchem:
                newchem[insert] = {}
            if insert not in newchem[c]:
                newchem[c][insert] = number
            else:
                newchem[c][insert] += number
            if link and link not in newchem[insert]:
                newchem[insert][link] = number
            elif link:
                newchem[insert][link] += number
    chemstruct = newchem
    turn += 1

eval = eval_chemstruct(chemstruct)

lowest = 99999999999999999
highest = 0

for l in eval:
    if eval[l] > highest:
        highest = eval[l]
    if eval[l] < lowest:
        lowest = eval[l]

done = datetime.now()
print("Answer to part 2:", highest-lowest)
print("Time taken:", done - now)