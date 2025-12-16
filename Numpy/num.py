import numpy as np

temperature = np.array([22.5, 23.0, 21.8, 22.1, 23.3])

average = np.mean(temperature)
print("Average Temperature:", average)

total_temp = np.sum(temperature)
print("Total Temperature using NumPy:", total_temp)