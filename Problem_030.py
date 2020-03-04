# Problem_030.py - Digit fifth powers

import math

finals = []

for i in range(1000000):

    the_sum = []
    for num in str(i):
        exponent = int(num)**5
        # print(exponent)
        the_sum.append(exponent)

    sum_of_sum = sum(the_sum)
    # print(sum_of_sum)

    if str(sum_of_sum) == str(i):
        # print('Sum: ' + str(sum_of_sum))
        finals.append(sum_of_sum)


print(finals)
sum_finals = sum(finals) - 1
print('Total Sum: ' + str(sum_finals))


