# a = 5
# b = 10

# value = a + b
# print("The sum of the numbers is:", value)


#* Data Types in Python
# Python supports various data types, including:
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str 

# print("===============================" * 2) # Output: =============================================================================================


#* Types of Functions in Python
# 1. Built-in Functions: Functions that are available by default in Python, such as print(), len(), type(), etc.
# 2. User-defined Functions: Functions that are defined by the user to perform specific tasks. These functions can be created using the def keyword.
# 3. Lambda Functions: Anonymous functions that can be defined using the lambda keyword. They are often used for short, simple operations.

#* important Built-in Functions in Python
# print(type(5))        # Output: <class 'int'>
# print(len("Hello"))  # Output: 5

#* Method Functions in Python
# Method functions in Python like upper(), lower(), strip(), replace(), split(), join(), find(), count(), etc. 
# are used to manipulate strings and perform various operations on them.
# name = "Dheeraj"
# name1 = name.upper() #output: 'DHEERAJ'
# name2 = name.lower() #output: 'dheeraj'
# name3 = name.strip() #output: 'Dheeraj'
# name4 = name.replace("Dheeraj", "Don") #output: 'Don'
# name5 = name.split(" ") #output: ['Dheeraj']
# name6 = name.find("D") #output: 0
# name7 = name.count("e") #output: 2
# name8 = name.join("Hello") #output: 'HDeheerajlDeheerajoDeheeraj'
# print(name1)
# print(name2)
# print(name3)
# print(name4)
# print(name5)
# print(name6)
# print(name7)
# print(name8)


# password = "Dheeraj"
# print(len(password))
# if len(password) < 8:
#     print("Password must be at least 8 characters long.")


# text = """Python is a high-level language. 
# Python is an interpreted language.
# Python is a popular language.
# Python is a powerful language.
# Python is a beginner-friendly language."""

# print(text.count("Python")) # Output: 5

# print("===============================" * 2) # Output: =============================================================================================


#* Transformations
phone = "123-456-7890"

# Remove the hyphens from the phone number
cleaned_phone = phone.replace("-", "")
print(cleaned_phone)  # Output: 1234567890

first_name = "John" 
last_name = "Doe"
# Concatenate first name and last name to create a full name
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
print(full_name.upper())  # Output: JOHN DOE

print("===============================" * 2) # Output: =============================================================================================


#* F--String Formatting
name = "Alice"
age = 30
# Using f-string formatting to create a formatted string
print(f"My name is {name} and I am {age} years old.") # Output: My name is Alice and I am 30 years old. 

#* Split function used to split a string into a list of substrings based on a specified delimiter.
stamp = "2024-06-15"
print(stamp.split("-")) # Output: ['2024', '06', '15']

csv_file = "name,age,city"
# Split the CSV string into a list of values
values = csv_file.split(",")
print(values)  # Output: ['name', 'age', 'city']

print("===============================" * 2) # Output: =============================================================================================


#* Indexing and Slicing
# Indexing allows you to access individual characters in a string using their position (index).
# Slicing allows you to extract a portion of a string by specifying a range of indices.
name = "Alice"
print(name[0])  # Output: A (first character)
print(name[-1]) # Output: e (last character)
print(name[1:4]) # Output: lic (characters from index 1 to 3)
print(name[:3])  # Output: Ali (first three characters)

mydate = "2024-06-15"
# Extracting the year, month, and day using slicing
print(mydate[:4])   # Output: 2024
print(mydate[5:7]) # Output: 06

#Extracting the date using negative indexing
print(mydate[-2:])  # Output: 15 (last two characters)


print("===============================" * 2) # Output: =============================================================================================

#* String Formatting
# String formatting allows you to create strings with dynamic content by inserting values into placeholders.
name = "Alice"
age = 30
# Using the format() method for string formatting
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old. 

print("===============================" * 2) # Output: =============================================================================================

#* strip functions in Python
# The strip() function is used to remove leading and trailing whitespace characters from a string.
#lstrip() removes leading whitespace, rstrip() removes trailing whitespace, and strip() removes both leading and trailing whitespace.
#rstrip() removes trailing whitespace, and strip() removes both leading and trailing whitespace.
text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"
print(text.lstrip()) # Output: "Hello, World!   "
print(text.rstrip()) # Output: "   Hello, World!"

#Cleanup of a string by removing unwanted characters using strip()
raw_string = "   ***Hello, World!, Python is awesome***   "
# Remove leading and trailing whitespace and asterisks
cleaned_string = raw_string.strip("  *")
print(cleaned_string)  # Output: "Hello, World!, Python is awesome"


print("===============================" * 2) # Output: =============================================================================================


#* Startswith() and endswith() functions in Python
# The startswith() function checks if a string starts with a specified prefix, and the endswith() function checks if a string ends with a specified suffix.
email = "user@gmail.com"
print(email.startswith("user"))  # Output: True
print(email.endswith("@gmail.com"))  # Output: True



print("===============================" * 2) # Output: =============================================================================================

#* Random Module in Python
# The random module in Python provides functions for generating random numbers and performing random operations.
import random

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)  # Output: A random integer between 1 and 10

#random float between 0 and 1
random_float = random.random()
print(random_float)  # Output: A random float between 0 and 1


#* isinstance() function in Python
# The isinstance() function is used to check if an object is an instance of a specified class or a subclass thereof.
# It returns True if the object is an instance of the class, and False

isinstance_result = isinstance(5, int)
print(isinstance_result)  # Output: True

isinstance_result2 = isinstance("Hello", int)
print(isinstance_result2)  # Output: False

