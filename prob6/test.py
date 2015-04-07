#prob 6, euler project
print 'start'
tot = 101
totlist=[]
totlist2=[]

for i in range(1,tot):  
    print i
    totlist.append(i)
    totlist2.append(pow(i,2))

print totlist
print totlist2

sum1 = sum(totlist)
sum2 = sum(totlist2)

print sum1
print sum2

print pow(sum1,2)-sum2
