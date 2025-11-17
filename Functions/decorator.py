"""
main function > function add 
without changing the main function code.

Decorator is also a function like as a nasted function
"""

def my_decorator(func):
    def wrapper():  # inner function
        print("Something is happening before the function called")
        func()
        print("Something is happening after the function called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# say_hello = my_decorator(say_hello)


import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function called")
        result = func(*args, **kwargs)   # মূল ফাংশনকে আর্গুমেন্ট পাঠানো ও রিটার্ন ধরে রাখা
        print("Something is happening after the function called")
        return result
    return wrapper

@my_decorator1
def say_hello1(name):
    print(f"Hello, {name}!")

say_hello1("Shakibul")




# প্রোগ্রাম লোড হয়; my_decorator ডিফাইন হয়।

# say_hello ডিফাইন করা হয়; এরপর @my_decorator এর কারণে Python চালায়: say_hello = my_decorator(say_hello)। এখন say_hello নামটায় wrapper ফাংশন স্টোর থাকে।

# তুমি say_hello() কল করলে আসলে wrapper() রান হয়।


# output
# Something is happening before the function called
# Hello
# Something is happening after the function called
