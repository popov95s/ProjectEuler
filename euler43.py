import itertools
	
perms = itertools.permutations([0,1,2,3,4,5,6,7,8,9],10)

sum=0

for item in list(perms):
	tempStr=""
	for digit in item :
		tempStr+=str(digit)
	if tempStr[0]!='0':
		if int(tempStr[1:4])%2==0 and int(tempStr[5:8])%11==0 and int(tempStr[2:5])%3==0 and int(tempStr[3:6])%5==0 and int(tempStr[4:7])%7==0 and int(tempStr[6:9])%13==0 and int(tempStr[7:10])%17==0 :
			sum+=int(tempStr)
			print tempStr
print sum