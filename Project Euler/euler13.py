list = []
with open("euler13.txt") as file :
	for num in file:
		list.append(int(num))
sum=0		
for num in list:
	sum += num


print sum	