# Problem_004.py - Largest Palindrome Product - Largest palindrome made from the product of 2 3-digit numbers

import math

palindromes = []

for i in range(100, 999):
	for d in range(100, 999):
		value = str(i*d)
		
		if value == value[::-1]:
			print(value)
			
			palindromes.append(value)
			
print(sorted(palindromes))		
print('Highest Palindrome: ' + max(palindromes))