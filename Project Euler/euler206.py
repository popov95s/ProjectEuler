
import math
tempNum = "1_2_3_4_5_6_7_8_9_0"
permList=[]

for num in range(3162277660 + 10000000, (3162277660 + 100000000)):
	if str(num)[0]== '1' and str(num)[2]== '2' and str(num)[4]== '3' and str(num)[6]== '4' and str(num)[8]== '5' and str(num)[10]== '6' and str(num)[12]== '7' and str(num)[14]== '8' and str(num)[16]== '9' and str(num)[18]== '10':
		print num 
		break