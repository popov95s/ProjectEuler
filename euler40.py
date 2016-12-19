

str1= ""

for num in range(1,200000):
	str1 += str(num)
	
print int(str1[10-1])*int(str1[100-1])*int(str1[1000-1])*int(str1[10000-1])*int(str1[100000-1])*int(str1[1000000-1])