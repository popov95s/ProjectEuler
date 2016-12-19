import itertools

def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)

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
	

for num in range (0,7):
	lst= []
	lst.append(num)
	lst.append(num+1)
	lst.append(num+2)
	lst.append(num+3)
	
	perms = itertools.permutations(lst)
	
	
	