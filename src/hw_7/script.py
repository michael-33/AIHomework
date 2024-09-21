import random


def first_question():
	amount_of_positive_numbers = 0
	amount_of_negative_numbers = 0
	amount_of_zeros = 0
	amount_of_numbers_divided_in_7 = 0
	last_positive_number = None
	last_negative_number = None
	had_negative_999 = False

	for i in range(10):
		# simulate user input
		random_number = random.randint(-2000, 2000)
		if random_number == -999:
			had_negative_999 = True
			break
		elif -1000 <= random_number <= 1000:
			if random_number % 7 == 0:
				amount_of_numbers_divided_in_7 += 1
			if random_number > 0:
				amount_of_positive_numbers += 1
				last_positive_number = random_number
			elif random_number < 0:
				amount_of_negative_numbers += 1
				last_negative_number = random_number
			else:
				amount_of_zeros += 1
	if not had_negative_999:
		print(f"amount_of_positive_numbers: {amount_of_positive_numbers}")
		print(f"amount_of_negative_numbers: {amount_of_negative_numbers}")
		print(f"amount_of_zeros: {amount_of_zeros}")
		print(f"amount_of_numbers_divided_in_7: {amount_of_numbers_divided_in_7}")
		print(f"last_positive_number: {last_positive_number}")
		print(f"last_negative_number: {last_negative_number}")


def second_question():
	names = ['Alex', 'John', 'Ron', 'Sally', 'Tom', 'Harry', 'Jane']
	good_results = []
	world_record = None
	for i in range(7):
		random_jump_height = round(random.uniform(4, 7), 2)
		if random_jump_height < 5.8:
			continue
		good_results.append(random_jump_height)
		if random_jump_height > 6.23:
			if world_record is None or random_jump_height > world_record["jump_height"]:
				world_record = {"name": names[i], "jump_height": random_jump_height}

	average_score = sum(good_results) / len(good_results)
	print(f"amount of good results: {len(good_results)}")
	print(f"average_score: {average_score}")
	print(f"world_record: {world_record}")

# first_question()
# second_question()
