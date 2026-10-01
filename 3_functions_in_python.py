
#* User Defined Functions in Python
#UDF stands for User Defined Function in Python
#Important: User defined functions allow you to encapsulate code for reuse and better organization
# They help in making the code more readable and maintainable
#Code Modularity: Functions help in breaking down the code into smaller, manageable, and reusable modules
#Example: The functions defined below demonstrate various common tasks such as greeting, calculating square, factorial, prime check, and finding maximum and minimum of two numbers.


#define a function to greet a person by name
def greet(name):
    return f"Hello, {name}!"

#function call example
print(greet("Alice")) #output: Hello, Alice!

#another function to calculate the square of a number
def square(number):
    return number ** 2

#function call example
print(square(4)) #output: 16

#another function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#function call example
print(factorial(5)) #output: 120

#another function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#function call example
print(is_prime(7)) #output: True

#another function to find the maximum of two numbers
def max_of_two(a, b):
    return a if a > b else b

#function call example
print(max_of_two(10, 20)) #output: 20

#another function to find the minimum of two numbers
def min_of_two(a, b):
    return a if a < b else b

#function call example
print(min_of_two(10, 20)) #output: 10


print("==========================================="*2) 


#* Types of Functions in Python
#1. Built-in Functions: Functions that are provided by Python itself, such as print(), len(), type(), etc.
#2. Python Library Functions: Functions that are provided by Python's standard library, such as math.sqrt(), os.listdir(), datetime.datetime.now(), etc.
#3. Python Community Functions: Functions that are created and shared by the Python community, often available through third-party libraries and packages.
#4. User Defined Functions: Functions that are defined by the user to perform specific tasks, as demonstrated above.
#5. Anonymous Functions (Lambda Functions): Functions that are defined without a name using the lambda keyword. They are typically used for short, simple operations.


#* Function Shape: Describes the general structure and components of a function in Python.
# A typical function in Python consists of the following parts:
#1. Function Definition: Begins with the def keyword, followed by the function name and parentheses ().
#2. Parameters (Optional): Variables listed inside the parentheses that the function can accept as input.
#3. Docstring (Optional): A string literal that describes the purpose and behavior of the function.
#4. Function Body: The block of code that performs the task defined by the function.
#5. Return Statement (Optional): Specifies the value to be returned by the function. If omitted, the function returns None.

# Arguments: The values passed to the function's parameters when calling the function. They provide input data for the function to work with.
# Return Value: The value that a function returns to the caller using the return statement. If no return statement is provided, the function returns None by default.
# Function Call: The act of invoking a function by using its name followed by parentheses, optionally passing arguments inside the parentheses.


#* *args and **kwargs: Special syntax in Python functions to handle variable numbers of arguments.
# *args allows a function to accept any number of positional arguments as a tuple.
# **kwargs allows a function to accept any number of keyword arguments as a dictionary.

# Example usage of *args
def total(*args):
    return sum(args)

# Can give any number of positional arguments to the total function using *args
print(total(1, 2)) #output: 3
print(total(1, 2, 3, 4, 5)) #output: 15
print(total(10, 20, 30)) #output: 60


# Example usage of **kwargs
def create_user(**kwargs):
    print(kwargs)

# Can give any number of keyword arguments to the create_user function using **kwargs
create_user(name="Alice", age=25, city="New York")
create_user(name="Bob", profession="Engineer")



print("==========================================="*2) #output: ===========================================...

#* Return Statement
# The return statement is used to send a value back to the caller from a function. If no return statement is provided, the function returns None by default.

# Example usage of return statement
def add(a, b):
    return a + b

result = add(5, 3)
print(result) #output: 8


#Check whether an email is valid using a function
def is_valid_email(email):
    return "@" in email and "." in email

# Example usage of is_valid_email function
print(is_valid_email("test@example.com")) #output: True
print(is_valid_email("invalid.email")) #output: False



#* Best practices in Python coding
# Docstring: Always include a docstring in your functions to describe their purpose and usage. 
# Use Type Hints: Include type hints for function parameters and return values to improve code clarity and help with static analysis.
# Comments: Use comments to explain the purpose and logic of your code, but avoid over-commenting obvious code.
# Meaningful Names: Use descriptive names for functions and parameters to improve code readability.
# Keep Functions Small: Each function should perform a single task or responsibility.
# Avoid Side Effects: Functions should avoid modifying global variables or external states unless necessary.
# Use Default Arguments: Provide default values for parameters when appropriate to make functions more flexible.
# Consistent Style: Follow PEP 8 guidelines for naming conventions, indentation, and code layout.
# Naming Conventions: Follow PEP 8 guidelines for naming functions, variables, and classes. 
# Use lowercase with underscores for function and variable names, and use CamelCase for class names.
# Avoid Deep Nesting: Keep the code structure simple and avoid excessive nesting of loops and conditionals.
# Avoid Global Variables: Minimize the use of global variables to reduce dependencies and potential side effects.
# Test Your Functions: Always write tests for your functions to ensure they work as expected and to catch potential bugs early.
# Other Best Practices: Continuously review and refactor your code to improve readability, maintainability, and performance.



#Example of using type hints and docstring in a function
def add(a: int, b: int):
    """
    Function that returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(add(5, 3)) #output: 8


#Getting docstring of the add function
print(add.__doc__)

