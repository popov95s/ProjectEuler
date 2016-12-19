

sum=0
for num in range(2,99999999):
	temp = num
	tempSum=0
	while temp>=1 : 
		tempSum += ((temp%10)**5)
		temp/=10
	if tempSum==num:
		sum+=num
		
print sum