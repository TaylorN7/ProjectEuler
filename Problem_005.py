# Problem_005.py - Smallest Multiple - Smallest number that is evenly divisible by all of the numbers from 1 to 20


import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

x = math.factorial(20)
print(x)

i = 20

while i > 1:
	
	if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
		print(i)

	i += 1
	
	