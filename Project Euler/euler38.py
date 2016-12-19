from collections import defaultdict

def isPandigital(n):
	list = []
	for digit in str(n) : 
		if digit in list or digit=='0': 
			return False
		else : 
			list.append(str(digit))
	
	return True
	
panDigitalList = defaultdict()
sum = 0 
for num in range (1, 9999):
	
	for num2 in range(1,9999):
		numStr= ""
		product = num*num2
		numStr+= str(num) + str(num2) + str(product)
		if len(numStr)<10:
			if isPandigital(int(numStr)) and panDigitalList[num2]!=num:
				sum+=product
				panDigitalList[num]=num2
				
print sum