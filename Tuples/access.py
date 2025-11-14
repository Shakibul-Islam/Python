a = (1, 2, 3, 10, 4, 5)
print("first element:", a[0])  # Accessing first element
print("last element:", a[-1])  # Accessing last element

print("elements from index 1 to 3:", a[1:4])  # Slicing from index 1 to 3

print("elements from start to index 2:", a[:3])  # 
print("elements from index 2 to end:", a[2:])  # 
print("entire tuple:", a[:])  # Accessing the entire tuple
# Iterating through the tuple
for element in a:
    print("element:", element)
# Checking membership
print("Is 3 in tuple?", 3 in a)

# Tuple unpacking
w, x, y, z, p, q = a   
print("Unpacked values:", w, x, y, z, p, q)
# Using built-in functions
print("Length of tuple:", len(a))
print("Minimum value in tuple:", min(a))
print("Maximum value in tuple:", max(a))
print("Count of 2 in tuple:", a.count(2))
print("Index of 4 in tuple:", a.index(4))
# Note: Tuples do not have a sort() method since they are immutable 
# but we can sort a tuple by converting it to a list first
sorted_a = sorted(a)    
print("Sorted tuple elements:", sorted_a)