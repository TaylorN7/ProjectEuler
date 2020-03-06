# Project Euler Problem #37 - Truncatable Primes - SOLVED

import common_functions
from datetime import datetime
startTime = datetime.now()

truncatable_primes = []
not_truncatable_primes = []

def truncate_number(number):
	if len(str(number)) >= 2:
		right_num = number
		len_rnum = len(str(right_num)) - 1
		left_num = number
		len_lnum = len(str(left_num))
		primes_list = []

		while len_rnum > 0:
			
			right_num = str(right_num)[0:len_rnum]
			right_num = int(right_num)
			rnum_prime = common_functions.is_prime(right_num)

			if rnum_prime == True:
				#print("R:",str(right_num)[0:len_rnum], "is Prime")
				primes_list.append(right_num)
			#else:
				#print("R:",str(right_num)[0:len_rnum], "is NOT Prime")

			len_rnum -= 1
			
		for y in range(1,len_lnum):
			left_num = int(left_num)
			new_l_num = str(left_num)[y:len_lnum]
			new_l_num = int(new_l_num)
			lnum_prime = common_functions.is_prime(new_l_num)

			if lnum_prime == True:
				#print("L:", str(left_num)[y:len_lnum], "is Prime")
				primes_list.append(new_l_num)
			#else:
				#print("L:", str(left_num)[y:len_lnum], "is NOT Prime")

		if len(str(number)) == 2:
			if len(primes_list) == 2:
				#print(primes_list)
				truncatable_primes.append(number)
		elif len(str(number)) == 3:
			if len(primes_list) == 4:
				#print(primes_list)
				truncatable_primes.append(number)
		elif len(str(number)) == 4:
			if len(primes_list) == 6:
				#print(primes_list)
				truncatable_primes.append(number)
		elif len(str(number)) == 6:
			if len(primes_list) == 10:
				#print(primes_list)
				truncatable_primes.append(number)		

	#else:
		#print("Prime lengh == 1")


for i in range (22, 739398):
	prime_number = common_functions.is_prime(i)

	if prime_number == True:
		#print(i)
		truncate_number(i)
		#print()
	
print(truncatable_primes)

truncatable_sum = sum(truncatable_primes)
print('# of Values:',len(truncatable_primes))
print("Total Sum:",truncatable_sum)
print()
print('Duration: ')
print(datetime.now() - startTime)