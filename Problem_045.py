# Project Euler - Problem #45 - Triangular, Pentagonal, and Hexagonal - SOLVED - 67s

from datetime import datetime
startTime = datetime.now()

def triangle_nums(n):
    x = n * (n + 1) / 2
    x = int(x)
    #print(x)
    return x

def pentagonal_nums(n):
    y = n * ((3 * n) - 1) / 2
    y = int(y)
    #print(y)
    return y

def hexagonal_nums(n):
    z = n * (2 * n - 1)
    z = int(z)
    #print(z)
    return z

triangle_num_list = []
pentagonal_num_list = []
hexagonal_num_list = []
all_list = []

#triangle_example = triangle_nums(285)
#pentagonal_example = pentagonal_nums(165)
#hexagonal_example = hexagonal_nums(143)

for i in range(285, 80000):
    triangle_num = triangle_nums(i)
    triangle_num_list.append(triangle_num)

for i in range(165, 60000):
    pentagonal_num = pentagonal_nums(i)
    pentagonal_num_list.append(pentagonal_num)

for i in range(143, 60000):
    hexagonal_num = hexagonal_nums(i)
    hexagonal_num_list.append(hexagonal_num)

for tri_num in triangle_num_list:
    if tri_num in pentagonal_num_list and tri_num in hexagonal_num_list:
        print("\nTRIANGLE NUMBER:",tri_num)
        all_list.append(tri_num)

print(all_list)

print('\nDuration: ')
print(datetime.now() - startTime)