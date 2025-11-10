# my_list = list((1,2,3,4, "Shakibul", 5.6, True))
# print(my_list)
# print(type(my_list))
# print(my_list[5])

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f'Before updating: {lst}')
lst[2] = "Shakibul" #updating value at index 2
print(f'After updating: {lst}')

#Updating multiple values
lst[5:8] = [600, 700, 'Rakibul']
print(f'After updating multiple values: {lst}')



