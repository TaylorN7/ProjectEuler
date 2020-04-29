# Project Euler - Problem #56 - Powerful Digit Numbers - SOLVED - 0.3s

from datetime import datetime
startTime = datetime.now()


sum_of_nums = []

for a in range(1,101):
    sums = []
    for b in range(1,101):
        c = a ** b

        c_list = list(str(c))
        running_num = 0
        for num in c_list:
            running_num += int(num)
        sum_of_nums.append(running_num)

print("Maximum Digital Sum:")
print(max(sum_of_nums))

print('\nDuration: ')
print(datetime.now() - startTime)