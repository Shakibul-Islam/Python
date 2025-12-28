import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1,2], [2,3]], [[3,4], [4,5]], [[5,6], [6,7]]])

print("1D array ndim:", arr_1d.ndim)  # Output: 1
print("2D array ndim:", arr_2d.ndim)  # Output: 2
print("3D array ndim:", arr_3d.ndim)  # Output: 3