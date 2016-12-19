
fractions =[]

for numerator in range(1,1000000):
	if numerator%10000==0:
		print "1"
	for denominator in range(numerator+1, 1000000):
		fractions.append(float(numerator)/denominator)
print len(fractions)