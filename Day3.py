# This is all about Lists and Dictionaries.

mycart = [1299, 312, 32, 43]

print(sum(mycart))

mycart.append(6758)

print(mycart)

print(len(mycart))

# Position of all elements in the list never change until and unless it is forced to do that.

print(mycart[3])

mystring = "Hello World"

print(mystring[5])

print(len(mystring))

my_list = [mystring, mycart]

print(my_list)

my_data = {"name" : "Justin Mitchel", "location" : "California"}

print(my_data.keys())

print(list(my_data.keys()))

print(list(my_data.keys())[0])

my_data['occ'] = ['Coder']

print(my_data)