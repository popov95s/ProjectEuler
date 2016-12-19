import math
divisorList=dict()
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
		
triangleNumbers=[]
sum =0
for num in range(1,100000):
	sum+=num
	triangleNumbers.append(sum)
	
for number in triangleNumbers:
	if (len(list(divisorGenerator(number)))>=500):
		print number 
		break