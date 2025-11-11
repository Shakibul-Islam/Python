list_1 = [1, 2, 3, 4, 5]
list__2 = list_1.copy()  # Create a shallow copy of list_1

list__2.append(6)
list__2[2] = 1000

print("list 1:", list_1)   # Original list remains unchanged

print("list 2:", list__2)  # Copied list reflects the changes