profile = {
    'name': 'Alice',
    'age': 30,  
    'salary': 70000
}
# # Using pop() method to remove a key-value pair
# removed_salary = profile.pop('salary', 'Not Found')
# print(f"Removed Salary: {removed_salary}")
# print(f"Updated Profile: {profile}")

# pop item 
pop_item = profile.popitem()
print(f"Popped Item: {pop_item}")
print(f"Updated Profile after pop_item: {profile}")