a = [1, 2, 3, 4, 5]

a.append(10000)  # Adds 10000 to the end of the list
print("After append:", a)

a.insert(2, 5000) # Inserts 5000 at index 2
print("After insert:", a)

a.remove(3)  # Removes the first occurrence of 3
print("After remove:", a)

popped_element = a.pop()  # Removes and returns the last element
print("After pop:", a)
print("Popped element:", popped_element)

a.sort()  # Sorts the list in ascending order
print("After sort:", a)

a.reverse()  # Reverses the list
print("After reverse:", a)

count_of_4 = a.count(4)  # Counts occurrences of 4
print("Count of 4:", count_of_4)

index_of_5000 = a.index(5000)  # Finds the index of the first occurrence of 5000
print("Index of 5000:", index_of_5000)

# a.clear()  # Clears the list
# print("After clear:", a)

b = [6, 7, 8]
a.extend(b)  # Extends list a by appending elements from list b
print("After extend:", a)

b.extend(a)  # Extends list b by appending elements from list a
print("After extending b with a:", b)

print("Final list a:", a)
print("Final list b:", b)

