
class Node:
    def __init__(self, val, left, right):
        self.l = left
        self.r = right
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
		


previousRow=[]
currentRow=[]
for line in reversed(open("euler67.txt").readlines()):
	line=line[0:len(line)-1]
	previousRow=[]
	previousRow=currentRow
	currentRow=[]
	for number in line.split(' '):
		currentRow.append(int(number))
	index=0
	if previousRow :
		for indx in range(0,len(currentRow)):
			if previousRow[index] > previousRow[index+1]: 
				currentRow[indx]+= previousRow[index]
			else:
				currentRow[indx]+= previousRow[index+1]
			index+=1
			
print currentRow