# ####################################################################################################################################
# TRY #1
# This try just picked the highest value in each row. They were not necessarily next to each other. Dead end.

# triangle = {1:[75], 2:[95,64], 3:[17,47,82]}
# max_vals = []

# for num,val in triangle.items():
	# print(num, val)


# for i in range(0,3):
	# print('ROW: ' + str(i))
	# print(max(triangle[i + 1]))
	# val = max(triangle[i + 1])
	

	
	# max_vals.append(val)
	
# print(max_vals)






# ####################################################################################################################################
# TRY #2
# This section starts at the top and works down
# For each value selected, it looks to the next row and chooses the highest value it can step to and then goes that direction



# tri = [[75, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [95, 64, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [17, 47, 82, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [18, 35, 87, 10, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [20,  4, 82, 47, 65, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [19,  1, 23, 75,  3, 34, 00, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [88,  2, 77, 73,  7, 63, 67, 00, 00, 00, 00, 00, 00, 00, 00],
	   # [99, 65,  4, 28,  6, 16, 70, 92, 00, 00, 00, 00, 00, 00, 00],
	   # [41, 41, 26, 56, 83, 40, 80, 70, 33, 00, 00, 00, 00, 00, 00],
	   # [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 00, 00, 00, 00, 00],
	   # [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 00, 00, 00, 00],
	   # [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 00, 00, 00],
	   # [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 00, 00],
	   # [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 00],
	   # [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]
	   
# highest_list = [75]	   
	   
# r = 0	   
# v = 0	   
	   
	   
	   
# highest_v = max(tri[r])	   
# print('H: ' + str(highest_v))

# for r in range(15):

	# if r <= 13:
		# #input('>')
		# if tri[r+1][v] > tri[r+1][v+1]:
			# #print("1: " + str(tri[r+1][v]))
			# #print()
			# #print("1: " + str(tri[r+1][v+1]))
			# #input('>')
			# high_v = tri[r+1][v]
			# highest_list.append(high_v)
			
			
		# else:
			# #print("2: " + str(tri[r+1][v]))
			# #print()
			# #print("2: " + str(tri[r+1][v+1]))
			# #input('>')
			# high_v = tri[r+1][v+1]
			# highest_list.append(high_v)
			# v += 1

	# print(highest_list)		
	# r += 1
		   
	   
# print(highest_list)	   
	   
# max_val = sum(highest_list)
# print('MAX: ' + str(max_val))	   
	   
	   

# ####################################################################################################################################
# TRY #3

tri = [[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
	   [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,],
	   [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,],
	   [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,],
	   [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,],
	   [41, 48, 72, 33, 47, 32, 37, 16, 94, 29,],
	   [41, 41, 26, 56, 83, 40, 80, 70, 33,],
	   [99, 65,  4, 28,  6, 16, 70, 92,],
	   [88,  2, 77, 73,  7, 63, 67,],
	   [19,  1, 23, 75,  3, 34,],
	   [20,  4, 82, 47, 65,],
	   [18, 35, 87, 10,],
	   [17, 47, 82,],
	   [95, 64,],
	   [75,]]
	
for r in range(0,14):	   

	new_tri = []	
	v = 0
	r = 1

	length = len(tri[r])
	for x in range(length):
		
		if tri[r][v] + tri[r-1][v] > tri[r][v] + tri[r-1][v+1]:
			print(tri[r][v])
			print(tri[r-1][v])
			print(tri[r][v] + tri[r-1][v])
			val = tri[r][v] + tri[r-1][v]
			
			new_tri.append(val)
			
		else:
			print(tri[r][v])
			print(tri[r-1][v+1])
			print(tri[r][v] + tri[r-1][v+1])
			val = tri[r][v] + tri[r-1][v+1]
			
			new_tri.append(val)

		if v < length - 1:
			v += 1
			
	tri.pop(0)
	tri.pop(0)
	print(new_tri)
	tri.insert(0, new_tri)
	print()
	print(tri)		
	print()
	































	   

	

