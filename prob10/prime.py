#sum all the primes beloow 2,000,000

upper = 2000000

primes=[]			
			
for i in range(2,upper):
 	#print i
 	flag=1
 	for j in range(2,i-1):
 		if i%j==0:
 			#print "No"
 			flag=0
 			break
 	if flag==1:
 		print i
 		primes.append(i)

final = sum(primes)
print final

 			