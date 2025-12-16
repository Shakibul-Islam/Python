import numpy as np

#2d array
ar_2d = np.full((2, 3),5)  # Creating a 2D array filled with the value 5
print("2D Array filled with 5:\n", ar_2d)

filled_array = np.full((2, 3, 4), 7)  # Creating a 3D array filled with the value 7
# Here 2 is the number of 2D arrays, 
#3 is the number of rows, and 
# 4 is the number of columns in each 2D array
print("3D Array filled with 7:\n", filled_array)

# Creating a 4D array with shape (2, 2, 3, 4) filled with the value 5
four_d_array = np.full((2, 2, 3, 4), 5)
print("4D Array filled with 5:\n", four_d_array)
# here 2 is the number of 3D arrays, 
# 2 is the number of 2D arrays in each 3D array,
# 3 is the number of rows, and
# 4 is the number of columns in each 2D array