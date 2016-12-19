

def colatz(n):
	if n%2==0:
		return n/2
	else :
		return 3*n+1
max=0
maxNum=0
chainList=dict()
for num in range(2,1000000):
	chainCount=0
	temp=colatz(num)
	while temp!=1:
		#print temp
		if str(temp) in chainList:
			chainCount+=chainList[str(temp)]
			break
		elif colatz(temp)==1: 
			chainCount+=1
			chainList[str(temp)]=chainCount
			temp=colatz(temp)
		else: 
			chainCount+=1
			temp=colatz(temp)
	if chainCount>max:
		max= chainCount
		maxNum=num
		
print maxNum,max