#!python3 - common_functions.py - compilation of common functions I use in my programs

# Common Function: 01
# get_primes() will get all prime numbers below a certain specified value and add them to the list prime_list
def get_primes():
	import math
	
	c = int(input('What number should I start with?\n')) 
	n = int(input('What number should I go to?\n')) 
	prime_list = []
	
	for num in range(c, n, 2):
		if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
			
			#print('Number: ' + str(num))
			prime_list.append(num)
	
	return prime_list

# Common Function: 02
# is_prime(n) will determine if provided 'n' is prime or not
def is_prime(n):
	import math
	
	if n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	return all(n%x for x in range(3, int(math.sqrt(n) + 1), 2))
	
	
# Common Function: 03
# is_a_palindrome(n) will determine if provided 'n' is the same forward and backward
def is_a_palindrome(n):	
	str_n = str(n)
	len_n = len(str_n)
	
	if str_n[:len_n] == str_n[::-1]:
		return True
		# print(str_n + ' is a palindrome')
		
	else:
		print(str_n + ' is NOT a palindrome')

	
# Common Function: 04
# convert_to_binary(n) will convert 'n' from an int to binary and remove the '0b' notifier
def convert_to_binary(n):
	bin_n = bin(n)
	bin_n = bin_n[2:]
	print(bin_n)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
