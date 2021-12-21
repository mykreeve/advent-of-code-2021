from datetime import datetime
import copy

filename = "input/day21input.txt"
file = open(filename, "r")
file = file.readlines()

for f in file:
    if 'Player 1 starting position: ' in f:
        f = f.replace('Player 1 starting position: ', '').replace('\n', '')
        player1init = int(f)
        player1pos = int(f)
    if 'Player 2 starting position: ' in f:
        f = f.replace('Player 2 starting position: ', '').replace('\n', '')
        player2init = int(f)
        player2pos = int(f)

player1score = 0
player2score = 0
turn = 1
dice = 0
rolls = 0


def roll_dice(d, rolls):
    rolls += 1
    if d < 100:
        return (d+1, rolls)
    else:
        return (1, rolls)


def move(pos, d):
    pos = pos + d
    while pos > 10:
        pos = pos - 10
    return pos


while player1score < 1000 and player2score < 1000:
    if turn == 1:
        (dice, rolls) = roll_dice(dice, rolls)
        player1pos = move(player1pos, dice)
        (dice, rolls) = roll_dice(dice, rolls)
        player1pos = move(player1pos, dice)
        (dice, rolls) = roll_dice(dice, rolls)
        player1pos = move(player1pos, dice)
        player1score += player1pos
        turn = 2
    elif turn == 2:
        (dice, rolls) = roll_dice(dice, rolls)
        player2pos = move(player2pos, dice)
        (dice, rolls) = roll_dice(dice, rolls)
        player2pos = move(player2pos, dice)
        (dice, rolls) = roll_dice(dice, rolls)
        player2pos = move(player2pos, dice)
        player2score += player2pos
        turn = 1

if player2score < 1000:
    print(player2score * rolls)
else:
    print(player1score * rolls)

distro = {}
for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        for c in [1, 2, 3]:
            if a+b+c not in distro:
                distro[a+b+c] = 1
            else:
                distro[a+b+c] += 1

p1wins = 0
p2wins = 0

pos = {(player1init, player2init, 1): {(0, 0): 1}}

while len(pos) > 0:
    newpos = {}
    for p in pos:
        (player1pos, player2pos, turn) = p
        for s in pos[p]:
            (player1score, player2score) = s
            frequency = pos[p][s]
            # print('p1pos', player1pos, 'p2pos',  player2pos, 'turn', turn,
            #       'p1score', player1score, 'p2score', player2score, 'freq', frequency)
            if turn == 1:
                for d in distro:
                    movement = d
                    freq = distro[d]
                    newp1pos = player1pos + movement
                    if newp1pos > 10:
                        newp1pos -= 10
                    newp1score = player1score + newp1pos
                    if newp1score >= 21:
                        p1wins += (frequency * freq)
                    else:
                        if (newp1pos, player2pos, 2) not in newpos:
                            newpos[(newp1pos, player2pos, 2)] = {
                                (newp1score, player2score): frequency*freq}
                        else:
                            if (newp1score, player2score) not in newpos[(newp1pos, player2pos, 2)]:
                                newpos[(newp1pos, player2pos, 2)][(
                                    newp1score, player2score)] = frequency*freq
                            else:
                                newpos[(newp1pos, player2pos, 2)][(
                                    newp1score, player2score)] += (frequency*freq)
            elif turn == 2:
                for d in distro:
                    movement = d
                    freq = distro[d]
                    newp2pos = player2pos + movement
                    if newp2pos > 10:
                        newp2pos -= 10
                    newp2score = player2score + newp2pos
                    if newp2score >= 21:
                        p2wins += (frequency * freq)
                    else:
                        if (player1pos, newp2pos, 1) not in newpos:
                            newpos[(player1pos, newp2pos, 1)] = {
                                (player1score, newp2score): frequency*freq}
                        else:
                            if (player1score, newp2score) not in newpos[(player1pos, newp2pos, 1)]:
                                newpos[(player1pos, newp2pos, 1)][(
                                    player1score, newp2score)] = frequency*freq
                            else:
                                newpos[(player1pos, newp2pos, 1)][(
                                    player1score, newp2score)] += (frequency*freq)
    pos = newpos

if p1wins > p2wins:
    print(p1wins)
else:
    print(p2wins)
