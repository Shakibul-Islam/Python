# yield keyword
def count_down(num):
    while num > 0 :
        yield num   # yield values one at a time
        num -= 1

# Using the generator
for i in count_down(5):
    print(i)