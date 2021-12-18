from datetime import datetime
import math
import time
import itertools

filename = "input/day18input.txt"
file = open(filename, "r")
file = file.readlines()

snail_numbers = []
for f in file:
    snail_numbers.append(f.replace('\n', ''))


def add_numbers(a, b):
    return('['+a+','+b+']')


def requires_explode(a):
    depth = 0
    for index, ch in enumerate(a):
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
        if depth == 5:
            return index
    return False


def requires_split(a):
    prev = None
    for index, ch in enumerate(a):
        if prev not in ['[', ']', ',', None] and ch not in ['[', ']', ',', None]:
            return index
        prev = ch
    return False


def do_split(a, pos):
    leftstring = a[:pos-1]
    mid = int(a[pos-1] + a[pos])
    mid = '[' + str(math.floor(mid/2)) + ',' + str(math.ceil(mid/2)) + ']'
    rightstring = a[pos+1:]
    return leftstring + mid + rightstring


def do_explode(a, pos):
    left_pos = pos
    explode_element = a[pos]
    pos += 1
    while a[pos] != ']':
        explode_element += a[pos]
        pos += 1
    right_pos = pos
    explode_element += ']'
    explode_element = explode_element.replace(
        '[', '').replace(']', '').split(',')
    # These numbers are from within the exploded element
    left_number = int(explode_element[0])
    right_number = int(explode_element[1])

    # print(explode_element, left_pos, right_pos)
    leftstring = a[:left_pos]
    rightstring = a[right_pos+1:]
    # print(leftstring + '0' + rightstring)
    going_left = left_pos-1
    number_to_left = False
    leftfound = False
    while going_left > 0 and not leftfound:
        if leftstring[going_left] not in ['[', ']', ',']:
            leftfound = True
            number_to_left = leftstring[going_left]
            if leftstring[going_left-1] not in ['[', ']', ',']:
                number_to_left = leftstring[going_left-1] + number_to_left
            number_to_left = (int(number_to_left))
        going_left -= 1

    going_right = 0
    number_to_right = False
    rightfound = False
    while going_right < len(rightstring) and not rightfound:
        if rightstring[going_right] not in ['[', ']', ',']:
            rightfound = True
            number_to_right = rightstring[going_right]
            if rightstring[going_right+1] not in ['[', ']', ',']:
                number_to_right += rightstring[going_right+1]
            number_to_right = (int(number_to_right))
        going_right += 1

    if leftfound:
        if number_to_left > 9:
            leftstring = leftstring[:going_left] + \
                str(number_to_left+left_number) + leftstring[going_left+2:]
        else:
            leftstring = leftstring[:going_left+1] + \
                str(number_to_left+left_number) + leftstring[going_left+2:]
    if rightfound:
        if number_to_right > 9:
            rightstring = rightstring[:going_right-1] + \
                str(number_to_right+right_number) + rightstring[going_right+1:]
        else:
            rightstring = rightstring[:going_right-1] + \
                str(number_to_right+right_number) + rightstring[going_right:]

    return leftstring + '0' + rightstring


number_of_numbers = len(snail_numbers)

working = snail_numbers[0]

for x in range(1, number_of_numbers):
    # print('adding')
    working = add_numbers(working, snail_numbers[x])
    # print(working)
    while requires_explode(working) or requires_split(working):
        while requires_explode(working):
            # print('explode')
            working = do_explode(working, requires_explode(working))
            # print(working)
        if requires_split(working):
            # print('split')
            working = do_split(working, requires_split(working))
            # print(working)
    # print(working)


def do_score_block(string):
    val = eval(string)
    return ((3*val[0]) + 2*val[1])


def evaluate_element(string):
    for index, ch in enumerate(string):
        if ch == '[':
            start = index
        if ch == ']':
            return (start, index+1)
    return None


def get_score(string):
    while ']' in string:
        (start, finish) = evaluate_element(string)
        value = do_score_block(string[start:finish])
        string = string[:start] + str(value) + string[finish:]
    return string


print(get_score(working))

best_score = 0

for n in itertools.permutations(range(100), 2):
    working = add_numbers(snail_numbers[n[0]], snail_numbers[n[1]])
    while requires_explode(working) or requires_split(working):
        while requires_explode(working):
            working = do_explode(working, requires_explode(working))
        if requires_split(working):
            working = do_split(working, requires_split(working))
    score = get_score(working)
    if int(score) > best_score:
        best_score = int(score)

print(best_score)
