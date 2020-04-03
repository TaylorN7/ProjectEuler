# Project Euler - Problem #47 - Distinct Prime Factors - SOLVED - 2.8s

import common_functions, math
from datetime import datetime
startTime = datetime.now()

distinct_vals = []
primes = common_functions.get_primes(1,1001)
primes.remove(1), primes.append(2)


def distinct_prime_factors(s,e):
    for i in range(s,e):
        prime_factors = []
        for prime in primes:
            if prime > i / 2:
                pass
            elif i % prime == 0:
                prime_factors.append(prime)

            for y in range(2,10):
                # TODO: Fails here for some reason if I take Try/Except out
                try:
                    if i % (prime ** y) == 0:
                        prime_factors.append(prime**y), prime_factors.remove(prime)
                except:
                    pass
                    
        prime_factors = set(prime_factors)

        if len(prime_factors) == 4:
            print("I:",i,prime_factors)

            result = 1
            for x in prime_factors:
                result = result * x

            if result == i:
                distinct_vals.append(i)


for i in range (134000, 135000):
    distinct_prime_factors(i, i+4)

distinct_vals = list(dict.fromkeys(distinct_vals).keys())

i = 3
while i < len(distinct_vals):
    if distinct_vals[i] - distinct_vals[i-3] == 3:
        print(distinct_vals[i-3:i+1])
    i += 1


print('\nDuration: ')
print(datetime.now() - startTime)