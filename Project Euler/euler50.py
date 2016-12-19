def isprime(n):
    """Returns True if n is prime."""
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

	

primeList=[]
for num in range (1,1000000):
	if isprime(num):
		primeList.append(num)
maxCount=0		
maxPrime=0
print "Got Primes"
for i in range(0,len(primeList)):
	sum = primeList[i] 
	count=0
	j=i+1
	for j in range(i+1,len(primeList)):
		sum+=primeList[j]
		if sum in primeList:
			if count>maxCount:
				maxCount=count
				maxPrime = sum
		count+=1
print maxCount, maxPrime