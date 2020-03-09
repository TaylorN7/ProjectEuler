# Project Euler - Problem #41 - Pandigital Prime - SOLVED - 62s

import common_functions
from datetime import datetime
startTime = datetime.now()

x = ''
pandigital_primes = []

for i in range(7000000 ,10000000):
    prime = common_functions.is_prime(i)

    if prime == True:
        x = str(i)
        chars = list(x)
        max_char = max(chars)

        if max_char == "2" and len(chars) == 2:
            if "1" in chars:
                pandigital_primes.append(i)
        elif max_char == "3" and len(chars) == 3:
            if "1" in chars and "2" in chars:
                pandigital_primes.append(i)
        elif max_char == "4" and len(chars) == 4:
            if "1" in chars and "2" in chars and "3" in chars:
                pandigital_primes.append(i)
        elif max_char == "5" and len(chars) == 5:
            if "1" in chars and "2" in chars and "3" in chars and "4" in chars:
                pandigital_primes.append(i)
        elif max_char == "6" and len(chars) == 6:
            if "1" in chars and "2" in chars and "3" in chars and "4" in chars and "5" in chars:
                pandigital_primes.append(i)
        elif max_char == "7" and len(chars) == 7:
            if "1" in chars and "2" in chars and "3" in chars and "4" in chars and "5" in chars and "6" in chars:
                pandigital_primes.append(i)
        elif max_char == "8" and len(chars) == 8:
            if "1" in chars and "2" in chars and "3" in chars and "4" in chars and "5" in chars and "6" in chars and "7" in chars:
                pandigital_primes.append(i)
        elif max_char == "9" and len(chars) == 9:
            if "1" in chars and "2" in chars and "3" in chars and "4" in chars and "5" in chars and "6" in chars and "7" in chars and "8" in chars:
                pandigital_primes.append(i)
        
print(pandigital_primes)
biggest_pandigital_prime = max(pandigital_primes)
print(biggest_pandigital_prime)
print()
print('Duration: ')
print(datetime.now() - startTime)