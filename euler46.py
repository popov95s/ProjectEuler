
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
for num in range (1,10000):
	if isprime(num)==True:
		primeList.append(num)
	

for num in range (1,100000):
	if num not in primeList and num%2!=0:
		
		flag = False	
		for prime in primeList: 
			if num == 
		