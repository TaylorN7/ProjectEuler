# Project Euler - Problem #52 - Permuted Multiples - SOLVED - .47s

import common_functions
from datetime import datetime
startTime = datetime.now()

for i in range (100000, 1000000):
    i_2 = 2*i
    i_3 = 3*i
    i_4 = 4*i
    i_5 = 5*i
    i_6 = 6*i

    str_i = str(i)
    str_i2 = str(i_2)
    str_i3 = str(i_3)
    str_i4 = str(i_4)
    str_i5 = str(i_5)
    str_i6 = str(i_6)

    list_i = list(str_i)
    list_i2 = list(str_i2)
    list_i3 = list(str_i3)
    list_i4 = list(str_i4)
    list_i5 = list(str_i5)
    list_i6 = list(str_i6)

    match_2 = set(list_i) & set(list_i2)
    match_3 = set(list_i) & set(list_i3)
    match_4 = set(list_i) & set(list_i4)
    match_5 = set(list_i) & set(list_i5)
    match_6 = set(list_i) & set(list_i6)

    if len(match_2) == len(list_i):
        print("2:",match_2)
        if len(match_3) == len(list_i):
            print("3:",match_3)
            if len(match_4) == len(list_i):
                print("4:",match_4)
                if len(match_5) == len(list_i):
                    print("5:",match_5)
                    if len(match_6) == len(list_i):
                        print("6:",match_6)

                        print("\nORIGINAL:",list_i)
                        print("I:",i)
                        break


print('\nDuration: ')
print(datetime.now() - startTime)

