def isPandigital(n):
	list = []
	for digit in n : 
		if digit in list or digit=='0': 
			return False
		else : 
			list.append(digit)
	if len(list)==9:
		return True
	else:
		return False
		
sum=0
for num in range(1,100):
	r=1
	if num > 9:	
		r = 123
	else :
		r=1234
	for second in range(r,100000/num+1):
		tempStr= ""
		tempStr+= str(num) + str(second)+  str(num*second)
		if  len(tempStr)<10: 
			if isPandigital(tempStr):
				sum+= num*second
				print num, second, num*second
				
			
print sum

#this takes about 10 seconds in trinket
def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if is_pandigital(str(i) + str(j) + str(i*j)): p.add(i*j)

print "Sum of products =", p