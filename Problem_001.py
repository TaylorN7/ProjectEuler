# Problem_001.py - Sum of all numbers divisible by 3 or 5 that are less than 1000

i_list = []

i = 1

while i < 1000:
	if i % 3 == 0 or i % 5 == 0: 
		print(i)
		i_list.append(i)
		
	i += 1	
		
		
sum_list = sum(i_list)
print(sum_list)