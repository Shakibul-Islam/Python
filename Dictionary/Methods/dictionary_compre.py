squares = { x: x*x for x in range(1, 11)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# Creating a dictionary with conditional logic
even_squares = { x: x*x for x in range(1,11) if x%2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Creating a dictionary from two lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Creating a dictionary with transformed values
original = {'apple': 1, 'banana': 2, 'cherry': 3}
transformed = {k: v*10 for k, v in original.items()}
print(transformed)  # Output: {'apple': 10, 'banana': 20, 'cherry': 30}