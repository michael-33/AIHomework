def q_1():
	for i in range(12, 25):
		print(i, end=" ")


def q_2():
	for i in range(7, 32, 2):
		print(i, end=" ")


def q_3():
	for i in range(10, 21, 2):
		print(i, end=" ")


def q_4():
	for i in range(1, 46):
		if i % 3 == 0:
			if i % 5 == 0:
				print("FizzBuzz", end=" ")
			else:
				print("Fizz", end=" ")
		elif i % 5 == 0:
			print("Buzz", end=" ")


def q_5(arr: list[int]):
	arr_sum: int = 0
	for num in arr:
		arr_sum += num
	print("arr_sum", arr_sum)


students_mock = [{
	"id": 1,
	"first_name": "John",
	"last_name": "Doe",
	"age": 20,
	"country": "USA",
	"city": "New York"
},
	{
		"id": 2,
		"first_name": "John2",
		"last_name": "Doe2",
		"age": 30,
		"country": "USA",
		"city": "Minnesota"
	}
]


def q_6_1(students: list[dict], student_property: str):
	for student in students:
		if student_property in student:
			del student[student_property]
	print("students", students)


def q_6_2(students: list[dict]):
	for student in students:
		for key, value in student.items():
			print(f"{key}: {value}")


def q_6_3(students: list[dict]):
	sorted_students = sorted(students, key=lambda student: student["age"], reverse=True)
	print("sorted_students", sorted_students)
	return sorted_students


our_pets = [
	{
		"animal_type": "cat",
		"names": [
			"Meowzer",
			"Fluffy",
			"Kit-Cat"
		]
	},
	{
		"animal_type": "dog",
		"names": [
			"Spot",
			"Bowser",
			"Frankie"
		]
	}
]


def q_7_1(animal_names_arr: list[dict]):
	for animal_names in animal_names_arr:
		if animal_names['animal_type'] == "cat":
			print(animal_names)


def q_7_2(animal_names_arr: list[dict], animal_type: str):
	for animal_names in animal_names_arr:
		if animal_names['animal_type'] == animal_type:
			print(animal_names['names'])


def q_7_3(animal_names_arr: list[dict], animal_name: str):
	for animal_names in animal_names_arr:
		if animal_name not in animal_names['names']:
			animal_names['names'].append(animal_name)
	print("animal_names_arr", animal_names_arr)


student_mock = {
	'name': 'John',
	'age': 20,
	'hobbies': ['reading', 'games', 'coding'],
}


def q_8_1(student: dict):
	for key, value in student.items():
		print(f"{key}: {value}")


def q_8_2(student: dict, hobby: str):
	if hobby not in student['hobbies']:
		student['hobbies'].append(hobby)
	return student


def q_8_3(student: dict, hobby: str):
	new_student = q_8_2(student, hobby)
	q_8_1(new_student)


def q_8_4(student: dict, hobby: str):
	if hobby in student['hobbies']:
		student['hobbies'].remove(hobby)
	return student


def q_8_5(student: dict, hobby: str):
	new_student = q_8_4(student, hobby)
	q_8_1(new_student)


def q_8_6(student: dict):
	student["family_name"] = "Alex"
	print("student", student)


matrix_mock = [
	[1, 2],
	[3, 4],
	[5, 6]
]

matrix_mock_2 = [
	[0, 1, 1],
	[0, 1, 0],
	[1, 0, 0]
]


def q_9(matrix):
	for row in matrix:
		for element in row:
			print(element, end=" ")
	print()


def q_10(matrix):
	count = 0
	for row in matrix:
		for element in row:
			if element == 0:
				count += 1
	print("count", count)


arr_mock = [4, 2, 34, 4, 1, 12, 1, 4]


def q_11(arr):
	arr.sort()
	duplicates = []

	for i in range(len(arr) - 1):
		if arr[i] == arr[i + 1] and arr[i] not in duplicates:
			duplicates.append(arr[i])

	print("duplicates", duplicates)


def q_12(arr):
	reversed_arr = []
	for i in range(len(arr) - 1, -1, -1):
		reversed_arr.append(arr[i])
	print("reversed_arr", reversed_arr)


def q_13(first_array, second_array):
	result = []
	for i in range(len(first_array)):
		result.append(first_array[i] + second_array[i])
	print("result", result)


def q_14(string):
	is_palindrome = string == string[::-1]
	print("is_palindrome", is_palindrome)


def q_15():
	counter = 1
	while counter < 100:
		print(counter)
		counter *= 2


def q_16():
	counter = 900000
	while counter > 50:
		print(counter)
		counter /= 2


def q_17(strings):
	duplicate_strings = []
	seen = []
	i = 0
	while i < len(strings):
		current = strings[i]
		if current in seen and current not in duplicate_strings:
			duplicate_strings.append(current)
		else:
			seen.append(current)
		i += 1
	print("duplicate_strings", duplicate_strings)


def q_18(strings):
	unique_strings = []
	i = 0

	while i < len(strings):
		if strings[i] not in unique_strings:
			unique_strings.append(strings[i])
		i += 1
	print("unique_strings", unique_strings)


def q_19(strings):
	unique_strings = []
	i = 0

	while i < len(strings):
		current = strings[i]
		if current != "Pete" and current not in unique_strings:
			unique_strings.append(current)
		i += 1
	print("unique_strings", unique_strings)


def q_20(array):
	i = 0
	while i < len(array) - 1:
		if array[i] == array[i + 1]:
			return i + 1
		i += 1
	return -1


def q_21():
	while True:
		full_name = input("Enter your full name")
		name_parts = full_name.split()
		if len(name_parts) == 2 and name_parts[0].isalpha() and name_parts[1].isalpha():
			break
		print("Invalid input. Please enter your full name with first and last name (only alphabetic characters).")

	while True:
		age = input("Enter your age (1-130)")
		if age.isdigit() and 1 <= int(age) <= 130:
			age = int(age)
			break
		print("Invalid input. Please enter a valid age between 1 and 130.")

	while True:
		email = input("Enter your email (must contain '@')")
		if "@" in email:
			break
		print("Invalid input. Please enter a valid email address.")

	print("full_name", full_name)
	print("age", age)
	print("email", email)
