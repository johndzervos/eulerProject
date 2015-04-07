start = 2
end = 100

list1 = []
for a in range(start, end+1):
	for b in range(start, end+1):
		tmp = pow(a,b)
		list1.append(tmp)

print list1
list2 = list(set(list1))
list3 = sorted(list2)
print list3
print len(list3)