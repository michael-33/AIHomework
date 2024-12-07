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


q_8_6(student_mock)
