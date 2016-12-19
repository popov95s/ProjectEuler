import math


n = math.factorial(100)
sum = 0 
while n>1 : 
	sum += n%10
	n/=10 
	
print sum