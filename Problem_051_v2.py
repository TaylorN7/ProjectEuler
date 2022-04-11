# Project Euler - Problem #51 Prime Digit Replacements

import common_functions
from datetime import datetime
startTime = datetime.now()

def get_primes(c,n):
    import math

    #c = int(input('What number should I start with?\n')) 
    #n = int(input('What number should I go to?\n')) 
    prime_list = []

    # Added this IF at Problem #50 - Remove if necessary for problems before that
    if 2 >= c and 2 <= n:
        prime_list.append(2)

    for num in range(c, n, 2):
        if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
            
            #print('Number: ' + str(num))
            prime_list.append(num)

    return prime_list

get_primes(1001,10001)

print('\nDuration: ')
print(datetime.now() - startTime)

