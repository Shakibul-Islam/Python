import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr+5)  # Output: [15 25 35 45 55]
print(arr-5)  # Output: [ 5 15 25 35 45]
print(arr*2)  # Output: [ 20  40  60  80 100]
print(arr/2)  # Output: [ 5. 10. 15. 20. 25.]
print(arr**2) # Output: [ 100  400  900 1600 2500]
print(np.sqrt(arr))  # Output: [3.16227766 4.47213595 5.47722558 6.32455532 7.07106781]
print(np.sin(arr))   # Output: [-0.54402111  0.91294525 -0.98803162  0.74511316 -0.26237485]
print(np.log(arr))   # Output: [2.30258509 2.99573227 3.40119738 3.68887945 3.91202301]
print(np.exp(arr))   # Output: [2.20264658e+04 4.85165195e+08 1.06864746e+13 2.35385267e+17 5.18470553e+21]
print(np.sum(arr))   # Output: 150
print(np.mean(arr))  # Output: 30.0
print(np.std(arr))   # Output: 14.142135623730951 std = sqrt(mean((x - mean(x))**2)) std = standard deviation

print(np.min(arr))  # Output: 10
print(np.max(arr)) # Output: 50

print(np.var(arr))  # Output: 200.0 Variance = mean((x - mean(x))**2)


