# Project Euler - Problem #58 - Spiral Primes - Solved - 1m 58s

import common_functions
from datetime import datetime
startTime = datetime.now()


def num_of_circles(circles):
    x = 8
    current_num = 2
    corners = 2
    diagonals = [1]

    for i in range(circles):
        for z in range(current_num,current_num + x):
            if z == (current_num + x - 1):
                #print("UpperRight:",z-(corners*3))
                #print("UpperLeft:",z-(corners*2))
                #print("LowerLeft:",z-corners)
                #print("LowerRight:",z)

                diagonals.append(z-(corners*3))
                diagonals.append(z-(corners*2))
                diagonals.append(z-corners)
                diagonals.append(z)

        corners += 2
        current_num += x
        x += 8

    num_of_primes_in_diagonals = 0
    for diagonal in diagonals:
        if common_functions.is_prime(diagonal) == True:
            num_of_primes_in_diagonals += 1

    print("\nNumber of Primes:",num_of_primes_in_diagonals)
    print("Number of Diagonals:",len(diagonals))
    percentage = num_of_primes_in_diagonals / len(diagonals) * 100
    percentage = round(percentage, 10)

    if num_of_primes_in_diagonals / len(diagonals) >= 0.1:
        print("\nNumber of Primes is greater than 10%")
        print(percentage,"%")
    elif num_of_primes_in_diagonals / len(diagonals) < 0.1:
        print("\nNumber of Primes is less than 10%")
        print(percentage,"%")

        print("\nLowerLeft:",z-corners)
        print("LowerRight:",z)
        print("Side Length:",(circles*2)+1)


# 13,120 - 9.9998094549 %
# 13,275 - 10.0054612907 %
# 13,280 - 10.0035767399 %
# 13,290 - 10.0035740486 %
# 13,293 - 10.0013164576 %
# 13,294 - 10.0005641537 %
# 13,295 - 9.9998119629 % - 26,591
# 13,300 - 9.9960527058 %
# 13,400 - 9.9867539785 %
# 14,450 - 9.9830858162 %
# 13,500 - 9.99%
# 14,000 - 9.94%
# 15,000 - 9.87%

num_of_circles(13120)

print('\nDuration: ')
print(datetime.now() - startTime)


