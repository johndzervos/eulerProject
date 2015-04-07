sum = 0
index=0

lines = tuple(open('tree.txt', 'r'))
#lines = tuple(open('triangle.txt', 'r'))
#print lines

#root
a = lines[0]
b = a.split()
sum = int(b[0])
print sum

max = len(lines)

for i in range(max-1):
	nextLine = lines[i+1].split()
	#print nextLine
	left = int(nextLine[index])
	right = int(nextLine[index+1])

	if left>right:
		sum = sum+left
		print left
		print sum
	else:
		sum = sum+right
		index = index+1
		print right
		print sum

print sum
#for line in f:
	#print line
	#data = line.split()
	#print data

	
	#print int(data[0])*2
	#print data.index(max(data))
    