# Problem_017.py - Number Letter Counts

import math

ones = {
	'0':'',
	'1':'one',
	'2':'two',
	'3':'three',
	'4':'four',
	'5':'five',
	'6':'six',
	'7':'seven',
	'8':'eight',
	'9':'nine',
	'10':'ten',
	'11':'eleven',
	'12':'twelve',
	'13':'thirteen',
	'14':'fourteen',
	'15':'fifteen',
	'16':'sixteen',
	'17':'seventeen',
	'18':'eighteen',
	'19':'nineteen',}
	
tens = {
	'0':'',
	'1':'',
	'2':'twenty',
	'3':'thrity',
	'4':'forty',
	'5':'fifty',
	'6':'sixty',
	'7':'seventy',
	'8':'eighty',
	'9':'ninety',}
	
large = {
	'3':'hundred',		# Length of number is 3
	'6':'thousand',		# Length of number is between 4-6
	'9':'million',		# length of number is between 7-9
	'12':'billion',		# length of number is between 10-12
	'15':'trillion',	# length of number is between 13-15
	'18':'quadrillion',	# length of number is between 16-18
	'21':'quintillion',	# length of number is between 19-21
	'24':'sextillion',	# length of number is between 22-24
	'27':'septillion',	# length of number is between 25-27
	'30':'octillion',	# length of number is between 28-30
	'33':'nonillion',	# length of number is between 31-33
	'36':'decillion',}	# length of number is between 34-36
	

nums_lens = []
	
spelled = ''
#number = input('What number?\n')


for number in range(1,1001):
	spelled = ''
	print(number)
	
	number_len  = len(str(number))
	
	if number_len == 2 and str(number)[0] == '1':
		spelled += ones[str(number)]
	
	elif number_len == 1:
		spelled += ones[str(number)]
		
	else:	

		if number_len == 2:
			if str(number)[1] == '0':
				spelled += tens[str(number)[:1]]
			else:
				spelled += tens[str(number)[:1]]
				spelled += ones[str(number)[1]]
			
		elif number_len == 3:
			
			if str(number)[:1] == '1':
				spelled += 'one' + large['3']		
			elif str(number)[:1] == '2':
				spelled += 'two' + large['3']
			elif str(number)[:1] == '3':
				spelled += 'three' + large['3']
			elif str(number)[:1] == '4':
				spelled += 'four' + large['3']
			elif str(number)[:1] == '5':
				spelled += 'five' + large['3']
			elif str(number)[:1] == '6':
				spelled += 'six' + large['3']
			elif str(number)[:1] == '7':
				spelled += 'seven' + large['3']
			elif str(number)[:1] == '8':
				spelled += 'eight' + large['3']
			elif str(number)[:1] == '9':
				spelled += 'nine' + large['3']

			
			if str(number)[1] == '1' and str(number)[2] == '0':
				spelled += 'andten'
			elif str(number)[1] == '1' and str(number)[2] == '1':
				spelled += 'andeleven'
			elif str(number)[1] == '1' and str(number)[2] == '2':
				spelled += 'andtwelve'
			elif str(number)[1] == '1' and str(number)[2] == '3':
				spelled += 'andthirteen'
			elif str(number)[1] == '1' and str(number)[2] == '4':
				spelled += 'andfourteen'
			elif str(number)[1] == '1' and str(number)[2] == '5':
				spelled += 'andfifteen'
			elif str(number)[1] == '1' and str(number)[2] == '6':
				spelled += 'andsixteen'
			elif str(number)[1] == '1' and str(number)[2] == '7':
				spelled += 'andseventeen'
			elif str(number)[1] == '1' and str(number)[2] == '8':
				spelled += 'andeighteen'
			elif str(number)[1] == '1' and str(number)[2] == '9':
				spelled += 'andnineteen'
			else:
				if str(number)[1] == '0' and str(number)[2] == '0':
					spelled += tens[str(number)[1]]
				else:
					spelled += 'and' + tens[str(number)[1]]

			
			if str(number)[1] == '1':
				spelled += ''
			elif str(number)[1] == '0':
				spelled += ones[str(number)[2]]
			elif str(number)[2] == '0':
				spelled += ''
			elif str(number)[1] == '0' and str(number)[2] == '0':
				spelled += ''
			else:
				spelled += ones[str(number)[2]]

				
		elif number_len == 4:
			if str(number)[:1] == '1':
				spelled += 'one' + large['6']	
	
	spelled_len = len(spelled)
	print(spelled)
	print(spelled_len)
	nums_lens.append(spelled_len)



	
print(nums_lens)
num_lems_sum = sum(nums_lens)
print('Sum of letters: ' + str(num_lems_sum))
