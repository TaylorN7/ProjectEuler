# Project Euler - Problem #46 - Goldbach's Other Conjecture

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

def goldbach_composite(n):
    for prime in primes:
        for square in twice_squares:
            if prime + square == n and n not in goldbach_composites:
                #print("\ngoldbach COMPOSITE:",n)
                #print("NUM:",n)
                #print("PRIME:",prime)
                #print("SQUARE:",square)
                goldbach_composites.append(n)


non_goldbach_composites = []
composite_number_list = []   
goldbach_composites = []
twice_squares = []

primes = common_functions.get_primes(3,10000)
print(primes)

for i in range(1, 1000):
    y = twice_a_square(i)
    twice_squares.append(i)

for i in range(1, 10000, 2):
    composite_numbers(i)

#for num in composite_number_list:
#    goldbach_composite(num)

# Testing
non_goldbach_composites.append(44)

final_list = [x for x in non_goldbach_composites if x not in goldbach_composites]

print("\nGOLDBACH COMPOSITES:")
print(goldbach_composites)

print("\nNON-GOLDBACH COMPOSITES:")
#print(non_goldbach_composites)
print(final_list)



# new section
for composite_number in composite_number_list:
    if composite_number in primes:
        pass
    else:
        for prime in primes:
            if prime > composite_number:
                pass
            else:
                for square in twice_squares:
                    if square > composite_number:
                        pass
                    elif prime + square = composite_number:
                        goldbach_composites.append(composite_number)














print('\nDuration: ')
print(datetime.now() - startTime)







