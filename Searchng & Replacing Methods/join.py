str = "a,b,c,d,e"
s = str.split(",")
print(s)  # Output: ['a', 'b', 'c', 'd', 'e']

joined_str = "-".join(s)
print(joined_str)  # Output: a-b-c-d-e

joined_str_with_limit = "-".join(s[:3])
print(joined_str_with_limit)  # Output: a-b-c