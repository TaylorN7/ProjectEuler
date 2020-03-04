# Answer: 45228
# Time: 9.2 seconds

from datetime import datetime
startTime = datetime.now()

z = 0
sums = []

for x in range(1,1000):
	
	#print('X: ' + str(x))
	
	x = str(x)

	for y in range(1,2000):
		
		nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

		x_list = []
		for x_char in x:
			x_list.append(x_char)

		y = str(y)
		y_list = []
		
		for y_char in y:
			y_list.append(y_char)
			
		z = int(x) * int(y)
		z = str(z)
		
		z_list = []
		for z_char in z:
			z_list.append(z_char)	
		
		#print(x_list)
		#print(y_list)
		#print(z_list)
		a_list = x_list + y_list + z_list
		#print(a_list)
		#print(set(a_list))
		
		if len(a_list) != len(set(a_list)):
			#print('There are duplicates')
			continue
			
		elif len(set(a_list)) > 9:
			#print('Too many numbers')
			continue
			
		elif len(set(a_list)) < 9:
			#print('Not enough numbers')
			continue
			
		elif len(set(a_list)) == 9:
			#print('Thats JUSSSST Right!')
			
			a_list = list(map(int, a_list))
			a_list_sum = sum(a_list)
					
			for a_char in a_list:
				#print('A_Char: ' + str(a_char))
				
				if a_char in nums:
					
					nums.remove(a_char)
					#print(str(a_char) + ' Removed from Nums')
					
					if not nums:
						
						sums.append(z)
						#print('Z: ' + str(z))

	
sums = list(map(int, sums))
sums = set(sums)
#print(sums)	
sums_len = len(sums)
#print('Number of Pandigital Products: ' + str(sums_len))

total = sum(sums)
print(total)
		
print('Duration: ')
print(datetime.now() - startTime)

	
				
			
				

		