import numpy as n

one_array = n.ones(5)
print("One Array:", one_array)
ones_array = n.ones((2,3))
print("Ones Array:", ones_array)
print("Ones Array Shape:", ones_array.shape)

print("Ones Array Data Type:", ones_array.dtype)
print("Ones Array Size (in bytes):", ones_array.nbytes)
print("Ones Array Number of Dimensions:", ones_array.ndim)

print("Ones Array - First Element:", ones_array[0])

print("Ones Array - Elements from Index 1 to 3:", ones_array[1:4])

print("Ones Array - Every Second Element:", ones_array[::2])