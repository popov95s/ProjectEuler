import re
from decimal import * 
regex = re.compile(r'(.+ .+)( \1)+')
maxRecur=0

#
#def spaceSeparate(stringPassed):
#	stringPassed= " ".join(stringPassed[m:m+2] for m in range(0, len(stringPassed), 2)
#	return stringPassed

s= str(1.0/7)

s = " ".join(s[i:i+2] for i in range(0, len(s), 2))	

sequence = regex.search(s)
print sequence.group(1)
maxNum=0
maxSequence=0
for num in range (3,1000,2):
	
	s = str(Decimal(1.0)/Decimal(num))
	s = " ".join(s[i:i+1] for i in range(0, len(s), 2))	
	
	sequence = regex.search(s)
	if sequence!=None:
		digitSet= set()
		for digit in sequence.group(1).split(' '): 
			digitSet.add(digit)
		
		if maxRecur <len(sequence.group(1)) and len(list(digitSet))>1:
			print digitSet, num, sequence.group(3)
			print s
			maxSequence = sequence.group(1)
			maxRecur= len(sequence.group(1))
			maxNum= num
#stringPassed= " ".join(stringPassed[m:m+2] for m in range(0, len(stringPassed), 2)	
#spaceSeparate(1.0/5)
##for n in range(1,1000):
#	print n 	
#	expression = str(1.0/n)
#	expression =  spaceSeparate(expression)
#	#match = regex.search(expression).group(1)
	#if maxRecur< len(match):
	#	maxRecur = len(match)
		
print maxRecur, maxNum, maxSequence