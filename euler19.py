
daysInMonth = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

dayOfWeek= 1
sundaysOnFirst= 0
for year in range (1900,1901):
	for month in range (1,13):
		if dayOfWeek%7==0:
			sundaysOnFirst+=1
		if year%4==0 and month==2:
			dayOfWeek+= daysInMonth[month] +1
		else:
			dayOfWeek+= daysInMonth[month]
		
print sundaysOnFirst, dayOfWeek