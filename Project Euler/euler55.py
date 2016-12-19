
def isPalindromic(n):
	for num in range(0,int(len(str(n))/2)):
		if str(n)[num]!=str(n)[len(str(n))-num-1]:
			return False
			
	return True

def produceReverse(n):
	temp=""
	while n>=1:
		temp+=(str(n%10))
		n/=10
	return int(temp)
count=0

for num in range (10,10000):
	iterations=0
	temp=produceReverse(num) +num
	while isPalindromic(temp)==False:
		iterations+=1
		if iterations== 50:
			print num, produceReverse(temp)+temp, iterations
			count+=1
			break
		temp=produceReverse(temp) + temp
		
		
print count