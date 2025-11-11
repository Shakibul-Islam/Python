list_1 = [1, 2, 3]
list_2 = list_1  # Alias assignment

list_2.append(4)
list_2[1] = 2000
print("List 1:", list_1)
print("List 2:", list_2) # Both lists reflect the changes since they reference the same object

