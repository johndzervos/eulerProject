import itertools
import numpy as np
import collections


f = open("matrix.txt", 'r')

mm=[]

for line in f:
	#print line 
	a = line.split(',')
	#print a
	mm.append(a)

#print mm
#print mm[0][0]
print len(mm)


mm2=[
	[131, 673, 234, 103, 18],
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331]
]

#print len(mm2)
#print mm2[0][0]

mm_final = mm2

#all possible actions to go from top left to bottom right: permutations
'''
actions = []
for i in range(len(mm_final)-1):
	actions.append('right')
	actions.append('down')

print actions
'''
print '--------'

act=['right', 'down']

#scenarios = list(itertools.permutations(actions, (len(mm_final)-1)*2))
scenarios = list(itertools.product(act, repeat=(len(mm_final)-1)*2))

scenarios2=[]
for i in scenarios:
	#print i
	counter=collections.Counter(i)
	#print counter
	if counter.values()==[len(mm_final)-1,len(mm_final)-1]:
		print counter
		scenarios2.append(i)

print len(scenarios)
print 'scenarios: ' 
#print scenarios
#scenarios2 = sorted(set(scenarios))

#EVALUATE SCENARIOS
#init with the top left
minsum = 0

print len(scenarios2)
for i in scenarios2:
	x=0
	y=0
	sum1 = mm_final[0][0]
	print i
	for j in range(len(i)):
		#print i[j]
		if i[j] is 'right':
			x+=1
		elif i[j] is 'down':
			y+=1
		sum1 += mm_final[x][y]
	if i==scenarios2[0]:
		minsum = sum1
	#keep the minimum sum
	if sum1 < minsum:
		minsum = sum1
print minsum

