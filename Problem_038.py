# Project Euler Problem #38 - Pandigital Multiples - SOLVED

import common_functions
from datetime import datetime
startTime = datetime.now()

pandigital_nums = []
concate_nums = []

for i in range (1,9999):
    pandigital_tries = []

    for x in range (1,10):
        y = i * x
        y_len = len(str(y))

        for c in str(y):
            if len(pandigital_tries) != 9:
                if y in pandigital_tries:
                    break
                else:
                    pandigital_tries.append(c)

        if len(pandigital_tries) == 9:
            break

    if len(pandigital_tries) == len(set(pandigital_tries)):
        if "0" not in pandigital_tries:
            concate_num = ''.join(pandigital_tries)
            concate_nums.append(concate_num)


print(max(concate_nums))
print()
print('Duration: ')
print(datetime.now() - startTime)