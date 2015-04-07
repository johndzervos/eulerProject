with open('number.txt') as f:
    lines = f.readlines() 

tot=0

for line in lines:
	tot += int(line)

print tot

