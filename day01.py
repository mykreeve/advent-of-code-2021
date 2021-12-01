from datetime import datetime

filename="input/day01input.txt"
file=open(filename,"r")
file=file.readlines()

numbers = []
for f in file:
	numbers.append(int(f.replace('\n','')))
compare = None
inccount = 0

now = datetime.now()
for a in numbers:
	if compare:
		if a > compare:
			inccount += 1
	compare = a

done = datetime.now()
print ("Answer to part 1:", inccount)
print ("Time taken:", done - now)

now = datetime.now()
inccount = 0
for a in range(1, len(numbers)-2):
	if (numbers[a-1] + numbers[a] + numbers[a+1]) < (numbers[a] + numbers[a+1] + numbers[a+2]):
		inccount += 1

done = datetime.now()
print ("Answer to part 2:", inccount)
print ("Time taken:", done - now)
