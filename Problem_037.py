#
#

import common_functions
from datetime import datetime
startTime = datetime.now()

prime_list = common_functions.get_primes()
print(prime_list)

truncated_primes_list = []

for prime in prime_list:
	
	str_prime = str(prime)
	prime_len = len(str_prime)
	print(prime)
	#print()
	
	i = 1
	while i < prime_len:
		print('I: ' + str(i))
		is_val_prime = str_prime[i:]
		is_val_prime = int(is_val_prime)
		print('Truncated Prime: ' + str(is_val_prime))
		is_it_true = common_functions.is_prime(is_val_prime)
			
		if is_it_true is True:	
			print('ITS TRUE!')
	
		i += 1
		print()

	#input()	
	
	i = prime_len - 1	
	while i > 0:
		print('I: ' + str(i))
		is_val_prime = str_prime[:i]
		is_val_prime = int(is_val_prime)
		print('Truncated Prime: ' + str(is_val_prime))
		is_it_true2 = common_functions.is_prime(is_val_prime)
			
		if is_it_true2 is True:	
			print('ITS TRUE!')
	
		i -= 1
		print()
		
		
	if is_it_true is True and is_it_true2 is True:
		print('THEY ARE BOTH TRUE!')
		
		truncated_primes_list.append(prime)
		
		
		
print(truncated_primes_list)
truncated_sum = sum(truncated_primes_list)
print('SUM: ' + str(truncated_sum))		
		
print('Duration: ')
print(datetime.now() - startTime)