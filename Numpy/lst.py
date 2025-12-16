temperature = [22.5, 23.0, 21.8, 22.1, 23.3]

total_temp = sum(temperature)
print("Total Temperature:", total_temp)


total = 0
for temp in temperature:
    total += temp
print("Total Temperature using loop:", total)
