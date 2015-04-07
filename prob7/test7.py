lower = 1
upper = 200000
primes = []
for num in range(lower,upper + 1):
	# prime numbers are greater than 1
   	if num > 1:
	    for i in range(2,num):
	      	if (num % i) == 0:
	           	break
	       	else:
	       		#print(num)
	       		primes.append(num)

	       		#if len(primes)%1000==0:
	       			#print len(primes)

	       		final=100
	       		if len(primes)==final:
	       			print num
	       			print ('stop')
	       			print primes
	       		break

print primes