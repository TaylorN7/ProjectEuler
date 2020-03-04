# Problem_012.py - Highly divisible triangular number

import math

x = 1
i = 2
divisors = []

while x > 0:
	divisors = []
	print('X: ' + str(x))
	
	
	for y in range(x):
		y += 1
		if x % y == 0:
			divisors.append(y)
			
			
			if len(divisors) >= 500:
				print('500+ divisors')
				print('# of Divisors: ' + str(len(divisors)))
				print(divisors)
				input()
				input()
				input()
			
	x += i
	i += 1

	
