# Answer: 40730 - Only 2 numbers do this (145, 40585)
# Time: 2.99 sec

import math
from datetime import datetime
startTime = datetime.now()

matches = []

def digit_factorial(digit):
	#print('Digit: ' + str(digit))
	fact = 0
	
	for char in digit:
		
		#print(char)
		fact += math.factorial(int(char))
		#print(math.factorial(int(char)))
	
	#print('Total: ' + str(fact))
		
	
	if int(fact) == int(digit):
		#print('HELLLLO')
		
		matches.append(digit)
	

for i in range(3,1000000):	
	digit_factorial(str(i))
	

	
#print(matches)
matches = list(map(int, matches))
print(matches)
matches_sum = sum(matches)

print('Sum of Matches: ' + str(matches_sum))

print('Duration: ')
print(datetime.now() - startTime)
