import math

num = math.factorial(100) 
print num

nums = str(num)
max = len(nums)

print nums[0]

sum = 0
for i in range(max):
	print nums[i]
	sum = sum+int(nums[i])

print sum