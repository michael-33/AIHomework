def first_question(user_id: str, first_name: str, last_name: str, height: float, year_of_birth: int):
	print("first_question")

	print(
		f"#id: {user_id} name: {last_name:<8} , {first_name:<8} height: {height:<6} year-of-birth: {year_of_birth:<4}")


# user input
first_question("1", "Yosi", "Aaron", 160.56, 1990)
first_question("1", "Shimon", "Tzur", 170.76, 1998)
first_question("1", "Hen", "Shmueli", 190.96, 1999)


def second_question(grade: int):
	print("second_question, input =", grade)

	if 0 <= grade <= 40:
		print("try harder next time...")
	elif 40 < grade <= 60:
		print("you're getting there, need some more work")
	elif 60 < grade <= 80:
		print("pretty good")
	elif 80 < grade <= 95:
		print("!awesome")
	elif 95 < grade <= 100:
		print("excellent!!! You're a Star!")
	else:
		print("grade illegal")

	match grade:
		case _ if 0 <= grade <= 40:
			print("try harder next time...")
		case _ if 40 < grade <= 60:
			print("you're getting there, need some more work")
		case _ if 60 < grade <= 80:
			print("pretty good")
		case _ if 80 < grade <= 95:
			print("awesome!")
		case _ if 95 < grade <= 100:
			print("excellent!!! You're a Star!")
		case _:
			print("grade illegal")


# user input
second_question(70)
second_question(700)


def third_question(volume: int):
	print("third_question, input =", volume)

	match volume:
		case 0:
			print("mute")
		case 1 | 2:
			print("very quiet")
		case 3:
			print("quiet")
		case 4:
			print("moderately quiet")
		case 5:
			print("medium")
		case 6:
			print("moderately loud")
		case 7:
			print("loud")
		case 8:
			print("very loud")
		case 9 | 10:
			print("extremely loud")
		case _:
			print("volume illegal")


# user input
third_question(1)
third_question(2)
third_question(9)
