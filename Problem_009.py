# Problem_009.py - Special Pythagorean Triplet

import math

# def pathag(sidea, sideb):
		# csquare = (sidea ** 2) + (sideb ** 2)
		# c = math.sqrt(csquare)
		# return c
		
		
# a = 0
# b = 0

# answer = pathag(a, b)
# print(answer)

i = 1	
a = 2
b = (a + i)
c = 0

total = 0

while total != 1000:
	
	
	for i in range(500):
		b = (a + i)

		c_sq = ((a**2) + (b**2)) 
		c = math.sqrt(c_sq)
		
		total = a+b+c
		
		print('A: ' + str(a))
		print('B: ' + str(b))
		print('C: ' + str(c))
		print('Total: ' + str(total))
		
		if total == 1000:
			input()
			input()
			input()
		
	a += 1
	
	

	
	
