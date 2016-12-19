

def trimLeft(n):
	return int(n)%10
def trimRight(n):
	return int(n)/10
	
for numerator in range (10,100):
	for denominator in range (numerator+1,100):
		if numerator%10 != 0 and denominator%10!=0 and (float(numerator)/denominator == float(trimRight(numerator))/trimLeft(denominator)):
			print numerator, denominator