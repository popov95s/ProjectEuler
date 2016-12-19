
list = []
for a in range(2,101):
	for b in range (2,101):
		p = a**b
		if p not in list:
			list.append(p)

print len(list)