# Answer: 55
# Time: 17 sec

import math, common_functions
from datetime import datetime
startTime = datetime.now()

#n = int(input('what number should I go to?\n'))
n = 1000000

prime_list = []
circular_primes = []

for num in range(1, n, 2):
	x = 0
	if all(num%b!=0 for b in range(2, int(math.sqrt(num))+1)):

		prime_list.append(num)
		str_prime = str(num)
		prime_len = len(str_prime)
		i = 0
		
		# Generate the circular numbers
		int_primes_list = []
		while i < prime_len:

			int_primes = int(str_prime)
			int_primes_list.append(int_primes)
			str_prime = str_prime[1:] + str_prime[0]
			i += 1
			
		#print(int_primes_list)
		
		# Determine if all circular numbers are primes
		are_all_circ_prime = all(common_functions.is_prime(pr) is True for pr in int_primes_list)
			
		if are_all_circ_prime is True:
			for prime_val in int_primes_list:
				if prime_val not in circular_primes:
					circular_primes.append(prime_val)
		

num_of_cir_primes = len(circular_primes)
print(circular_primes)
print('Number of Circular Primes:')
print(num_of_cir_primes)			
			
print('Duration: ')
print(datetime.now() - startTime)

	