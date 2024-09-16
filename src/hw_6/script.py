import random


def first_question(first_player: str, second_player: str, third_player: str, fourth_player: str):
	random_player = random.choice((first_player, second_player, third_player, fourth_player))
	print(random_player)


def second_question():
	random_number = random.randint(1, 100)
	amount_of_guesses = 0
	while True:
		amount_of_guesses += 1
		user_guess = int(input("Guess a number"))
		if user_guess > random_number:
			print("too high")
		elif user_guess < random_number:
			print("too low")
		else:
			print(f"you win, amount of guesses: {amount_of_guesses}")
			break


def two_and_a_half_question():
	def get_valid_temperature():
		temp = random.randint(-100, 100)
		if -50 <= temp <= 45:
			return temp
		return get_valid_temperature()

	temperatures = []
	for i in range(5):
		temperatures.append(get_valid_temperature())

	average_temp = sum(temperatures) / len(temperatures)
	print("average temp", average_temp)

# first_question("1", "2", "3", "4");
# second_question()
# two_and_a_half_question()
