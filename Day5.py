# Conditionals and Control flow

# if True:
#     print("Hello World!")

# if False:
#     print("No Hello to anyone.!")

# if not False:
#     print("Wassup?")

# print(True == False)

# var_ = "this"

# True = False

# for = True

# print(10 > 32)

# print(424 < 3423525245)

# print(10 > 32 or 10 < 32)

# print(not 10 > 32)

# print(200 > 200)

# print(200 >= 200)

# print(200 > 200 or 200 == 200)

# abc = [1,2,3,4,5]

# abc_sq = []

# for num in abc:
#     new_number = num ** 2
#     abc_sq.append(new_number)

# print(abc_sq)

# is_even = []
# is_odd = []

# for num in abc_sq:
#     if num %2 == 0:
#         print("Is Even")
#         is_even.append(num)
#     else:
#         print("Is Odd")
#         is_odd.append(num)

# print(is_even)
# print(is_odd)

# is_even = []
# is_odd = []
# is_factor_of_3 = []

# for num in abc_sq:
#     if num % 3 == 0:
#         is_factor_of_3.append(num)
#     elif num % 2 == 0:
#         is_even.append(num)
#     else:
#         is_odd.append(num)

# print(is_factor_of_3, is_even, is_odd)

# Control flow with while loops

# x = 10
# i = 0

# while i < x:
#     print(i)
#     i = i + 1

# x = 10
# i = 0
# z = 12

# while i < x:
#     z = z * 2
#     if z > 342900:
#         break
#     print(z, i)
#     i = i + 0.00001

# x = 10
# i = 0
# while i < x:
#     if i % 2 == 0:
#         print("Even")
#     else:
#         continue
#     i += 1

# x = 10
# i = 0
# while i < x:
#     print(i)
#     if i % 2 == 0:
#         print("Even")
#     else:
#         continue
#     i += 1

x = 10
i = 0
while i < x:
    i += 1
    if i % 2 == 0:
        continue
    print(i)