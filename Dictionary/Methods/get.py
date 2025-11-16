profile = {
    'name': 'Alice',
    'age': 30,  
    'salary': 70000
}

# Using get() method to retrieve values 
name = profile.get('name')
age = profile.get('age')
salary = profile.get('salary')

print(f"Name: {name}, Age: {age}, Salary: {salary}")

# Attempting to get a non-existing key
department = profile.get('department', 'Not Available or found')
print(f"Department: {department}")