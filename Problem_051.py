# Project Euler - Problem #51 Prime Digit Replacements

import common_functions
from datetime import datetime
startTime = datetime.now()

# STATUS: Works for 5-char numbers (up to replacing 2)

def character_replacement(list_i):
    for num_of_chars in range(1, len(list_i)):
        print("\nNUM OF CHARS:", num_of_chars)
        #print()
        
        # Replace 1 Character
        if num_of_chars == 1:
            print("Replace 1 Character")
            
            # START OF ORIGINAL
            for x in range(0,len(list_i)):
                val_primes_list = []
                #print("NUM:",i)
                #print("Char Count:",x)

                for num in digits:
                    list_i[x] = str(num)
                    updated_str = "".join(list_i)
                    #print("List_I:", updated_str)
                    updated_num = int(updated_str)

                    if updated_num > 10 and updated_num < 100000:
                        if common_functions.is_prime(updated_num) == True:
                            val_primes_list.append(int(updated_str))
                
                if i not in prime_digits:
                    prime_digits[i] = val_primes_list
                    #print(prime_digits)
                elif i in prime_digits:
                    if len(val_primes_list) >= len(prime_digits[i]):
                        #print(val_primes_list)
                        #print(prime_digits[i])
                        prime_digits[i] = val_primes_list
                        #print(prime_digits)

                list_i = list(str_i)
            # END OF ORIGINAL

        # Replace 2+ characters 
        elif num_of_chars == 2:
            print("Replace 2 Characters")

            for x in range(0,len(list_i)):
                val_primes_list = []
                print("NUM:",i)
                print("Char Count:",x)
                print("LEN LIST I:", len(list_i))

                for num in digits:
                    #print("X:",x)
                    
                    # First Number
                    if x == 0:
                        for num_vals in range(1,len(list_i)-1):
                            list_i[x] = str(num)
                            list_i[x+num_vals] = str(num)
                            updated_str = "".join(list_i)
                            print("List_I:", updated_str)
                            updated_num = int(updated_str)
                            list_i = list(str_i)

                    elif x > 0 and x < len(list_i)-1:
                        num_difference = (len(list_i)-1) - 1
                        for num_vals in range(1,num_difference):

                            if x == 1: 
                                list_i[x] = str(num)
                                list_i[x+num_vals] = str(num)
                            list_i[x] = str(num)
                            list_i[x+1] = str(num)
                            updated_str = "".join(list_i)
                            print("List_I:", updated_str)
                            updated_num = int(updated_str)
                            list_i = list(str_i)
                        
                    # Last Number
                    elif x == len(list_i)-1:
                        for num_vals in range(2,len(list_i)):
                            list_i[x] = str(num)
                            list_i[x-num_vals] = str(num)
                            updated_str = "".join(list_i)
                            print("List_I:", updated_str)
                            updated_num = int(updated_str)
                            list_i = list(str_i)

                    if updated_num > 100 and updated_num < 100000:
                        if common_functions.is_prime(updated_num) == True:
                            val_primes_list.append(int(updated_str))

                if i not in prime_digits:
                    prime_digits[i] = val_primes_list
                    print(prime_digits)
                elif i in prime_digits:
                    if len(val_primes_list) >= len(prime_digits[i]):
                        print(val_primes_list)
                        print(prime_digits[i])
                        prime_digits[i] = val_primes_list
                        print(prime_digits)

                list_i = list(str_i)


        # START WORKING HERE - EVERYTHING ABOVE WORKS
        elif num_of_chars == 3:
            print("Replace 3 Characters")
            for x in range(0,len(list_i)-1):
                val_primes_list = []
                print("NUM:",i)
                print("Char Count:",x)
                print("LEN LIST I:", len(list_i))

                for num in digits:
                    #print("X:",x)
                    
                    if x == 0:
                        for num_vals in range(1,len(list_i)-2):
                            list_i[x] = str(num)
                            list_i[x+num_vals] = str(num)
                            list_i[x+num_vals+1] = str(num)
                            updated_str = "".join(list_i)
                            print("List_I:", updated_str)
                            updated_num = int(updated_str)
                            list_i = list(str_i)

                    elif x > 0 and x < len(list_i)-2:
                        num_difference = (len(list_i)-1) - 1
                        for num_vals in range(1,num_difference):

                            if x == 1: 
                                list_i[x] = str(num)
                                list_i[x+num_vals] = str(num)
                                list_i[x+num_vals+1] = str(num)
                            else: 
                                list_i[x] = str(num)
                                list_i[x+1] = str(num)
                                list_i[x+2] = str(num)
                            updated_str = "".join(list_i)
                            print("List_I:", updated_str)
                            updated_num = int(updated_str)
                            list_i = list(str_i)
                        
                    # Last Number
                    elif x == len(list_i)-1:
                        for num_vals in range(2,len(list_i)):
                            list_i[x] = str(num)
                            list_i[x-num_vals] = str(num)
                            list_i[x-num_vals] = str(num)-2
                            updated_str = "".join(list_i)
                            print("List_I:", updated_str)
                            updated_num = int(updated_str)
                            list_i = list(str_i)

                    if updated_num > 1000 and updated_num < 100000:
                        if common_functions.is_prime(updated_num) == True:
                            val_primes_list.append(int(updated_str))

                if i not in prime_digits:
                    prime_digits[i] = val_primes_list
                    print(prime_digits)
                elif i in prime_digits:
                    if len(val_primes_list) >= len(prime_digits[i]):
                        print(val_primes_list)
                        print(prime_digits[i])
                        prime_digits[i] = val_primes_list
                        print(prime_digits)

                list_i = list(str_i)

