
#* Data structures in Python
#Types of data structures in Python:
#1. List: A list is a collection of items that are ordered and changeable. It allows duplicate members.
#2. Tuple: A tuple is a collection of items that are ordered and unchangeable. It allows duplicate members.
#3. Set: A set is a collection of items that are unordered and unindexed. It does not allow duplicate members.
#4. Dictionary: A dictionary is a collection of items that are unordered, changeable, and indexed. 


#* create a list
#A list can be created by placing all the items (elements) inside square brackets [], separated by commas.
my_list = [1, 2, 3, 4, 5]

print("List:", my_list) #output: List: [1, 2, 3, 4, 5]
print("Type of my_list:", type(my_list)) #output: Type of my_list: <class 'list'>

#create a list by using the list() 
letters = list('Python')
print(letters)

#* Create a tuple
#A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple) #output: Tuple: (1, 2, 3, 4, 5)
print("Type of my_tuple:", type(my_tuple)) #output: Type of my_tuple: <class 'tuple'>

#* Create a set
#A set is created by placing all the items (elements) inside curly braces {}, separated by commas.
#Set does not allow duplicate members.

my_set = {1, 2, 3, 4, 5}
print("Set:", my_set) #output: Set: {1, 2, 3, 4, 5}
print("Type of my_set:", type(my_set)) #output: Type of my_set: <class 'set'>

#* Create a dictionary
#A dictionary is created by placing all the items (elements) inside curly braces {}, separated by commas.
#Each item is a key-value pair, separated by a colon :.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict) #output: Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Type of my_dict:", type(my_dict)) #output: Type of my_dict: <class 'dict'>


print("===============================" * 2) # Output: =============================================================================================

#* Unpacking Lists 
#List unpacking allows you to assign the elements of a list to multiple variables in a single statement.

person = ["John", "Doe", 30, "USA"]
first_name, last_name, age, country = person

print("First Name:", first_name) #output: First Name: John
print("Last Name:", last_name) #output: Last Name: Doe
print("Age:", age) #output: Age: 30
print("Country:", country) #output: Country: USA

#Unpacking can also be done with the * operator to capture multiple elements into a list.

employee = ["Alice", "Smith", 28, "Manager", "HR"]
first_name, last_name, age, *details = employee

print("First Name:", first_name) #output: First Name: Alice
print("Last Name:", last_name) #output: Last Name: Smith
print("Age:", age) #output: Age: 28
print("Details:", details) #output: Details: ['Manager', 'HR']


#Unpacking with underscore
#The underscore (_) is often used as a placeholder for values that you want to ignore during unpacking.

data = ["Alice", "Smith", 28, "Manager", "HR"]
first_name, last_name, _, *details = data

print("First Name:", first_name) #output: First Name: Alice
print("Last Name:", last_name) #output: Last Name: Smith
print("Details:", details) #output: Details: ['Manager', 'HR']
#In this example, the underscore (_) is used to ignore the age value during unpacking.

#Ignoring multiple values
#You can use multiple underscores to ignore multiple values during unpacking.

data = ["Alice", "Smith", 28, "Manager", "HR"]
first_name, last_name, *_ = data

print("First Name:", first_name) #output: First Name: Alice
print("Last Name:", last_name) #output: Last Name: Smith
#In this example, the asterisk (*) with an underscore (*_) is used to ignore multiple values during unpacking. 

print("===============================" * 2) # Output: =============================================================================================

#* All or Any functions
#The all() function returns True if all elements in an iterable are true.
#The any() function returns True if any element in an iterable is true.

numbers = [1, 2, 3, 4, 5]
print("All numbers are positive:", all([1,0,4])) #output: All numbers are positive: False
print("Any number is greater than 3:", any(n > 3 for n in numbers)) #output: Any number is greater than 3: True 


#* Remove and Pop functions 
#The remove() function removes the first occurrence of a specified value from a list.
#The pop() function removes and returns an element at a specified index (default is the last element).

fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")
print("After remove:", fruits) #output: After remove: ['apple', 'cherry', 'date']

popped_fruit = fruits.pop(1)
print("Popped fruit:", popped_fruit) #output: Popped fruit: cherry
print("After pop:", fruits) #output: After pop: ['apple', 'date']


print("===============================" * 2) # Output: =============================================================================================

#* Iterable and Iterator
#An iterable is any Python object capable of returning its members one at a time, allowing it to be iterated over in a for-loop.
#An iterator is an object that represents a stream of data; it returns the next item of the sequence when you call the `next()` function on it.

numbers = [1, 2, 3, 4, 5]
iterable = iter(numbers)

print("First element:", next(iterable)) #output: First element: 1
print("Second element:", next(iterable)) #output: Second element: 2
print("Remaining elements:")
for num in iterable:
    print(num) #output: 3, 4, 5 (each number on a new line)
#Note: Once an iterator is exhausted, it cannot be reset. You need to create a new iterator to iterate again. 

print("===============================" * 2) # Output: =============================================================================================

#* map Function, filter Function and Zip Function
#The map() function applies a given function to all items in an iterable.
#The filter() function filters elements in an iterable based on a given condition.
#The zip() function combines multiple iterables into a single iterable of tuples.  

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers) #output: Squared numbers: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers) #output: Even numbers: [2, 4]

letters = ["a", "b", "c", "d", "e"]
zipped = list(zip(numbers, letters))
print("Zipped list:", zipped) #output: Zipped list: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

print("===============================" * 2) # Output: =============================================================================================

#* Lambda Function
#A lambda function is a small anonymous function defined using the `lambda` keyword. 
#It can have any number of arguments but only one expression.

add = lambda x, y: x + y
print("Sum using lambda:", add(3, 5)) #output: Sum using lambda: 8

print("===============================" * 2) # Output: =============================================================================================
