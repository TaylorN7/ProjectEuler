# Problem_021.py - Amicable numbers

import math

i_divisors_sum = 0
y_divisors_sum = 0

amicable = []

for i in range(10000):
	i_divisors = []
	y_divisors = []
	
	print('I: ' + str(i))
	for x in range(1,i):
		if i % x == 0:
			#print(x)
			i_divisors.append(x)
		
		i_divisors_sum = sum(i_divisors)
		
		
		
		
	for y in range(1,i_divisors_sum):
		
		if i_divisors_sum % y == 0:
			y_divisors.append(y)
			#print(y_divisors)
			#print('Y: ' + str(y))
	
			y_divisors_sum = sum(y_divisors)
		
	print('I-Divisor Sum: ' + str(i_divisors_sum))
	print('Y-Divisor Sum: ' + str(y_divisors_sum))
	
	if y_divisors_sum == i:
		amicable.append(i_divisors_sum)
		#amicable.append(y_divisors_sum)
		#input()
		
	
	
	#print(amicable)
	#input()
			
			
print(amicable)
amicanle_sum = sum(amicable)
print(amicanle_sum - (6+28+496+8128))