'''
        elif num_of_chars == 4:
            print("Replace 4 Characters")
            for x in range(0,len(list_i)):
                val_primes_list = []
                print("NUM:",i)
                print("Char Count:",x)
                print("LEN LIST I:", len(list_i))

                for num in digits:
                    #print("X:",x)
                    

                    if x != len(list_i)-3:
                        list_i[x] = str(num)
                        list_i[x+1] = str(num)
                        list_i[x+2] = str(num)
                        list_i[x+3] = str(num)
                        updated_str = "".join(list_i)
                        print("List_I:", updated_str)
                        updated_num = int(updated_str)
                    elif x != len(list_i)-2:
                        list_i[x] = str(num)
                        list_i[x+1] = str(num)
                        list_i[x+2] = str(num)
                        list_i[x-2] = str(num)
                        updated_str = "".join(list_i)
                        print("List_I:", updated_str)
                        updated_num = int(updated_str)
                    elif x != len(list_i)-1:
                        list_i[x] = str(num)
                        list_i[x+1] = str(num)
                        list_i[x-2] = str(num)
                        list_i[x-3] = str(num)
                        updated_str = "".join(list_i)
                        print("List_I:", updated_str)
                        updated_num = int(updated_str)
                    else:
                        list_i[x] = str(num)
                        list_i[x-2] = str(num)
                        list_i[x-3] = str(num)
                        list_i[x-4] = str(num)
                        updated_str = "".join(list_i)
                        print("List_I:", updated_str)
                        updated_num = int(updated_str)

                    if updated_num > 10000 and updated_num < 100000:
                        if common_functions.is_prime(updated_num) == True:
                            val_primes_list.append(int(updated_str))

                if i not in prime_digits:
                    prime_digits[i] = val_primes_list
                    print(prime_digits)
                elif i in prime_digits:
                    if len(val_primes_list) >= len(prime_digits[i]):
                        print(val_primes_list)
                        print(prime_digits[i])
                        prime_digits[i] = val_primes_list
                        print(prime_digits)

                list_i = list(str_i)




                        if num_of_chars == 5:
                            print("Replace 5 Characters")

                            if num_of_chars == 6:
                                print("Replace 6 Characters") '''
    

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

prime_digits = {}
for i in range(56003,56004):
    str_i = str(i)
    
    if common_functions.is_prime(i) == True:
        list_i = list(str_i)
        character_replacement(list_i)

max_key = max(prime_digits, key=lambda x: len(set(prime_digits[x])))

print("\nMAX KEY")
print(prime_digits[max_key])
print("Number of Primes:", len(prime_digits[max_key]))

print('\nDuration: ')
print(datetime.now() - startTime)

