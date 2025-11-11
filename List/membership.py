'''
in - Membership Operators
not in - Membership Operators
'''
list_1 = [1, 2, 3, 4, 5]
check = int(input("Enter a number to check its membership in the list: "))

if check in list_1:
    print(f"{check} is present in the list.")
else:
    print(f"{check} is not present in the list.")