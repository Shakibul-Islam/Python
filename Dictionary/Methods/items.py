profile = {
    'name': 'Alice',
    'age': 30,  
    'salary': 70000
}
keys = profile.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'salary'] )

value = profile.values()
print(list(value))  # Output: dict_values(['Alice', 30, 70000] )

# Both Keys and Values
all_items = profile.items()
print(all_items)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('salary', 70000)])
print(list(all_items))  # Converting to list for better readability

print(profile)  # Dictionary print