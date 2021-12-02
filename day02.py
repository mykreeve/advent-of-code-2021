from datetime import datetime

filename="input/day02input.txt"
file=open(filename,"r")
file=file.readlines()

commands = []
for f in file:
	command = f.replace('\n', '').split(' ')
	command[1] = int(command[1])
	commands.append(command)

now = datetime.now()
pos = (0,0)
for c in commands:
	if c[0] == 'forward':
		pos = (pos[0]+c[1], pos[1])
	if c[0] == 'down':
		pos = (pos[0], pos[1]+c[1])
	if c[0] == 'up':
		pos = (pos[0], pos[1]-c[1])

done = datetime.now()
print ("Answer to part 1:", pos[0]*pos[1])
print ("Time taken:", done - now)


now = datetime.now()
pos = (0,0)
aim = 0
for c in commands:
	if c[0] == 'forward':
		pos = (pos[0]+c[1], pos[1]+(aim * c[1]))
	if c[0] == 'down':
		aim += c[1]
	if c[0] == 'up':
		aim -= c[1]

done = datetime.now()
print ("Answer to part 2:", pos[0]*pos[1])
print ("Time taken:", done - now)