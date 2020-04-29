# Project Euler - Problem #55 - Lychrel Numbers - SOLVED - 0.07s

from datetime import datetime
startTime = datetime.now()

def lychrel_numbers(start,end):
    lychrel_nums = []
    palindrome_nums = []

    for i in range(start, end):
        #print("\nI:",i)
        a = 0
        str_i = str(i)
        while a != 51:
            #str_i = str(i)
            #print("STR_I:",str_i)
            #print("STR_I Type:",type(str_i))
            reverse_i = str_i[::-1]
            #print("Reverse I:",reverse_i)
            added_i = int(str_i) + int(reverse_i)
            added_i = str(added_i)
            #print("Added I:",str(added_i))

            if added_i == added_i[::-1]:
                #print("Added I:",str(added_i), "is a palindrome.")
                palindrome_nums.append(i)
                a = 51
            else:
                #print("Added I:",str(added_i), "is NOT a palindrome.")        
                str_i = added_i
                str_i = str(str_i)
                a += 1

                if a == 51:
                    lychrel_nums.append(i)

    #print("\nPalindrome Numbers:")
    #print(palindrome_nums)

    print("\nLychrel Numbers:")
    print(lychrel_nums)
    print("Number of Lychrel Nums:", len(lychrel_nums))


lychrel_numbers(10,10000)

print('\nDuration: ')
print(datetime.now() - startTime)
