base = '123432'
tot = ''

def sumsub(a):
	#print len(a)
	sum=0
	for i in range(0,len(a)):
		sum += int(a[i])
	return sum

#construct the total number by iterating the base
for i in range(100):
	tot = tot+base

print tot

listnum = []

finish=12
for i in range(finish):
	substr = ''
	cnt=0
	while sumsub(substr)!=i:
		cnt+=1
		substr = tot[0:cnt]
		#print substr
	#raw_input()
	listnum.append(substr)
	print substr
	tot = tot[cnt:]

#first entry is ''
listnum = listnum[1:]
print listnum

final = 0
for j in listnum:
	print j
	final = final+int(j)
print final
#test = sumsub(tot)
#print test

	