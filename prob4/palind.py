#3 digit numbers
for i in range(800,1000):
	for j in range(800, 1000):
		prod = i*j

		sp = str(prod)
		#print sp
		if (sp[0]==sp[5]) & (sp[1]==sp[4]) & (sp[2]==sp[3]): 
			print i
			print j
 
