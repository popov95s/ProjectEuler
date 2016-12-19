pentagonalList=dict()
triangleList=[]
hexagonalList=[]


for num in range (144,100000):
	hexagonalList.append(num*(2*num-1))
for num in range (166,1000000):
	pentagonalList[(num*(3*num-1))/2] = num
	
for num in hexagonalList:
	if num in pentagonalList:
		print num
		break