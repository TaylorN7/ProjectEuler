# Problem_025.py - 1000-digit Fibonacci number

import math

list = []
a = 1
b = 2	

while len(str(a)) <= 3:
	
	print(a)
	a_len = len(str(a))
	
	a, b = b, a + b
	
	#print('Length: ' + str(a_len))
	list.append(a)
	
	if a_len == 3:
		
		print(len(list) + 1)
		input()

	
	#print(len(list))
	
	

