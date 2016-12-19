import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
		
def getSum(divisor):
	sum=0
	for number in divisor:
		sum+=number
	return sum

map = dict()	

sum=[]
for num in range(1,10000):
	sumOfDivisors=getSum(divisorGenerator(num)) - num 
#	print num,sumOfDivisors
	if str(sumOfDivisors) in map and map[str(sumOfDivisors)] == num:
		#print num, sumOfDivisors
		sum.append(sumOfDivisors)
		sum.append(num)
	else: 
		map[str(num)]=sumOfDivisors
	
#print map
sumOf=0
for number in set(sum):
	sumOf+=number
print sumOf