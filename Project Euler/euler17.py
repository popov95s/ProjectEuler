

list = { 1:"one", 2 : "two", 3: "three", 4:"four", 5:"five", 6:"six", 7: "seven", 8: "eight", 9:"nine", 10:"ten" , 11:"eleven", 12:"twelve", 13: "thirteen",
		14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60 :"sixty",
		70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred", 1000:"onethousand" }
		
sum =0 
for x in range(1,100):
	if x in list:
		sum += len(list[x])
		print list[x]
	else : 
		sum += len(list[x%10])
		sum += len(list[x - x%10])
		print list[x-x%10] + '\t' + list[x%10]

print sum
sum *=10 
print sum
for x in range (100,1000):
	#print list[x/100] + list[100] + 'and' 
	if x%100 != 0 :
		sum += len(list[x/100]) +3 + len(list[100])
	else:
		sum+= len(list[x/100]) + len(list[100])
sum+=len(list[1000])
print sum