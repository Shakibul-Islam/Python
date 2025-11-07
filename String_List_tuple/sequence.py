#string , list , tuple , range

string_var = "Hello, World!"
# print(string_var[0])  
# print(string_var[7:12]) # World
# print(string_var.lower())
# print(string_var.upper())
# print(string_var.replace("World", "Python"))
print(string_var.split("H,o"))  # ['','ell', ' W', 'rld!']


# list_var = [1, 2, 3, 4, 5]
# print(list_var[0])
# print(list_var[1:4])  # [2, 3, 4]
# list_var.append(6)
# print(list_var)
# list_var.remove(3)
# print(list_var)


# listV1 = ['apple', 'banana', 'cherry']
# listV1[0] = 'blueberry'
# print(listV1)  # ['apple', 'blueberry', 'cherry']

# tuple_var = (10, 20, 30, 40, 50)
# print(tuple_var[1])
# print(tuple_var[2:5])  # (30, 40, 50)
# #tuple_var[0] = 100  # This will raise an error because tuples are immutable
# print(tuple_var.count(20))  # 1
# print(tuple_var.index(30))  # 2


range_var = range(1, 10)
print(range_var[0])
print(range_var[2:5])  # range(3, 6)
for num in range_var:
    print(num)
print(list(range_var))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
