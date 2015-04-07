def valuestr(a):
	sum = 0
	print a
	#print len(a)
	for j in range(len(a)):
		#print a[j]
		val = ord(a[j])-64
		#print val
		sum = sum + val
	return sum

filename = "names.txt"
mynames = []
with open(filename) as f:
    for line in f:
        mynames.append([n for n in line.strip().split(',')])

#print len(mynames[0])

list1 = []

for i in mynames[0]:
	newstr = i.replace('"', "")
	list1.append(newstr)

list2 = sorted(list1)
wlist = []

for i in range(len(list2)):
	#print list2[i]
	w1 = valuestr(list2[i])
	print w1
	w2 = i+1
	print w2
	w3 = w1*w2
	print w3
	wlist.append(w3)

print sum(wlist)
#print wlist[937]
#print list2[937]