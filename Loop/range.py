a = range(3, 13 , 2)  # start, stop, step

for i in a:
    print(i)

print("Length of range a is:", len(a))

b = list(range(10))  # default start is 0, step is 1
print("List from range b:", b)
for j in b:
    print(j)

print("-----")
c = tuple(range(5, 0, -1)) # counting down
print("Tuple from range c:", c)
print("-----")
for k in c:
    print(k)