# Project Euler - Problem #46 - Goldbach's Other Conjecture - SOLVED - 59s

import common_functions
from datetime import datetime
startTime = datetime.now()

def twice_a_square(n):
    z = 2 * (n ** 2)
    return z

def composite_numbers(n):
    if n in primes:
        pass
    else:
        composite_number_list.append(n)

non_goldbach_composites = []
composite_number_list = []   
goldbach_composites = []
twice_squares = []

primes = common_functions.get_primes(3,6000)

for i in range(1, 6000):
    y = twice_a_square(i)
    twice_squares.append(y)

for i in range(1, 6000, 2):
    composite_numbers(i)

for num in composite_number_list:
    #print(num)
    for prime in primes:
        if prime < num:
            x = num - prime

            if x in twice_squares:
                if num not in goldbach_composites:
                    goldbach_composites.append(num)

for num in composite_number_list:
    if num not in goldbach_composites:
        non_goldbach_composites.append(num)

if 1 in non_goldbach_composites:
    non_goldbach_composites.remove(1)

print("NON-GOLDBACK COMPOSITES")
print(non_goldbach_composites)


print('\nDuration: ')
print(datetime.now() - startTime)







