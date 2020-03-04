# Problem_006.py - Sum Square Difference - Difference between square of sum and sum of square


import math

squares = []

i = 0
y = 0


# Sum of Squares
for i in range(101):
	x = i ** 2
	squares.append(x)
	print(x)
	
sum_of_squares = sum(squares)
print('X: ' + str(sum_of_squares))
	
#print('X: ' + str(x))

# Square of Sums
y = (100 * (100 + 1)) / 2
print('Y: ' + str(y))

y_2 = y ** 2
print('Y2: ' + str(y_2))


# The Difference
print('Difference: ' + str((y_2 - sum_of_squares)))