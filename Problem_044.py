# Project Euler - Problem #44 - Pentagon Numbers - SOLVED

from datetime import datetime
startTime = datetime.now()

def pentagonal_num(n):
    pentagonal_val = n * (3*n - 1) / 2
    return pentagonal_val

pentagonals = []
for i in range(1,5000):
    x = pentagonal_num(i)
    x = int(x)
    pentagonals.append(x)

pentagonals_a = pentagonals
pentagonals_b = pentagonals

print("\nPENTAGS:")
print(pentagonals)

for pentagonal_x in pentagonals_a:
    for pentagonal_y in pentagonals_b:
        #print("A:",pentagonal_x)
        #print("B:",pentagonal_y)

        added = pentagonal_x + pentagonal_y
        difference = pentagonal_x - pentagonal_y
        difference = abs(difference)
        

        if added in pentagonals and difference in pentagonals:
            print("A:",pentagonal_x)
            print("B:",pentagonal_y)
            print(difference)
            print("Added in Pentagonals:", added)


print('\nDuration: ')
print(datetime.now() - startTime)