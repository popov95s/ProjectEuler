def produceBinary(n):
	temp=""
	while n>=1:
		temp=str(n%2) +temp
		n/=2
	return temp
	

def isPalindromic(n):
	for num in range(0,int(len(str(n))/2)):
		if str(n)[num]!=str(n)[len(str(n))-num-1]:
			return False
			
	return True

print isPalindromic(produceBinary(3))

sum=0
for num in range(1,1000000):
	if isPalindromic(produceBinary(num))==True and isPalindromic(num)==True:
		sum+=num
print sum