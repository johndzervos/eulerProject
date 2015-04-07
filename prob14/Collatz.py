maxsteps = 0
maxnum = 0
for num1 in range (1,1000000):
	#num = 13
	num=num1
	print num
	steps = 1
	while num != 1:
		steps=steps+1
		if num%2==0:
			num=num/2
			#print num
		else:
			num=num*3+1
			#print num
	#print steps
	#print num
	if steps > maxsteps:
		maxsteps = steps
		maxnum=num1


print "max: " + str(maxnum) + " " + str(maxsteps)