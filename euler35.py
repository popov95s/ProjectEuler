
import itertools
import time
digitCirculars=dict()
listOfPrimes=dict()	

def getCircularNums(n):
	listOfDigits=[]
	circularNums=[]
	for digit in str(n):
		listOfDigits.append(int(digit))
	listOfDigits.sort()
	if int(''.join(map(str,listOfDigits))) not in digitCirculars:
		permutes = itertools.permutations(listOfDigits)
		for item in permutes : 
			if item[0]!=0:
				circularNums.append(int(''.join(map(str,list(item)))))
		
		digitCirculars[int(''.join(map(str,listOfDigits)))]=list(set(circularNums))		
		return list(set(circularNums))
	else:
		return digitCirculars[int(''.join(map(str,listOfDigits)))]
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
	for num in listOfPrimes:
		if n%num==0:
			return False
	while i * i <= n:
		if n % i == 0:
			return False

		i += w
		w = 6 - w

	return True

totalCount=0

start= time.clock()
for num in range(2,	100000):
	count=0
	circulars=getCircularNums(num)
	for item in circulars:
		if item in listOfPrimes:
			count+=1
		elif isprime(item)==True:
			listOfPrimes[item]=item
			count+=1
	if len(circulars)==count:
		totalCount+=1
end= time.clock()
time= (end-start)
print time
print totalCount
print getCircularNums(221)