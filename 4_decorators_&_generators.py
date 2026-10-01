
#* Decorators in Python
# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function.
# A decorator allows you to wrap another function in order to extend its behavior without permanently modifying it.
# Decorators are commonly used for logging, authentication, and other cross-cutting concerns.

# Example of a simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
# Applying the decorator to the base function `say_hello`
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# ---------------------------------------------------------------------------------

#* Timer decorator example

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Time taken:", end_time - start_time)
        return result
    return wrapper


@timer_decorator
def brew_tea():
    #start_time = time.time()
    print("Boiling water...")
    time.sleep(2)
    print("Steeping tea...")
    time.sleep(3)
    print("Tea is ready!")
    #end_time = time.time()
    #print("Time taken:", end_time - start_time)
    return "Tea is ready!"


@timer_decorator
def brew_coffee():
    print("Boiling water...")
    time.sleep(2)
    print("Brewing coffee...")
    time.sleep(2)
    print("Coffee is ready!")
    return "Coffee is ready!"


brew_tea()
brew_coffee()



# ---------------------------------------------------------------------------------

#*Generators in Python

# A generator is a special type of iterator in Python that allows you to iterate over a sequence of values lazily,
    # meaning it generates values on the fly and does not store them in memory.
# Generators are defined using functions and the `yield` statement.

# Example of a simple generator
def my_generator():
    for i in range(5):
        yield i

# Using the generator
for value in my_generator():
    print(value)



# Visualizing the difference in memory usage between list and generator
# List: builds all 10 million numbers in memory
squares_list = [x * x for x in range(10_000_000)]

# Generator: computes one at a time, almost no memory
squares_gen = (x * x for x in range(10_000_000))   # note ( ) not [ ]

print(sum(squares_gen))

