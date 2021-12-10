from datetime import datetime
import math

filename = "input/day10input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()
closures = {
    '<': '>',
    '(': ')',
    '{': '}',
    '[': ']'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

score = 0
score2 = []

for line in file:
    expected = []
    good = True
    for ch in line:
        if ch == '<':
            expected.insert(0, '>')
        if ch == '{':
            expected.insert(0, '}')
        if ch == '[':
            expected.insert(0, ']')
        if ch == '(':
            expected.insert(0, ')')
        if ch == '>':
            if expected[0] == '>':
                expected.pop(0)
            else:
                # print('error: found > but expected ' + expected[0])
                good = False
                score += scores[ch]
                break
        if ch == '}':
            if expected[0] == '}':
                expected.pop(0)
            else:
                # print('error: found } but expected ' + expected[0])
                good = False
                score += scores[ch]
                break
        if ch == ']':
            if expected[0] == ']':
                expected.pop(0)
            else:
                # print('error: found ] but expected ' + expected[0])
                good = False
                score += scores[ch]
                break
        if ch == ')':
            if expected[0] == ')':
                expected.pop(0)
            else:
                # print('error: found ) but expected ' + expected[0])
                good = False
                score += scores[ch]
                break
    if good:
        line_complete_score = 0
        for c in expected:
            # print(c)
            line_complete_score *= 5
            line_complete_score += scores2[c]
            # print(line_complete_score)
        score2.append(line_complete_score)

done = datetime.now()
print("Answer to part 1:", score)
print("Time taken:", done - now)

now = datetime.now()
score2.sort()
print("Answer to part 2:", score2[math.floor(len(score2)/2)])
done = datetime.now()
print("Time taken:", done - now)
