# Project Euler - Problem #51 Prime Digit Replacements

import common_functions
from datetime import datetime
startTime = datetime.now()

# STATUS: Script done for 2 character numbers replacing 1 char each time
# TODO: Update script to allow for replacing 2 characters with the same character

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

prime_digits = {}
for i in range(10,15):
    str_i = str(i)
    
    if common_functions.is_prime(i) == True:
        list_i = list(str_i)
        


        # START OF ORIGINAL
        for x in range(0,len(list_i)):
            val_primes_list = []
            print("\nNUM:",i)
            print("Char Count:",x)

            for num in digits:
                #print("LIST_I[x]",list_i[x])

                #if str(num) != list_i[x]:

                list_i[x] = str(num)
                updated_str = "".join(list_i)
                print("List_I:", updated_str)
                updated_num = int(updated_str)

                if updated_num > 10 and updated_num < 100:
                    if common_functions.is_prime(updated_num) == True:
                        val_primes_list.append(int(updated_str))

            print(val_primes_list)
            
            if i not in prime_digits:
                prime_digits[i] = val_primes_list
                print(prime_digits)
            else:
                #print("HELLO",i)
                if len(prime_digits[i]) >= len(val_primes_list):
                    print(prime_digits)

            list_i = list(str_i)
        # END OF ORIGINAL


max_key = max(prime_digits, key=lambda x: len(set(prime_digits[x])))

print("\nMAX KEY")
print(prime_digits[max_key])

print('\nDuration: ')
print(datetime.now() - startTime)


# 1: Count through numbers of a given length (2 chars, 3 chars, etc.)
# 2: Convert number to a string
# 3: For Char in string, replace Char with all Characters from 0-9
# 4: Add all of the new numbers into a list
# 5: For value in list, get number of primes
# 6: List with most primes = number we care about