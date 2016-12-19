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
		
def getSum(numbers):
	sum=0
	for number in numbers:
		sum+= number
	return sum
abundantNums=[]
for num in range (0,28125):
	if num < (getSum(divisorGenerator(num))-num):
		abundantNums.append(num)
sums = set()	
for num in abundantNums:
	for num2 in abundantNums:
		sums.add(num+num2)
sum=0
for num in range(0,28124):
	if num not in sums:
		sum+=num
print sum