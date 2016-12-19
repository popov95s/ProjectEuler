import math
maxValue=0
maxKey=0
tupleList=dict()
for a in range(1,1000):
	for b in range (a,1000):
		c = math.sqrt(a**2+b**2)
		
		if a+b+round(c)>1000:
			break
		if c.is_integer():
			c=int(c)
			if a+b>c and a+c>b and b+c>a:
				if (int(a+b+c)) in tupleList:
					tupleList[int(a+b+c)]+=1
				else:
					tupleList[int(a+b+c)]=1
for key,value in tupleList.items():
	if value>maxValue:
		maxValue=value
		maxKey=key
		
print maxKey,maxValue