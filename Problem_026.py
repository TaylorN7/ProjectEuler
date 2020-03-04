# Problem_026.py - reciprocal cycles

from datetime import datetime
startTime = datetime.now()

import math
from decimal import *



# #################################################################################################################
# First attempt - Try to add characters individually to a list and then compare the list to another list
# Solved: 8.7 seconds

# Avoid looking below for the answer







# Look away unless you want to see the answer







# Seriously, dont look here







# Answer: 983

'''
0.00101729399796541200406917599186164801627670396744659206510681586978636826042726347914547304170905391658189216683621566632
756866734486266531027466937945066124109867751780264496439471007121057985757884028484231943031536113936927772126144455747
711088504577822990844354018311291963377416073245167853509664292980671414038657171922685656154628687690742624618514750762
970498474059003051881993896236012207527975584944048830111902339776195320447609359104781281790437436419125127161749745676
500508646998982706002034587995930824008138351983723296032553407934893184130213631739572736520854526958290946083418107833
163784333672431332655137334689725330620549338758901322482197355035605289928789420142421159715157680569684638860630722278
738555442522889114954221770091556459816887080366225839267548321464903357070193285859613428280773143438453713123092573753
814852492370295015259409969481180061037639877924720244150559511698880976602238046795523906408952187182095625635808748728
3825025432349949135300
'''

getcontext().prec = 10000

reps = ''
final_reps = []


for x in range(2,2000):

	#print('1 / ' + str(x))
	string = Decimal(1) / Decimal(x)
	#print(string)
	string = str(string)
	string = string[4:]
	#print(string)

	rep_list = []
	i = 0
	a = 0

	string_list = []

	for char in string:
		string_list.append(string[a])
		a += 1
		
	#print(string_list)	


	for character in string:
		
		#print(character)
		rep_list.append(character)
		rep_len = len(rep_list)
		char_step = i
		#print(rep_len)
		#print(rep_list)
		#print(string[:rep_len])
		#print('I: ' + str(i))
		#print('String List ' + str(string_list[i+1:i+i+2]))
		
		if rep_list == string_list[i+1:i+i+2]:
			#print('Rep_List: ' + str(rep_list))
			#print('1 / ' + str(x))
			reps = ''.join(rep_list)
			final_reps.append(reps)
			#print(reps)
			break
			
		#else:
		#	print('No Repeats')
			
			
		#input()
		i += 1

		
#print('Final Reps: ' + str(final_reps))

longest_repeat = max(final_reps, key=len)
print('Longest Repeat: ' + str(longest_repeat))
print('Length: ' + str(len(longest_repeat)))



print('Duration: ')
print(datetime.now() - startTime)


