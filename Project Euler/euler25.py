d = dict()

def fibonacci(n):
	if n==1 or n==2 :
		return 1
	if n in d:
		return d[n]
	else:
		return fibonacci(n-1) + fibonacci(n-2)
		
		
i=1 
m=1


while len(str(m))<=999: 
	m=fibonacci(i)
	d[i]=m
	#print m
	#print i
	i+=1
	
print len(str(m))
print len(str(d[4782])) 
print i