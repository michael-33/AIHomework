# conditions

def conditions_1():
	first_num: int = int(input("enter first number"))
	second_num: int = int(input("enter second number"))
	smaller_num: int = first_num if first_num < second_num else second_num
	for _ in range(3):
		print("smaller_num", smaller_num)


def conditions_2():
	first_num: int = int(input("enter first number"))
	second_num: int = int(input("enter second number"))
	average = (first_num + second_num) / 2
	print("average", average)


def conditions_3():
	nums = []
	for _ in range(3):
		num: int = int(input("enter number"))
		nums.append(num)
	print("max num", max(nums))


def conditions_4():
	minutes: int = int(input("enter minutes"))
	hours = minutes // 60
	relative_minutes = minutes % 60
	print(f"{hours} hours and {relative_minutes} minutes")


def conditions_5():
	num = int(input("enter number with 4 digits"))
	right_digit = num % 10
	print("right_digit", right_digit)


def conditions_6():
	num = int(input("enter number with 4 digits"))
	second_right_digit = num // 10 % 10
	print("second_right_digit", second_right_digit)


def conditions_7():
	num = int(input("enter number with 2 digits"))
	right_digit = num % 10
	left_digit = num // 10
	digits_sum = right_digit + left_digit
	print("digits_sum", digits_sum)


def conditions_8():
	num = int(input("enter number with 2 digits"))
	right_digit = num % 10
	left_digit = num // 10
	reverse_num = right_digit * 10 + left_digit
	print("reverse_num", reverse_num)


def conditions_9():
	num = int(input("enter number"))
	is_even = num % 2 == 0
	print("even" if is_even else "odd")


def conditions_10():
	salary = int(input("enter salary"))
	tax: float = 0
	while True:
		match salary:
			case _ if salary > 50_000:
				relative_portion = salary - 50_000
				tax += relative_portion * 0.51
				salary -= relative_portion
			case _ if salary > 35_000:
				relative_portion = salary - 35_000
				tax += relative_portion * 0.45
				salary -= relative_portion
			case _ if salary > 25_000:
				relative_portion = salary - 25_000
				tax += relative_portion * 0.4
				salary -= relative_portion
			case _ if salary > 18_000:
				relative_portion = salary - 18_000
				tax += relative_portion * 0.3
				salary -= relative_portion
			case _ if salary > 12_000:
				relative_portion = salary - 12_000
				tax += relative_portion * 0.2
				salary -= relative_portion
			case _ if salary > 6_000:
				relative_portion = salary - 6_000
				tax += relative_portion * 0.1
				salary -= relative_portion
			case _:
				break
	print("tax", tax)


def conditions_11():
	age = int(input("enter age"))
	height = int(input("enter height"))
	first_condition = 8 <= age < 18 and height > 115
	second_condition = age >= 18 and height > 100
	is_allowed = first_condition or second_condition
	print("is allowed", is_allowed)


# loops

def loops_1():
	top = int(input("enter number"))
	for i in range(1, top + 1):
		print(i, end=" ")


def loops_2():
	first_num: int = int(input("enter first number"))
	second_num: int = int(input("enter second number"))
	top = first_num if first_num > second_num else second_num
	bottom = second_num if second_num < first_num else first_num
	for i in range(bottom, top + 1):
		print(i, end=" ")


def loops_3():
	num: int = int(input("enter number"))
	top = num + 1 if num % 2 == 0 else num
	for i in range(0, top, 2):
		print(i, end=" ")


def loops_4():
	max_num: int = int(input("enter first number"))
	den_num: int = int(input("enter second number"))
	for i in range(max_num + 1):
		if i % den_num == 0:
			print(i, end=" ")


# data process

def data_process_1():
	nums_sum: int = 0
	SENTINEL: int = -99
	is_sentinel_on_first_input = True
	while True:
		num = int(input("enter number"))
		if num == SENTINEL:
			break
		if is_sentinel_on_first_input:
			is_sentinel_on_first_input = False
		nums_sum += num
	print(nums_sum if not is_sentinel_on_first_input else "None")


