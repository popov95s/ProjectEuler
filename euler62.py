

permutations= dict()
perms= dict()
for num in range(1,10000):
	tempArray=[]
	for digit in str(num**3):
		tempArray.append(int(digit))
	tempArray.sort()
	tempStr=""
	for digit in tempArray:
		tempStr+=str(digit)
	if tempStr in permutations:
		permutations[tempStr]+=1
		perms[tempStr].append(num)
		if permutations[tempStr]==5:
			print tempStr
			print num
			print perms[tempStr]
			break
	else:
		permutations[tempStr]=1
		perms[tempStr]=[]
		perms[tempStr].append(num)