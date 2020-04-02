# Project Euler - Problem #48 - Self Powers - SOLVED - 0.03s

import common_functions
from datetime import datetime
startTime = datetime.now()

self_power_nums = []

for i in range(1,1001):
    x = common_functions.self_power(i)
    self_power_nums.append(x)


self_power_total = sum(self_power_nums)
self_power_str = str(self_power_total)
self_power_splice = self_power_str[-10:]

print("\nSelf Power Splice:", self_power_splice)

print('\nDuration: ')
print(datetime.now() - startTime)
