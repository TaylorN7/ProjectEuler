# Project Euler - Problem #43 - Sub-String Divisibility - SOLVED - 25s

from itertools import permutations
from datetime import datetime
startTime = datetime.now()

pandigital_nums = []
perms = [''.join(p) for p in permutations('1234567890')]

for perm in perms:

    nums = list(perm)
    
    if "0" in nums and "1" in nums and "2" in nums and "3" in nums and "4" in nums and "5" in nums and "6" in nums and "7" in nums and "8" in nums and "9" in nums:
        val_1 = str(perm)[1:4]
        val_1 = int(val_1)

        val_2 = str(perm)[2:5]
        val_2 = int(val_2)

        val_3 = str(perm)[3:6]
        val_3 = int(val_3)

        val_4 = str(perm)[4:7]
        val_4 = int(val_4)

        val_5 = str(perm)[5:8]
        val_5 = int(val_5)

        val_6 = str(perm)[6:9]
        val_6 = int(val_6)

        val_7 = str(perm)[7:]
        val_7 = int(val_7)

        if val_1 % 2 == 0:
            if val_2 % 3 == 0:
                if val_3 % 5 == 0:
                    if val_4 % 7 == 0:
                        if val_5 % 11 == 0:
                            if val_6 % 13 == 0:
                                if val_7 % 17 == 0:
                                    pandigital_nums.append(int(perm))

print(pandigital_nums)
print("SUM:",sum(pandigital_nums))
print('\nDuration: ')
print(datetime.now() - startTime)