def data_process_2():
	highest_num = None
	lowest_num = None
	is_sentinel_on_first_input = True
	while True:
		num = int(input("enter number"))
		if num <= 0:
			break
		if is_sentinel_on_first_input:
			is_sentinel_on_first_input = False
		if highest_num is None or num > highest_num:
			highest_num = num
		if lowest_num is None or num < lowest_num:
			lowest_num = num
	if is_sentinel_on_first_input:
		print("None")
	else:
		print("highest_num", highest_num)
		print("lowest_num", lowest_num)


def data_process_3():
	height_index = 1
	highest_num = None
	for i in range(1, 6):
		num = int(input("enter number"))
		if highest_num is None or num > highest_num:
			highest_num = num
			height_index = i
	print("height_index", height_index)


def data_process_4():
	first_num: int = int(input("enter first number"))
	second_num: int = int(input("enter second number"))
	multiplication: int = 0
	for _ in range(first_num):
		multiplication += second_num
	print("multiplication", multiplication)


def data_process_5():
	first_num: int = int(input("enter first number"))
	second_num: int = int(input("enter second number"))
	power: int = 1
	for _ in range(first_num):
		power *= second_num
	print("power", power)


def data_process_6():
	num: int = int(input("enter number"))
	digit: int = int(input("enter digit"))
	num_digits: list[int] = []
	while True:
		if num < 10:
			num_digits.append(num)
			break
		else:
			right_digit = num % 10
			num_digits.append(right_digit)
			num //= 10
	print(digit in num_digits)


def data_process_7():
	first_num: int = int(input("enter first number"))
	second_num: int = int(input("enter second number"))
	highest_divider = 1
	top = first_num if first_num < second_num else second_num
	for i in range(1, top + 1):
		if first_num % i == 0 and second_num % i == 0:
			highest_divider = i
	print("highest_divider", highest_divider)


def data_process_8():
	num: int = int(input("enter number"))
	is_prime: bool = True
	if num <= 1:
		is_prime = False
	else:
		for i in range(2, int(num ** 0.5) + 1):
			if num % i == 0:
				is_prime = False
				break
	print("is_prime", is_prime)


# complex loops

def complex_loops_1():
	temperatures: list[int] = []
	is_wrong_data = False
	while len(temperatures) < 12:
		try:
			temperature = int(input("enter temperature"))
			if temperature < -5 or temperature > 40:
				is_wrong_data = True
				break
			if len(temperatures) > 0 and temperature == 0 and temperatures[-1] == 0:
				continue
			temperatures.append(temperature)
		except:
			print("invalid input, enter only numbers")
	if is_wrong_data:
		print("wrong data")
		return
	print("correct data")
	max_temperature = max(temperatures)
	min_temperature = min(temperatures)
	average = sum(temperatures) / len(temperatures)
	print("max_temperature", max_temperature)
	print("min_temperature", min_temperature)
	print("average", average)


def complex_loops_2():
	for_states_indexes: list[int] = []
	against_states_indexes: list[int] = []
	avoided_states_indexes: list[int] = []
	vote_subject = input("enter vote subject")
	for i in range(1, 45):
		try:
			vote = int(input("enter vote between 1 to 4"))
			match vote:
				case 1:
					for_states_indexes.append(i)
				case 2:
					against_states_indexes.append(i)
				case 3:
					avoided_states_indexes.append(i)
				case 4:
					print(f"state number {i} vetoed the vote")
					break
				case _:
					continue
		except:
			print("invalid input, enter only numbers")
	print("vote_subject", vote_subject)
	print("amount of votes for", len(for_states_indexes))
	print("amount of votes against", len(against_states_indexes))
	print("amount of votes avoided", len(avoided_states_indexes))
	print("first country for", for_states_indexes[0] if len(for_states_indexes) > 0 else None)
	print("last country against", against_states_indexes[-1] if len(against_states_indexes) > 0 else None)
