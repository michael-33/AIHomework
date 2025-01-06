def q1(num):
	print(num - 10 if num > 10 else num * 10)


def q2(n1, n2, n3):
	total = n1 + n2 + n3
	print(total if total > 100 else "sum is less than 100")


def q4(age):
	print(age if 0 < age < 120 else "invalid age")


def q5(num):
	print((num // 10) % 10)


def q6(n):
	for i in range(n, 0, -1):
		print(i, end=" ")


def q7(a, b):
	start = min(a, b)
	end = max(a, b)
	start += (start % 2)
	for i in range(start, end + 1, 2):
		print(i, end=" ")


def q8(n):
	for i in range(1, n + 1):
		if i % 3 == 0 or i % 5 == 0:
			print(i, end=" ")


def q9(n):
	for i in range(7, n + 1, 7):
		print(i, end=" ")


def q11():
	total = 0
	while True:
		n = int(input("enter number:"))
		if n == 0:
			break
		if n < 0:
			total += n
	print(total)


def q12():
	nums = [int(input("enter number:")) for _ in range(10)]
	for i in reversed(nums):
		print(i, end=" ")


def q13():
	def is_prime(n):
		if n < 2:
			return False
		for i in range(2, int(n ** 0.5) + 1):
			if n % i == 0:
				return False
		return True

	count = 0
	while True:
		num = int(input("enter number:"))
		if num == 0:
			break
		if is_prime(num):
			count += 1
	print(count)


def q14():
	nums = [int(input("enter number:")) for _ in range(5)]
	avg = sum(nums) / 5
	above = sum(1 for x in nums if x > avg)
	print(f"average: {avg}, numbers above average: {above}")


def q15(a, b):
	count = 0
	while a >= b:
		a -= b
		count += 1
	print(count)


def q16(num):
	sum_digits = 0
	for digit in str(num):
		sum_digits += int(digit)
	print("divisible by 3" if sum_digits % 3 == 0 else "not divisible by 3")


def q17(text):
	print("palindrome" if text == text[::-1] else "not palindrome")
