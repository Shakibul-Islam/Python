unique_number  = {5, 1, 1, 2, 4,  6, 3, 5, 2}
print(unique_number)  # {1, 2, 3, 4, 5, 6}

unique_number.add(7)
print(unique_number)  # {1, 2, 3, 4, 5, 6, 7}

unique_number.remove(3)
print(unique_number)  # {1, 2, 4, 5, 6, 7}

print(len(unique_number))  # 6
for num in unique_number:
    print(num)

