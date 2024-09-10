def first_question(amount_of_slices: int, amount_of_friends: int = 4):
	slices_per_friend = amount_of_slices // amount_of_friends
	slices_left = amount_of_slices % amount_of_friends
	print(f"slices_per_friend={slices_per_friend}, slices_left={slices_left}")


first_question(3)
first_question(8)
first_question(9, 2)

# second question

print("second question - True")

a = 0
b = 0
if a == b:
	print(f"was True for {a} {b}")
else:
	print(f"was False for {a} {b}")

a = 1
b = 1
c = 1
d = 1
if a + b and c + d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a >= b or c > d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a >= b or c < d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a == b and c <= d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 1
b = 0
c = 0
d = 0
if True and a + b + c + d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 1
b = 0
if a != b:
	print(f"was True for {a} {b}")
else:
	print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or True:
	print(f"was True for {a} {b} {c}")
else:
	print(f"was False for {a} {b} {c}")

a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or False:
	print(f"was True for {a} {b} {c}")
else:
	print(f"was False for {a} {b} {c}")

a = 0
b = 1
c = 3
d = 2
if a % b == 0 and c % d == 1:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

print("second question - False")

# MAKE ALL OF THIS CONDITION FALSE

a = 1
b = 0
if a == b:
	print(f"was True for {a} {b}")
else:
	print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
d = 0
if a + b and c + d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 1
c = 0
d = 0
if a >= b or c > d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 1
c = 0
d = 0
if a >= b or c < d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 3
d = 0
if a == b and c <= d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
if a != b:
	print(f"was True for {a} {b}")
else:
	print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or True:
	print(f"was True for {a} {b} {c}")
else:
	print(f"was False for {a} {b} {c}")

a = 1
b = 0
c = 0
if a != b and a <= c or a <= b or False:
	print(f"was True for {a} {b} {c}")
else:
	print(f"was False for {a} {b} {c}")

a = 1
b = 5
c = 0
d = 0
if a % b == 0 and c % d == 1:
	print(f"was True for {a} {b} {c} {d}")
else:
	print(f"was False for {a} {b} {c} {d}")

# third_question

# 4<9 True
# (2*3+4)*(7+7) True
# 18+18 True
# 10 == 10 True
# 10 == 10 and 20 == 30 False
# 10 == 10 or 20 == 30 True
# 20 == 30 or 10 == 10 True
# not 3 False
# 3 True
# (33>20) and (2<12) and 10 True
#
# if True and True: True
# if True and False: True
# if True or False: True
# if False or True: True
# if (not 10) and (10): False
# if (not 10) and (not 10): False
# if 5 != 5 and 5 == 5: False
# if 2 == 2 or 3 == 3: True
# if 2 == 2 and 3 == 3: True
# if 40 == 30 and 1 >= 4: False
# if 13 >= 3 or 47 >= 5: True

# forth question

for i in range(10, 21):
	print(i)

for i in range(10, 21, 2):
	print(i)


def set_skip_amount(skip_amount: int):
	for number in range(10, 21, skip_amount):
		print(number)


set_skip_amount(3)
