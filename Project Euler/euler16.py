import math
from sys import getsizeof
x = 2**1000
print getsizeof(x)
sum = 0
while(x>=1):
	sum = sum + math.floor(x%10)
	#print math.floor(x%10)
	x=x/10
print sum