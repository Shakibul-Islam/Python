# str = "Python is great"
# print(str.startswith("P")) # Output: True #checks if string starts with 'P'

# print(str.endswith("t")) # Output: True #checks if string ends with 't'
# print(str.startswith("is", 7)) # Output: True #checks if substring starting at index 7 starts with 'is'
# print(str.endswith("is", 0, 7)) # Output: True #checks if substring from index 0 to 7 ends with 'is'

# print(str.isalpha()) # Output: False #checks if all characters are alphabetic
# print("Python".isalpha()) # Output: True #checks if all characters are alphabetic

str1 = "12345"
print(str1.isdigit())  # Output: True #checks if all characters are digits
print("123a45".isdigit())  # Output: False #checks if all characters are digits

str2 = "abs123"
print(str2.isalnum())