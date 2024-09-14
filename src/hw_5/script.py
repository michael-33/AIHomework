def first_question(movie_length: int):
	hours = movie_length // 60
	minutes = movie_length % 60
	print(f"hours: {hours}, minutes: {minutes}")


def second_question():
	for i in range(0, 11):
		print(i, end=" ")
	print()
	for i in range(40, 89, 2):
		print(i, end=" ")
	print()
	for i in range(77, 106, 7):
		print(i, end=" ")
	print()
	for i in range(99, 65, -3):
		print(i, end=" ")
	print()


def third_question_one():
	user_message = "enter your height between 0.4 to 2.5"
	height = float(input(user_message))
	while height < 0.4 or height > 2.5:
		print("wrong input")
		height = float(input(user_message))


def third_question_two(first_number: int, second_number: int):
	skip = 1 if first_number < second_number else -1
	for i in range(first_number, second_number + skip, skip):
		print(i, end=" ")
	print()


def third_question_three():
	num_of_trials = 3
	while num_of_trials > 0:
		user_input = float(input("How much is pi"))
		if user_input == 3.14:
			print("You are3 correct")
			break
		elif num_of_trials == 1:
			print("pi is 3.14")
			num_of_trials -= 1
		else:
			print("Try again")
			num_of_trials -= 1


def third_question_four():
	is_conditions_met = False
	while not is_conditions_met:
		first_number = int(input("enter first number"))
		second_number = int(input("enter second number"))
		third_number = int(input("enter third number"))
		if 0 <= first_number <= 10 <= second_number <= 60 <= third_number <= 100 and (
				first_number + third_number) / 2 == second_number:
			print("Success!")
			is_conditions_met = True
		else:
			print("Try again")


def third_question_five():
	amount_of_beers = 10
	while amount_of_beers > 0:
		age = int(input("How old are you"))
		if age < 18:
			print("come back later")
		else:
			amount_of_beers -= 1
			print(f"Take your beer, {amount_of_beers} beers left")

# first_question(70)
# first_question(160)
# second_question()
# third_question_one()
# third_question_two(5, -7)
# third_question_three()
# third_question_four()
# third_question_five()
