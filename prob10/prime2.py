primes = []

for i in range(2,2000000):
 	#print i
 	if i%10000==0:
 		print i
 	flag=1

 	for j in range(2,i-1):
 		if i%j==0:
 			#print "No"
 			flag=0
 			break
 	if flag==1:
 		#print i
 		primes.append(i)

 		if i%100==0:
 			print i
print sum(primes) 
