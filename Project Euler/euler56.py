

maxSum=0
for a in range (1,100):
	for b in range (1,100):
		sum=0
		for digit in str(a**b):
			sum+=int(digit)
		if sum> maxSum:
			maxSum=sum
			
			
print maxSum