str = "Python is great"
print(str.startswith("P")) # Output: True #checks if string starts with 'P'

print(str.endswith("t")) # Output: True #checks if string ends with 't'
print(str.startswith("is", 7)) # Output: True #checks if substring starting at index 7 starts with 'is'
print(str.endswith("is", 0, 7)) # Output: True #checks if substring from index 0 to 7 ends with 'is'

print(str.isalpha()) # Output: False #checks if all characters are alphabetic
print("Python".isalpha()) # Output: True #checks if all characters are alphabetic