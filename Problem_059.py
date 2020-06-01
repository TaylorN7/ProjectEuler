# Project Euler - Problem #59 - XOR Decryption

import common_functions
from datetime import datetime
startTime = datetime.now()

#ascii_encryption_key = "abcdefghijklmnopqrstuvwxyz"
ascii_encryption_key = "abctz"
ascii_character_vals = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*();:'~`,./<>?"
test_string = "Hello World!"


def get_ascii_char_vals(string):
    print()
    ascii_vals = []
    for char in string:
        ascii_val = ord(char)
        ascii_vals.append(ascii_val)
        #print("Char/Value:",char,ascii_val)

    #print(ascii_vals)
    return ascii_vals

def encrypt(string):
    pre_cypher = get_ascii_char_vals(string)
    pre_cypher = "".join(map(str, pre_cypher))
    print("Pre-Cypher:",pre_cypher)
    pre_cypher_bin = common_functions.convert_to_binary(int(pre_cypher))
    print("Pre-Cypher Binary:",pre_cypher_bin)


#def xor(pre_cypher_bin, encryption_key):


ascii_encryption_key_vals = get_ascii_char_vals(ascii_encryption_key)
ascii_vals_all = get_ascii_char_vals(ascii_character_vals)


for char1 in ascii_encryption_key_vals:
    #print("\nChar 1:",char1)
    for char2 in ascii_encryption_key_vals:
        #print("Char 2:",char2)
        for char3 in ascii_encryption_key_vals:
            #print("Char 3:",char3)

            if len(str(char1)) != 3:
                char1 = "0" + str(char1)
            if len(str(char2)) != 3:
                char2 = "0" + str(char2)
            if len(str(char3)) != 3:
                char3 = "0" + str(char3)

            char1 = int(char1)
            char2 = int(char2)
            char3 = int(char3)

            char1 = format(char1, '03d')
            char2 = format(char2, '03d')
            char3 = format(char3, '03d')

            #char1 = int(char1)
            #char2 = int(char2)
            #char3 = int(char3)


            decryption_key = str(char1) + str(char2) + str(char3)
            print("Decryption Key:",decryption_key)

            decryption_key_bin1 = common_functions.convert_to_binary(char1)
            decryption_key_bin2 = common_functions.convert_to_binary(char2)
            decryption_key_bin3 = common_functions.convert_to_binary(char3)

            decyrption_key_bin = str(decryption_key_bin1) + str(decryption_key_bin2) + str(decryption_key_bin3)

            print("Decryption Key Binary:",decyrption_key_bin)




#pre_cypher_bin_val = encrypt("cat")
encrypt("cat")

print('\nDuration: ')
print(datetime.now() - startTime)