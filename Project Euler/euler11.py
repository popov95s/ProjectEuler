

list = []
with open("euler11.txt") as file :
	for num in file:
		templist=[]
		for number in num.split():
			templist.append(int(number))
			#print number
		list.append(templist)

max = 0 
for x in range(3,17): 
	for y in range (3,17):
		#horizontal right
		if list[x][y]* list[x+1][y]*list[x+2][y]*list[x+3][y] > max :
			max=list[x][y]* list[x+1][y]*list[x+2][y]*list[x+3][y]
		#diagonal right down
		if list[x][y]* list[x+1][y+1]*list[x+2][y+2]*list[x+3][y+3] > max:
			max=list[x][y]* list[x+1][y+1]*list[x+2][y+2]*list[x+3][y+3]
		#veritcal down
		if list[x][y]* list[x][y+1]*list[x][y+2]*list[x][y+3] > max:	
			max =list[x][y]* list[x][y+1]*list[x][y+2]*list[x][y+3]
		#horizontal left
		if list[x][y]* list[x-1][y]*list[x-2][y]*list[x-3][y] > max :
			max=list[x][y]* list[x-1][y]*list[x-2][y]*list[x-3][y]
		#diagonal left up
		if list[x][y]* list[x-1][y-1]*list[x-2][y-2]*list[x-3][y-3] > max:
			max=list[x][y]* list[x-1][y-1]*list[x-2][y-2]*list[x-3][y-3]
		#diagonal right up
		if list[x][y]* list[x+1][y-1]*list[x+2][y-2]*list[x+3][y-3] > max:
			max=list[x][y]* list[x+1][y-1]*list[x+2][y-2]*list[x+3][y-3]
		#diagonal left down
		if list[x][y]* list[x-1][y+1]*list[x-2][y+2]*list[x-3][y+3] > max:
			max=list[x][y]* list[x-1][y+1]*list[x-2][y+2]*list[x-3][y+3]
		#vertical up
		if list[x][y]* list[x][y-1]*list[x][y-2]*list[x][y-3] > max:	
			max =list[x][y]* list[x][y-1]*list[x][y-2]*list[x][y-3]
			
print max 