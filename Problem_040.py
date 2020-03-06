# Project Euler - Problem #40 - Champernowne's Constant - SOLVED - 2.4s

from datetime import datetime
startTime = datetime.now()

y = ''

for i in range (1, 1000000):
    x = str(i)
    y += x

val = int(y[0]) * int(y[9]) * int(y[99]) * int(y[999]) * int(y[9999]) * int(y[99999]) * int(y[999999])

print()
print("VAL:",val)

print()
print('Duration: ')
print(datetime.now() - startTime)