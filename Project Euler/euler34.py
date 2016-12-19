
import math

sum = 0
for num in range (1,100000000):
	score = 0
	for digit in str(num):
		score += math.factorial(int(digit))
		
	if score==num:
		sum+=num
		
print sum