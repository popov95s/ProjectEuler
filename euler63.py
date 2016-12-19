

import math
def isRoot(n, power):
	x = (n**(1.0/power))
	x = int(round(x)) 
	if x**power == n :
		return True
	return False
count =0
for num in range (500000000,600000000):
	if isRoot(num,len(str(num))):
		count+=1
		
print count