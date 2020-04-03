# Project Euler - Problem #49 - Prime Permutations - Solved 0.02s

import common_functions
from datetime import datetime
startTime = datetime.now()


for x in range(1023,9997):
    a = common_functions.is_prime(x)
   
    if a == True:

        for y in range(3330,3331):
            second_sequence_num = x + y
            b = common_functions.is_prime(second_sequence_num)
            
            if b == True:
                third_sequence_num = second_sequence_num + y
                c = common_functions.is_prime(third_sequence_num)

                if c == True:
                    first_sequence_str = str(x)
                    second_sequence_str = str(second_sequence_num)
                    third_sequence_str = str(third_sequence_num)

                    first_sequence_set = set(first_sequence_str)
                    second_sequence_set = set(second_sequence_str)
                    third_sequence_set = set(third_sequence_str)

                    final_str = first_sequence_str + second_sequence_str + third_sequence_str
                    final_str_set = set(final_str)
                    
                    if len(final_str) == 12:
                        #if len(final_str_set) == 4:
                        if first_sequence_set == second_sequence_set and first_sequence_set == third_sequence_set:

                            print(final_str_set)
                            print("\nY:",y)
                            print('A:', x)
                            print("B:",second_sequence_num)
                            print("C:",third_sequence_num)
                            print("SOLUTION:",final_str)


print('\nDuration: ')
print(datetime.now() - startTime)