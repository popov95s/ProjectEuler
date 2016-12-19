

def sameDigits(x, timesx):
	if len(str(x)) == len(str(timesx)):
		digitList=[]
		for digit in str(x):
			digitList.append(digit)
			
		for digit in str(timesx):
			if digit not in digitList:	
				return False
		return True
	else :
		return False
		
		

for num in range (100, 1000000):
	if sameDigits(num, 2*num)==True and sameDigits(num, 3*num)==True and sameDigits(num, 4*num)==True and sameDigits(num, 5*num)==True and sameDigits(num, 6*num)==True :
		print num