squre_list = []
for i in range(1,12):
    squre_list.append(i**2)
print("List of squares from 1 to 11:", squre_list)

# List comprehension to create the same list of squares
squre_comp = [i**2 for i in range(1, 12) if i%2 == 0] 
print("List of squares using list comprehension:", squre_comp)

print("1 t0 21 odd number:", [i for i in range(1, 22, 2)])  # odd numbers from 1 to 21

print("2 to 22 even number:", [j for j in range(2, 22, 2) ]) # even numbers from 2 to 22

