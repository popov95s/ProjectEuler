
list = []
with open("euler8.txt") as file :
	for num in file:
		for number in num.strip('\n'):
			list.append(int(number))
			#print number
max = 0 		
index=0
for x in list:
	temp = 1
	if 0 not in list[index:index+13]:
		for y in range (0,13):
			temp *= list[index+y] 
		if temp>max:
			max=temp
	index+=1
print max