


names= []
with open("names.txt") as file : 
	for name in file.readlines():
		name= name[1:len(name)-1]
		names.append(name.strip("'"))
	
print len(names)
names.sort()
sum = 0
index = 1
for name in names:
	score=0
	for character in name:
		score+=ord(character) - 64
	sum += (score*index)
	index+=1
print sum