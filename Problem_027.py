import math

# Problem_027.py - Quadratic Primes

import math, sys

sys.setrecursionlimit(2000)
#sys.stdout = open('c:\\users\\tneves\\desktop\\problem27.txt', 'w')

go_to = 1001

c = (-1001)
y = (-1001)

a_b_products = []
dict = {}

def over():
    #print('END')
    sys.exit()
			
def find_max_primes(s):
	global y
	global c
	#print('C: ' + str(c))

	for a in range(s, go_to):
	#for a in range(-61,-62,-1):
		#print('A: ' + str(a))
		
		
		for b in range(y,go_to):
		#for b in range(971,972):
			#print('B: ' + str(b))
			num_of_primes = 0

			
			for n in range(0,1001):

				num = n**2 + (a*n) + b

				#print('N: ' + str(n))

				if all(num%i!=0 for i in range(2, int(math.sqrt(abs(num)))+1)):
					#print('PRIME: ' + str(num))
					num_of_primes += 1
					#input()
				
				else:
					#print()
					#print('A: ' + str(a))
					#print('B: ' + str(b))
					#print('N: ' + str(n))
					a_b = a*b
					
					dict[num_of_primes] = a_b
					
					#print('A, B Product: ' + str(a_b))
					#print('Number of Primes: ' + str(num_of_primes))
					#print('~~~~~~~~~~~~~~~~~~~~')
					#print('~~~~~~~~~~~~~~~~~~~~')
					
					if c != go_to:
						c += 1
						#find_max_primes(c)
						break
						
					else:
						over()
			
						
			#print('Number of Primes: ' + str(num_of_primes))			
		
		c+=1	
			
find_max_primes(c)	

print(dict)

