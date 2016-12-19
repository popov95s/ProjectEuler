


xcoord = []
i=0
for x in range(0,20):
	ycoord = []
	for y in range (0,20):
		ycoord.append(i)
		i+=1
	xcoord.append(ycoord)
sum = 0 
def iterateMap(x,y, sum):
	if xcoord[x][y]== 399:
		sum+=1
		print "SUCCESS"
		return
	else:
	
		xcoord[x][y] = -1
		if x<19 and xcoord[x+1][y]!=-1:
			iterateMap(x+1,y,sum)
		if y<19 and xcoord[x][y+1]!=-1:
			iterateMap(x,y+1,sum)
iterateMap(0,0,sum)
print sum