# Project Euler - Problem #39 - Interger Right Triangles - SOLVED - 1min 51s

from datetime import datetime
startTime = datetime.now()

solutions = {}

for i in range(10, 999):
    right_triangles = []
    for x in range(1, int(i/2)):
        for y in range(1, int(i/2)):
            z = i - (y + x)

            if x + y + z == i:
                x_sq = x**2
                y_sq = y**2
                z_sq = z**2

                if x_sq + y_sq == z_sq:
                    right_triangles.append(i)
                    solutions[i] = int(len(right_triangles)/2)


max_value = max(solutions, key=solutions.get)
print(max_value, solutions[max_value])
# print(solutions[max_value])
# print(solutions)
print()
print('Duration: ')
print(datetime.now() - startTime)

