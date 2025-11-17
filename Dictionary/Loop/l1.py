profile = {
    'name': "Shakibul",
    'age': 24,
    'salary': 50000
}
for keys in profile:
    print(keys)

for k in profile:
    print(k)        # prints keys

for k in profile.keys():
    print(k)        # prints keys

for k in profile.values():
    print(k)        # prints values


# Both Keys and Values
for k in profile.items():
    print(k)