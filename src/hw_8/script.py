import random


def first_question():
	# a
	num_list: list[int] = []
	for i in range(1, 101):
		num_list.append(i)
	print("num_list", num_list)
	# b
	print("num_list[0]", num_list[0])
	# c
	print("num_list[-1]", num_list[-1])
	# d
	print("len(num_list)", len(num_list))
	# e
	new_num_list_e = num_list[2: 12]
	print("new_num_list_e", new_num_list_e)
	# f
	new_num_list_f = num_list[79:]
	print("new_num_list_f", new_num_list_f)
	# g
	new_num_list_g = num_list[:18]
	print("new_num_list_g", new_num_list_g)
	# h
	new_num_list_h = num_list[::-1]
	print("new_num_list_h", new_num_list_h)
	# i
	new_num_list_i = num_list[1::2]
	print("new_num_list_i", new_num_list_i)
	# j
	new_num_list_j = num_list[2::3]
	print("new_num_list_j", new_num_list_j)
	# k
	new_num_list_k = num_list[6::7]
	print("new_num_list_k", new_num_list_k)
	# l
	new_num_list_l = num_list[9::10]
	print("new_num_list_l", new_num_list_l)
	# m
	new_num_list_m = num_list[65::3][::-1]
	print("new_num_list_m", new_num_list_m)
	# n
	num_list.insert(50, 999)
	print("num_list n", num_list)
	# o
	num_list.pop()
	print("num_list o", num_list)


def second_question():
	player_heights: list[float] = []

	for i in range(10):
		# simulate user input
		height = round(random.uniform(1, 4), 2)
		if height == -999:
			break
		if height < 1.60 or height > 3.0:
			continue
		player_heights.append(height)

	num_players = len(player_heights)
	max_height = max(player_heights)
	min_height = min(player_heights)
	average_height = sum(player_heights) / num_players
	taller_than_2m = 0
	for height in player_heights:
		if height > 2.0:
			taller_than_2m += 1
	taller_than_average = 0
	for height in player_heights:
		if height > average_height:
			taller_than_average += 1

	print("player_heights", player_heights)
	print("num_players", num_players)
	print("max_height", max_height)
	print("min_height", min_height)
	print("average_height", average_height)
	print("taller_than_2m", taller_than_2m)
	print("taller_than_average", taller_than_average)

# first_question()
# second_question()
