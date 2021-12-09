from datetime import datetime
import math

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

now = datetime.now()

numbers_lookup = {
    0: ['b', 'bl', 'br', 't', 'tl', 'tr'],
    1: ['br', 'tr'],
    2: ['b', 'bl', 'm', 't', 'tr'],
    3: ['b', 'br', 'm', 't', 'tr'],
    4: ['br', 'm', 'tl', 'tr'],
    5: ['b', 'br', 'm', 't', 'tl'],
    6: ['b', 'bl', 'br', 'm', 't', 'tl'],
    7: ['br', 't', 'tr'],
    8: ['b', 'bl', 'br', 'm', 't', 'tl', 'tr'],
    9: ['b', 'br', 'm', 't', 'tl', 'tr'],
}

filename = "input/day08input.txt"
file = open(filename, "r")
file = file.readlines()

displays = []

for f in file:
    f = f.replace('\n', '').split(' | ')
    data = f[0].split(' ')
    code = f[1].split(' ')
    displays.append({'data': data, 'code': code})

count = 0
for d in displays:
    for c in d['code']:
        if len(c) in [2, 3, 4, 7]:
            count += 1

done = datetime.now()
print("Answer to part 2:", count)
print("Time taken:", done - now)

now = datetime.now()

score = 0

for d in displays:
    # t (8), tl (6), tr (8), m (7), bl (4), br (9), b (7)
    lookup = {}
    lengths = {}
    frequency = {}
    for c in d['data']:
        if len(c) not in lengths:
            lengths[len(c)] = [c]
        else:
            lengths[len(c)].append(c)
        for ch in c:
            if ch not in frequency:
                frequency[ch] = 1
            else:
                frequency[ch] += 1
    analysis_frequency = {}
    for f in frequency:
        if frequency[f] not in analysis_frequency:
            analysis_frequency[frequency[f]] = [f]
        else:
            analysis_frequency[frequency[f]].append(f)
    lookup[analysis_frequency[4][0]] = 'bl'
    lookup[analysis_frequency[6][0]] = 'tl'
    lookup[analysis_frequency[9][0]] = 'br'
    # print (lookup, lengths)
    for i in lengths[2][0]:
        if i not in lookup:
            lookup[i] = 'tr'
    for i in lengths[4][0]:
        if i not in lookup:
            lookup[i] = 'm'
    for i in lengths[3][0]:
        if i not in lookup:
            lookup[i] = 't'
    for i in 'abcdefg':
        if i not in lookup:
            lookup[i] = 'b'
    converted_digits = []
    for cd in d['code']:
        digit = []
        for ch in cd:
            digit.append(lookup[ch])
        digit.sort()
        converted_digits.append(digit)
    num = ''
    for cd in converted_digits:
        for n in numbers_lookup:
            if cd == numbers_lookup[n]:
                num = num + str(n)
    score += (int(num))

done = datetime.now()
print("Answer to part 2:", score)
print("Time taken:", done - now)
