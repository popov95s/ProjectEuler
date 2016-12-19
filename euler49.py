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
for num in range (1000,9999):
	if isprime(num):
		primeList.append(num)
		
		
for num in primeList:
	tempArray=[]
	while num>=1:
		tempArray.append = (num%10)
		num/=10
	perms = itertools.permutations(tempArray)
	
	for item in list(perms):
		