bot_start = 10

not_in = [20, 30, 40, 50,60, 70, 80, 90]

top_list = []
bot_list = []

for top in range(10,100):

	for bot in [x for x in range(bot_start,100) if x not in not_in]:

		top = str(top)
		bot = str(bot)

		if top[1] == bot[0]:

			top_0 = top[0]
			top_0 = int(top_0)

			bot_1 = bot[1]
			bot_1 = int(bot_1)
			bot = int(bot)
			top = int(top)

			fraction = (top / bot)

			if (top / bot) == (top_0 / bot_1):
				if top != bot:

					print('TOP ' + str(top))
					print('BOT ' + str(bot))
					print(fraction)

					top_list.append(top_0)
					bot_list.append(bot_1)

			bot = int(bot)
			top = int(top)
			bot += 1
	
	bot_start += 1

print(top_list)
print(bot_list)

top_val = 1
bot_val = 1

for i in top_list:
	top_val *= i

for y in bot_list:
	bot_val *= y
	
print(top_val)
print(bot_val)

reduced_val = top_val / bot_val
print(reduced_val)
