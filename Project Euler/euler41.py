import itertools
def isPandigital(n):
	list = []
	for digit in str(n) : 
		if digit in list or digit=='0': 
			return False
		else : 
			list.append(str(digit))
	
	return True
	
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

max = 0
perms = itertools.permutations([1,2,3,4,5,6,7],7)
#print list(perms)
for numList in list(perms):
	tempStr=""
	for digit in numList:
		tempStr+= str(digit)
	if isprime(int(tempStr)) == True:
		max = int(tempStr)
		
print max