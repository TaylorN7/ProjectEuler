
r = 499
change_value = 8
value = 1
print(value)


start_1 = 3
start_1x = 2
list_1 = [3]

start_2 = 5
start_2x = 4
list_2 = [5]

start_3 = 7
start_3x = 6
list_3 = [7]

start_4 = 9
start_4x = 8
list_4 = [9]


print(start_1)
start_1 = start_1 + start_1x

for val1 in range(r):
	start_1 = start_1 + change_value
	print(start_1)
	list_1.append(start_1)
	change_value = change_value + start_1x + 8
	start_1x = 0
	val1 += 1
	
	

print()
change_value = 8
print(start_2)
start_2 = start_2 + start_2x

for val2 in range(r):
	start_2 = start_2 + change_value
	#print(start_2)
	list_2.append(start_2)
	change_value = change_value + start_2x + 8
	start_2x = 0
	val2 += 1
	

	
print()	
change_value = 8
print(start_3)
start_3 = start_3 + start_3x

for val3 in range(r):
	start_3 = start_3 + change_value
	#print(start_3)
	list_3.append(start_3)
	change_value = change_value + start_3x + 8
	start_3x = 0
	val3 += 1	
	
	
	
print()	
change_value = 8
print(start_4)
start_4 = start_4 + start_4x

for val4 in range(r):
	start_4 = start_4 + change_value
	#print(start_4)
	list_4.append(start_4)
	change_value = change_value + start_4x + 8
	start_4x = 0
	val4 += 1	
		
	
	
list_1_sum = sum(list_1)
print(list_1_sum)
print(len(list_1))

list_2_sum = sum(list_2)
print(list_2_sum)
print(len(list_2))

list_3_sum = sum(list_3)
print(list_3_sum)
print(len(list_3))

list_4_sum = sum(list_4)
print(list_4_sum)
print(len(list_4))

	
	
total_sum = list_1_sum + list_2_sum + list_3_sum + list_4_sum + 1
print()
print(total_sum)
	
	
	
	
	
	
