import math

def isPower(n, base): 

    if n == base:
        return True

    if base == 1:
        return False

    temp = base

    while (temp <= n):
        if temp == n:
            return True
        temp *= base

    return False

def sumOfDigits(n):
	sum=0
	while n>=1:
		sum+=n%10
		n/=10
	return sum

	
#math.log(10,sumOfDigits(10))
	
for num in range(10**8,2*10**8):
	#	print num
	sumOfDigs = sumOfDigits(num)
	if sumOfDigs!= 1 and math.log(num,sumOfDigs).is_integer():
		print num, sumOfDigs
		
	#elif sumOfDigs==1:
	#	print num, sumOfDigs