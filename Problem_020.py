# Problem_020.py - Factorial digit sum

import math

num = math.factorial(100)
print(num)
num = str(num)

num_list = list(num)
num_list = map(int, num_list)

num_sum = sum(num_list)
print(num_sum)



