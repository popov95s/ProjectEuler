def getNextChain(n):
	sum = 0
	print "nextC"
	while n>=1:
		sum+= (n%10)**2
		n/=10
		print sum
	return sum

map = dict()

count=0

for num in range (10, 11):
 
	print num
	if num in map and map[num]==89:
		count+=1
	elif num not in map: 
		temp=num +getNextChain(num)
		print "after nextC"
		while temp != 89 or temp !=1:
			if temp in map and map[temp]==89:
				count+=1
				break
			temp += getNextChain(temp)
		if temp==89:
			count+=1
			map[num]=89
		elif temp==1 :
			map[num]=1
			
print count