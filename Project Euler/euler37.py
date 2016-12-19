def isprime(n):
	"""Returns True if n is prime."""
	if n== 1 :
		return False
	if n == 2:
		return True
	if n == 3:
		return True
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False

	i = 5
	w = 2

	while i * i <= n:
		if n % i == 0:
			return False

		i += w
		w = 6 - w

	return True
	
listOfPrimes=[]
def truncateRight(n):
	if n>=10: 
		return n/10
	else :
		return False 
	
def truncateLeft(n):
	if len(str(n))>1:
		return int(str(n)[1:])
	else :
		return False
sum =0
for num in range (10,1000000):
	temp=num
	if(isprime(temp)):
		listOfPrimes.append(temp)
		isTruncPrime= True
		left = temp 
		right = temp
		while truncateLeft(left)!=False or truncateRight(right)!=False:
			left = truncateLeft(left)
			right = truncateRight(right)
			if left not in listOfPrimes or right not in listOfPrimes:
				if isprime(left)==False or isprime(right)==False:
					isTruncPrime= False
					#print "broken", num
					break
		if isTruncPrime==True:
			print num
			sum+=num
			
print sum