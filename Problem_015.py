# Problem_015.py - Lattice Paths

import math

sides = 20
total_steps = sides * 2
down_steps = sides

top = math.factorial(total_steps)
bot = math.factorial(down_steps) * math.factorial(down_steps)

answer = top / bot

print (answer)