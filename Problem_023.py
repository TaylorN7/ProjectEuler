# Problem_023.py - Non-abundant Sums

import math

abundant_numbers = []

goto = 28124

for i in range(goto):
	print(i)
	divisors = []
	
	for x in range(1, i):
		if i % x == 0:
			divisors.append(x)	
			
			
			
	#print(divisors)
	divisors_sum = sum(divisors)
	#print('Divisors Sum: ' + str(divisors_sum))
	
	if divisors_sum > i:
		abundant_numbers.append(i)
				
#print(abundant_numbers)


abundant_num_sums = []
print('HAHAHAHA')


for y in abundant_numbers:
	for z in abundant_numbers:
		
		print('Y+Z: ' + str(y+z))
		yz_sum = y+z
		
		if yz_sum not in abundant_num_sums:
			abundant_num_sums.append(yz_sum)
			
#print(abundant_num_sums)
print('HAHAHAHA')

total = 0
for numbers in range(goto):
	if numbers not in abundant_num_sums:
		print('Numbers: ' + str(numbers))
		total += numbers
	
print('Total: ' + str(total))
		
		
			
			
			
			
			


