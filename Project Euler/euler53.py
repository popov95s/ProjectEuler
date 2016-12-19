import math

count =0 
for n in range(1,101):
	for r in range (0, n):
		if( math.factorial(n))/(math.factorial(r)*math.factorial(n-r)) > 1000000 : 
			count=count+1
			#print str((math.factorial(n))/(math.factorial(r)*math.factorial(n-r))) + '\t' + str(n) + '\t' + str(r)
			
print count