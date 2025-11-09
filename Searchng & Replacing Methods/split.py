str = "a,b,c,d,e"
print(str.split(","))  # Output: ['a', 'b', 'c', 'd', 'e'] #output as list
print(str.split(",", 2))  # Output: ['a', 'b', 'c,d,e'] #split at most 2 times

print(str.rsplit(",", 2))  # Output: ['a,b,c', 'd', 'e'] #split at most 2 times from right
print(str.splitlines())  # Output: ['a,b,c,d,e'] #no line breaks, so entire string as single element