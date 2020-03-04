# Problem_002.py - Even Fibonacci Numbers - Sum of even numbers in Fibonacci sequence whos values dont exceed 4 million

list = []
a = 1
b = 2	

while a < 4000000:
	
	print(a)
	a, b = b, a + b
	
	if a % 2 == 0:
		list.append(a)
		
list_sum = sum(list)
print('Sum of Evens: ' + str(list_sum))
	

	
	
