text = "phython is fun. I love python programming."

print(text.find("is"))          # Output: 8  # first occurrence of "is"
print(text.find("python"))      # Output: 0
print(text.find("java"))        # Output: -1
print(text.rfind("python"))     # Output: 21
print(text.index("fun"))       # Output: 14 # end of the word "fun"
print(text.rindex("python"))    # Output: 21
# The following line would raise a ValueError since "java" is not found
# print(text.index("java"))