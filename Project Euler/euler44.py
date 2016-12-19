
pentagonalList=dict()
for num in range (1,10000):
	pentagonalList[(num*(3*num-1))/2] = num
	
for j in pentagonalList:
	for k in pentagonalList:
		if k+j in pentagonalList and k - j in pentagonalList:
			print k-j