#* is_integer() function in Python
# The is_integer() function is used to check if a float value is an integer (i.e., has no decimal part). 
# It returns True if the float is an integer, and False otherwise
is_integer_result = (5.0).is_integer()
print(is_integer_result)  # Output: True

is_integer_result2 = (5.5).is_integer()
print(is_integer_result2)  # Output: False


print("===============================" * 2) # Output: =============================================================================================

#* Comparison Operators in Python
# Comparison operators are used to compare values and return a boolean result (True or False).
# Examples of comparison operators:
print(10 == 10) # Output: True
print(10 != 5)  # Output: True
print(10 > 5)   # Output: True
print(10 < 5)   # Output: False



print("===============================" * 2) # Output: =============================================================================================

#* Conditional Statements in Python
# Conditional statements allow you to execute different blocks of code based on certain conditions.

#Example of an if statement:
number = 10
if number > 0:
    print("The number is positive.")  # Output: The number is positive. 


#Example of an if-else statement:
number = -5
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")  # Output: The number is negative.


#Example of an if-elif-else statement:
number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")  # Output: The number is zero. 


#Example of nested if statements:
number = 15
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")  # Output: The number is positive and odd. 

#Example of a simple password validation using if statements:
password = "Dheeraj"
if len(password) < 8:
    print("Password must be at least 8 characters long.")  

#Example of in-line if statement (ternary operator):
age = 17
message = "You are an adult." if age >= 18 else "You are a minor."
print(message)  # Output: You are a minor.


print("===============================" * 2) # Output: =============================================================================================


#* Loops in Python
#For Loop in Python
# Loops allow you to execute a block of code repeatedly based on a condition.
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4 (each number on a new line)


#While Loop in Python
# A while loop continues to execute a block of code as long as a specified condition is true
count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4 (each number on a new line)
    count += 1


print("===============================" * 2) # Output: =============================================================================================

#*for-loop real world example

scores = [85, 90, 78, 92, 88] 
total_score = 0
for score in scores:
   total_score += score
   print(f"Current Score: {score}")

print(f"Total Score: {total_score}")


#for-loop example for processing file names
files = ["data.csv ", " company_data.txt", "file3.txt "]
for file in files:
    file = file.strip().lower().replace("txt", "csv") # Remove leading/trailing whitespace and convert to lowercase
    print(f"Processed File: {file}")


#for-loop usage for printing 7*1=7 complete multiplication table
number = 7
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

#for-loop for printing left aligned star pattern
for i in range(1,10):
    print("*" * i)


print("===============================" * 2) # Output: =============================================================================================


#* match-case statement in Python
# The match-case statement is a control flow structure that allows you to match a value against multiple patterns and execute different blocks of code based on the matched pattern.
# It is similar to a switch statement in other programming languages. The match-case statement was introduced in Python 3.10.
#Example of a match-case statement:
day = "Monday"
match day:
    case "Monday":
        print("It's the start of the work week.")  # Output: It's the start of the work week.
    case "Friday":
        print("It's the end of the work week.")
    case _:
        print("It's a regular day.")

print("===============================" * 2) # Output: =============================================================================================

#* Break, Continue and Pass Statements in Python
# The break statement is used to exit a loop prematurely. 
# While the continue statement is used to skip the current iteration and move to the next iteration of the loop.
# The pass statement is a null operation; it does nothing when executed. It is often used as a placeholder in situations where a statement is syntactically required but no action is needed.


#* Break Statement Example
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Output: 0, 1, 2, 3, 4 (each number on a new line)


#Break Statement Example with if-loop
Names = ["Alice", "Bob", "Charlie", "", "Eve"]
for name in Names:
    if name == "":
        print("Empty name field found, stopping the loop.")
        break
    print(name)

#*Continue Statement Example
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Output: 1, 3, 5, 7, 9 (each number on a new line)   


#Continue Statement Example with if-loop
Names = ["Alice", "Bob", "Charlie", "", "Eve"]
for name in Names:
    if name == "":
        print("Empty name field found! Skipping this entry.")
        continue  # Skip the empty name field
    print(name)

#* Pass Statement Example
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    print(i)  # Output: 0, 1, 2, 3, 4 (each number on a new line)


# Skip weekends in a loop using continue
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekends = ["Saturday", "Sunday"]

for day in days:
    if day in weekends:
        continue  # Skip weekends
    print(f'Workday:{day}')  # Output: Monday, Tuesday, Wednesday, Thursday, Friday (each day on a new line)


#Check whether any filename appears more than once in a list of filenames using break
filenames = ["file1.txt", "file2.txt", "file3.txt", "file2.txt", "file4.txt"]
seen = set()
duplicates = set()

for filename in filenames:
    if filename in seen:
        duplicates.add(filename)
    else:
        seen.add(filename)

print(duplicates)  # {'file2.txt'}


print("===============================" * 2) # Output: =============================================================================================

#* Shallow Copy and Deep Copy
#A shallow copy creates a new object but does not create copies of nested objects; it only copies references to them.
#A deep copy creates a new object and recursively copies all nested objects.

import copy

original_list = [[1, 2, 3, 4, 5, 6]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)

# Modify the original list
original_list[0] = [100, 2, 3, 4, 5, 6]

print("Original List:", original_list) #output: Original List: [[100, 2, 3, 4, 5, 6]]
print("Shallow Copied List:", shallow_copied_list) #output: Shallow Copied List: [[100, 2, 3, 4, 5, 6]]
print("Deep Copied List:", deep_copied_list) #output: Deep Copied List: [[1, 2, 3, 4, 5, 6]] 


print("===============================" * 2) # Output: =============================================================================================

