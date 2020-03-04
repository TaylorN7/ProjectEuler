# Answer: 872187
# Time: 0.68 seconds

from datetime import datetime
startTime = datetime.now()

palindromes_list = []

def convert_to_binary(n):
	bin_n = bin(n)
	bin_n = bin_n[2:]
	bin_is_a_palindrome(bin_n, n)

def is_a_palindrome(n):	
	str_n = str(n)
	len_n = len(str_n)
	
	if str_n[:len_n] == str_n[::-1]:
		convert_to_binary(n)
		
def bin_is_a_palindrome(bin, n):	
	str_n = str(n)
	str_bin = str(bin)
	len_n = len(str_n)
	len_bin = len(bin)

	if str_bin[:len_bin] == str_bin[::-1]:
		palindromes_list.append(n)

for i in range(1, 1000000):
	#print(i)
	is_a_palindrome(i)
	
print(palindromes_list)
palindromes_sum = sum(palindromes_list)
print('Palindromes Sum: ' + str(palindromes_sum))

print('Duration: ')
print(datetime.now() - startTime)