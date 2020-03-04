# Problem_024.py - Lexicographic Permutations

from itertools import permutations
import math

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}


perms = [''.join(p) for p in permutations('ABCDEFGHIJ')]
#perms = [''.join(p) for p in permutations('ABC')]
#print(perms)			
			
			
			
millionith = perms[999999]
print(millionith)
number = ''

for letter in millionith:
	if letter in letters:
		print(letters[letter])
		number += str(letters[letter])
		
		
print('Millionith: ' + number)

