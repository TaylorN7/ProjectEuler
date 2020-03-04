# Problem_010.py - Summation of Primes

import math

num = int(input('what number should I go to?\n'))
primes = []

for num in range(1, 2000000, 2):
	if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
		print(num)
		primes.append(num)
		
sum_of = sum(primes)

print(sum_of + 2)


	

	

	
