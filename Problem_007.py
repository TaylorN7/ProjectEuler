# Problem_007.py - 10001st Prime

import math


# Way1
#n = int(input('what number should I go to?\n'))
n = int(input('what number should I go to?\n'))

list = []

for num in range(1, n, 2):
	if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
		print(num)
		list.append(num)
		
		if len(list) == 10001:
			print('REAL')
			print(len(list))
			print(list[10000])
			break
		
		



	
