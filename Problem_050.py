# Project Euler - Problem #50 Consecutive Prime Sum - SOLVED - 1.4s

import common_functions
from datetime import datetime
startTime = datetime.now()

def prime_range_sum(start, end):
    if start == 2:
        primes_sum = end - 0
    else:
        primes_sum = end - start
    return primes_sum


prime_list = common_functions.get_primes(3,5000)
prime_list_len = len(prime_list)

''' 
prime_sum_list = []
for prime in prime_list:
    if prime == 2:
        prime_sum = 2
        prime_sum_list.append(prime_sum)
    else:
        prime_sum += prime
        prime_sum_list.append(prime_sum)

prime_dict = {prime_list[i]:prime_sum_list[i] for i in range(0,prime_list_len)}
'''

running_dict = {}

i = 0
while i < prime_list_len:
    x = 1
    running_sum = prime_list[i]
    while x < prime_list_len:
        if x > i:
            running_sum += prime_list[x]
            running_sum_prime = common_functions.is_prime(running_sum)

            if running_sum_prime == True:
                if running_sum < 1000000:
                    difference_len = (x+1)-i
                    running_dict[difference_len] = running_sum 

        x += 1
    i += 1

print(max(running_dict.items()))


print('\nDuration: ')
print(datetime.now() - startTime)