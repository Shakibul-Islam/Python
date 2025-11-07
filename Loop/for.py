alist = [2, 3, 4, 5 ,6, 7, 8, 9] #list

for i in alist:
    print(i)

print("-----")
for i in range(1, 21, 3):
    print(i)

print("-----")
for char in "Python Programming":
    print(char)

print("-----")
for key in {'name': 'Alice', 'age': 30, 'city': 'New York'}:
    print(key)

print("-----")
for item in (10, 20, 30, 40, 50):  # tuple
    print(item)

print("-----")
for number in {1, 2, 3, 4, 5, 4, 5}:  # set
    print(number)

print("-----")
for byte in b'Hello':  # bytes
    print(byte)
