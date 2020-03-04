# Problem_014.py - Longest Collatz sequence

import math

lengths = []
	
for i in range(2, 1000000):
	len_of_collatz = []
	
	
	print(i)
	len_of_collatz.append(i)

	while i != 1:
		if i % 2 == 0:
			i = (i / 2)
			len_of_collatz.append(i)
			
		elif i % 2 != 0:
			i = ((3 * i) + 1)
			len_of_collatz.append(i)
	
	
	len_of_list = len(len_of_collatz)
	
	if len_of_list == 525:
		print('Longest Collatz Number: ' + str(i))
		input()
	
	lengths.append(len_of_list)
	
	
	



print('Longest Collatz Sequence: ' + str(max(lengths)))

	




