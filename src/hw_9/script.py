def first_question():
	# a
	lst: list[float] = []
	SENTINEL: int = -999

	# b
	# simulate user input
	numbers = [123, -10, 1000, 50, 22.2, -23.1, 8.7, -666, SENTINEL]
	for num in numbers:
		if num == SENTINEL:
			break
		if -50 <= num <= 50:
			lst.append(num)

	# c
	lst.extend([-20.0, 39.1, 18.5])

	# d
	new_lst = lst + [4, 5, 6]
	lst.extend([7, 8, 9])

	# e
	max_temperature = max(lst)
	min_temperature = min(lst)

	# f
	exists_18_5 = 18.5 in lst

	# g
	count_neg_20 = lst.count(-20.0)

	# h
	total_sum = sum(lst)
	length = len(lst)
	average_value = total_sum / length if length > 0 else 0

	# i
	print("List elements:")
	for element in lst:
		print(element)

	# j
	index_39_1 = lst.index(39.1) if 39.1 in lst else None

	# k
	if len(lst) > 0:
		del lst[0]

	# l
	for i in range(len(lst) - 1, -1, -1):
		if i % 2 == 0:
			del lst[i]

	# m
	if 18.5 in lst:
		lst.remove(18.5)

	# n
	temp_last = lst.pop() if lst else None

	# o
	copied_lst = lst.copy()
	copied_lst.sort()

	# p
	copied_lst_second = lst.copy()
	copied_lst_reverse = sorted(copied_lst_second, reverse=True)

	print(f"lst: {lst}")
	print(f"max_temperature: {max_temperature}")
	print(f"min_temperature: {min_temperature}")
	print(f"exists_18_5: {exists_18_5}")
	print(f"count_neg_20: {count_neg_20}")
	print(f"total_sum: {total_sum}, length: {length}, average_value: {average_value}")
	print(f"index_39_1: {index_39_1}")
	print(f"temp_last: {temp_last}")
	print(f"copied_lst: {copied_lst}")
	print(f"copied_lst_reverse: {copied_lst_reverse}")


def second_question():
	lst = []
	counts = {}
	index = 0

	# simulate user input
	numbers = [9, 9, 9, 2, 8, 8, 2, 8, 9, 1, 9, 0, -999]

	for num in numbers:
		if num == -999:
			break
		if 0 <= num <= 10:
			lst.append(num)
			counts[num] = counts.get(num, 0) + 1

			if index < len(counts):
				unique_num = list(counts.keys())[index]
				print(f"Statistics: [{unique_num}]: {counts[unique_num]}")
				index += 1


first_question()
# second_question()
