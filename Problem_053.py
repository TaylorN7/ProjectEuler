# Project Euler - Problem #53 - Combinatoric Selections - SOLVED - 0.03s

import math
import common_functions
from datetime import datetime
startTime = datetime.now()

def combinatoric_selections(n,r):

    n_r = n - r
    n_val = math.factorial(n)
    r_val = (math.factorial(r)) * (math.factorial(n_r))

    nr_val = n_val / r_val
    return nr_val


combinations = []
for n in range(1, 101):
    for r in range(1,1000):
        if r <= n:
            nr_val = combinatoric_selections(n,r)

            if nr_val > 1000000:
                combinations.append(nr_val)



#print("VALUES:")
#print(combinations)

print("# of Values:",len(combinations))

print('\nDuration: ')
print(datetime.now() - startTime)
