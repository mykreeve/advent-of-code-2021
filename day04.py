from datetime import datetime
import copy

filename = "input/day04input.txt"
file = open(filename, "r")
file = file.readlines()

bingo_numbers = None
bingo_boards = []

curr_board = []
for index, f in enumerate(file):
	if index == 0:
		bingo_numbers = f.replace('\n','').split(',')
	elif index > 1:
		fproc = f.replace('\n','').lstrip().replace('  ',' ')
		if fproc == '':
			bingo_boards.append(curr_board)
			curr_board = []
		else:
			curr_board.append(fproc.split(' '))

eval_boards = copy.deepcopy(bingo_boards)

def mark_numbers(board, number):
	for row in range(len(board)):
		for item in range(len(board[row])):
			if board[row][item] == number:
				board[row][item] = 'X'
	return board

def evaluate_if_winner(board):
	for row in range(len(board)):
		eval = ''
		for item in range(len(board[row])):
			eval += board[row][item]
		if eval == 'XXXXX':
			return True
	for row in range(len(board[0])):
		eval = ''
		for item in range(len(board)):
			eval += board[item][row]
		if eval == 'XXXXX':
			return True
	return False

for b in bingo_numbers:
	for e in range(len(eval_boards)):
		eval_boards[e] = mark_numbers(eval_boards[e], b)
	for e in range(len(eval_boards)):
		win = evaluate_if_winner(eval_boards[e])
		if (win):
			win_board = e
			last_number = b
			break
	if (win):
		break

score = 0
for row in range(len(eval_boards[win_board])):
	for item in range(len(eval_boards[win_board][row])):
		if eval_boards[win_board][row][item] != 'X':
			score += int(eval_boards[win_board][row][item])

score *= int(last_number)

print (score)


eval_boards = copy.deepcopy(bingo_boards)

found = False
for b in bingo_numbers:
	for e in range(len(eval_boards)):
		eval_boards[e] = mark_numbers(eval_boards[e], b)
	mark_for_delete = []
	for e in range(len(eval_boards)):
		win = evaluate_if_winner(eval_boards[e])
		if (win):
			win_board = e
			last_number = b
			if (len(eval_boards)) == 1:
				found = True
				break
			mark_for_delete.append(eval_boards[e])
	for m in mark_for_delete:
		eval_boards.remove(m)
	if (found):
		break

score = 0
for row in range(len(eval_boards[0])):
	for item in range(len(eval_boards[0][row])):
		if eval_boards[0][row][item] != 'X':
			score += int(eval_boards[0][row][item])

score *= int(last_number)

print (score)
