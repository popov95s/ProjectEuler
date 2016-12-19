

waysToWrite= dict()
waysToWrite[1]=1


for num in range(2,6):
	for subtractor in range(num - 1,1):
		count=0
		if num - subtractor in waysToWrite:
			count+=waysToWrite[num-subtractor]
		else:
			count+=1
		waysToWrite[num]= count
	print num#, subtractor	
print waysToWrite