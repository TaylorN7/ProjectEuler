# Problem_003.py - Largest Prime Factor - what is the largest prime factor of 600851475143

import math

primes = []
factors = []

num = int(input('what number should I go to?\n'))


for num in range(3, 600851475143, 2):
	if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
		print(num)
		primes.append(num)
		
		
for number in primes:
	if 600851475143 % number == 0:
		factors.append(number)


print(primes)		
print(factors)
		
		
largest_factor = max(factors)

print('')
print('Largest Factor of 600851475143: ' + str(largest_factor))

	
