# my_dectionary = {
#     'Fruits': ['Apple', 'Banana', 'Orange'],
#     'Vegetables': ('Carrot', 'Broccoli', 'Spinach'),
#     'Dairy': {'Milk': 2, 'Cheese': 1, 'Yogurt': 3} #List, Tuple, Dictionary
# }
# print(my_dectionary)

# my_dectionary['Price'] = 100.5
# print(my_dectionary)

my_dict= {
    'name': 'python',
    'version': 3.10,
}

print(my_dict)
my_dict['version'] = 3.111 # if key already exists(same), it will update the value else it will create a new key-value pair
print(my_dict)

my_dict['creator'] = 'Guido van Rossum' # new key-value pair
print(my_dict)