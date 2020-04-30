# Project Euler - Problem #57 - Square Root Convergents - Solved - 0.01s

from decimal import Decimal
from fractions import Fraction
from datetime import datetime
startTime = datetime.now()


p = 1
q = 1
#new_n = (n+(2*d)) / (n + d)
more_digits = []

#print(new_n)
for i in range(1,1000):

    
    # I would like to get this to work, but I run into a limitation with Python
    # I am maxing out the number of decimals that it will show
    # And then maxing out the capability of Fraction() from that number of decimals
    '''
    new_n = (new_n+(2*d)) / (new_n + d)
    print("\nI:", i+1)
    #print("%.100f" % new_n)
    print(new_n)

    new_frac = str(Fraction(new_n).limit_denominator(1000000))
    print(new_frac)

    frac_split = new_frac.split('/')
    print(frac_split)

    if len(frac_split[0]) > len(frac_split[1]):
        more_digits.append(new_frac)

    '''

    numerator = p + 2*q
    denominator = p + q


    if len(str(numerator)) > len(str(denominator)):
        more_digits.append(str(numerator) + "/" + str(denominator))

    p = numerator
    q = denominator


print("\nNum of More Digits in Numerator:")
print(len(more_digits))
#print(more_digits)

print('\nDuration: ')
print(datetime.now() - startTime)