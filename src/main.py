# from hw_04_09.script import first_question

arr = [89, 91, 23, 34, 15, 98, 71, 99, 101]
sorted_arr = sorted(arr, key=lambda i: (i % 10, i))
print("sorted_arr", sorted_arr)
