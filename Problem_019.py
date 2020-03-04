# Problem_019.py - Counting Sundays

import math
	
day = ''
x = 0	
mondays = []

first_of_month_leap	= 	[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
first_of_month= 		[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

days = ['Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday',
	'Sunday',]

	
for year in range(1900,2001):
	print(year)

	
	if year % 4 == 0 and year != 1900:
		total_days = 366
		print('LEAP YEAR')
		
		for i in range(total_days):

			if x == 7:
				x = 0
			day = days[x]
			
			if day == 'Sunday' and i in first_of_month_leap:
				mondays.append(1)			
			x += 1

		
	else:
		total_days = 365
		
		for i in range(total_days):
			#print(i)
			if x == 7:
				x = 0
			day = days[x]
			#print(day)
			if day == 'Sunday' and i in first_of_month:
				#print('MONDAY')
				mondays.append(1)
			x += 1
			
	#input()

num_of_mons = sum(mondays)
print(num_of_mons - 2)


