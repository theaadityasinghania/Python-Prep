# Iterations and Loops

# mylist = [1,2,3,4,5,6,7,8,9,0]

# for i in range(len(mylist)):
#     print(mylist[i])

# for val in mylist:
#     print(val)

# for i in range(10):
#     print(i)

# for i in range(1,10):
#     print(i)

# for char in "Aaditya Singhania":
#     print(char)

# user1 = {"username":"theaadityasinghania", "id":1}
# user2 = {"username":"missyashisinghania", "id":2}

# my_users = [user1, user2]

# for user in my_users:
#     print(user)

# for user in my_users:
#     print(user["username"])

# for user in my_users:
#     print(user["email"])

# user1 = {"username":"theaadityasinghania", "id":1}
# user2 = {"username":"missyashisinghania", "id":2, "email":"email"}
# my_users = [user1, user2]

# for user in my_users:
#     if 'email' in user:
#         print(user["email"])

user1 = {"username":"theaadityasinghania", "id":1}
user2 = {"username":"missyashisinghania", "id":2, "email":"email"}
my_users = [user1, user2]

# selected_user = {}
# my_user_lookup = 2

# for user in my_users:
#     if 'id' in user:
#         if user['id'] == my_user_lookup:
#             selected_user = user

# print(selected_user)

for i in range(0, 10):
    for user in my_users:
        if user['id'] == i:
            print(user)

# while loop will be coverd with conditionals