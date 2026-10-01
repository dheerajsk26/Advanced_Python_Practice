
#* Object-Oriented Programming (OOP) in Python
# OOP is a programming paradigm that uses objects and classes to structure code.
# It allows for encapsulation, inheritance, and polymorphism.
# Python supports OOP and provides features to define classes, create objects, and implement methods.


# Why use OOP?
# OOP helps in organizing code, making it reusable, and easier to maintain.
# It allows modeling real-world entities as objects with attributes and behaviours.
# It promotes code modularity and helps in managing complexity in large programs.
# Reusability: Code can be reused through inheritance, reducing redundancy.
# Modularity: Code is organized into classes and objects, making it easier to manage and understand.
# Scalability: OOP allows for building scalable and maintainable software systems.

# Key Concepts of OOP:
# Classes and Objects:
# A class is a blueprint for creating objects. It defines attributes and methods that the objects will have.
# An object is an instance of a class. It represents a specific entity with its own state and behaviour.
# A class defines the structure and behavior of objects, while an object is a concrete instance of a class.
# A method is a function defined within a class that operates on instances of the class. It can access and modify the object's attributes and perform actions related to the object.


# Inheritance: Classes can inherit attributes and methods from other classes, promoting code reuse.
# Encapsulation: Data and methods are bundled together, providing data hiding. Access to the internal state is controlled through methods.
# Polymorphism: Objects of different classes can be treated as objects of a common superclass.
# Abstraction: Hiding complex implementation details and exposing only necessary functionality.


# Example of defining a class and creating objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling the greet method on the objects
person1.greet()
person2.greet()


print("===========================================" * 2)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary += self.salary * percent / 100

    def summary(self):
        return f"{self.name} earns {self.salary:.0f}"

# Objects: separate instances of the class
emp1 = Employee("Dheeraj", 60000)
emp2 = Employee("Asha", 75000)

emp1.give_raise(10)
print(emp1.summary())   # Dheeraj earns 66000

emp2.give_raise(5)
print(emp2.summary())   # Asha earns 78750



print("===========================================" * 2) #Output = ===================================================...

#* Encapsulation in Python
# Encapsulation is the concept of restricting access to certain attributes and methods of an object.
# In Python, this is typically done using private variables (prefixing with double underscores) 
        # and providing getter and setter methods to access and modify them.

#How Encapsulation is implemented in Python:
# 1. Prefixing attributes with double underscores to make them private.
# 2. Providing getter and setter methods to access and modify the private attributes.

# Public methods (getters and setters) are used to access and modify private attributes.
# Private attributes are not directly accessible from outside the class.
# Protected attributes (prefixing with a single underscore) are a convention to indicate that they should not be accessed directly, but they are still accessible from outside the class.


# Example of Encapsulation in Python 
class EncapsulatedEmployee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def give_raise(self, percent):
        self.__salary += self.__salary * percent / 100

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def summary(self):
        return f"{self.__name} earns {self.__salary:.0f}"

# Creating objects of the EncapsulatedEmployee class
enc_emp1 = EncapsulatedEmployee("Dheeraj", 60000)
enc_emp2 = EncapsulatedEmployee("Asha", 75000)

enc_emp1.give_raise(10)
print(enc_emp1.summary())   # Dheeraj earns 66000

enc_emp2.give_raise(5)
print(enc_emp2.summary())   # Asha earns 78750



print("===========================================" * 2) #Output = ===================================================...




#* Types of Methods in a Class
# 1. Instance Methods: Operate on an instance of the class and have access to instance attributes.
# 2. Class Methods: Operate on the class itself and have access to class attributes. Defined using @classmethod decorator.
# 3. Static Methods: Do not operate on an instance or the class. Defined using @staticmethod decorator.

# Example of Instance method in a class
class ExampleClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print(f'The value is {self.value}')

# Creating an object of the class
example = ExampleClass(10)
example.instance_method()

#---------------------------------------------------------------------------

# Example of Class method in a class
class ExampleClassWithClassMethod:
    class_attribute = "I am a class attribute"

    @classmethod
    def class_method(cls):
        print(f'The class attribute is {cls.class_attribute}')

# Creating an object of the class
example_class_method = ExampleClassWithClassMethod()
example_class_method.class_method()

#---------------------------------------------------------------------------

# Example of Static method in a class
class ExampleClassWithStaticMethod:
    @staticmethod
    def static_method():
        print("This is a static method.")

# Creating an object of the class
example_static_method = ExampleClassWithStaticMethod()
example_static_method.static_method()



# -------------------------------------------------------------------------------------------------------------------------------------------


# Example of a simple class in Python


class Company:
    def __init__(self, company_name: str):
        self.company_name = company_name

    def company_info(self):
        print(f'Company Name: {self.company_name}')

# Creating an object of the Company class
company = Company("Anthropic")
company.company_info()

#----------------------------------------------------------------------------------------------

#Single-level Inheritance Example using a subclass

class Employee(Company):
    def __init__(self, company_name: str, employee_name: str):
        super().__init__(company_name)
        self.employee_name = employee_name

    def employee_info(self):
        super().company_info()
        print(f'Employee Name: {self.employee_name}')

# Creating an object of the Employee class
employee = Employee("Anthropic", "John Doe")
employee.employee_info()


#----------------------------------------------------------------------------------------------

#Multiple-level Inheritance Example using a subclass of Employee

class Manager(Employee):
    def __init__(self, company_name: str, employee_name: str, manager_name: str):
        super().__init__(company_name, employee_name)
        self.manager_name = manager_name

    def manager_info(self):
        super().employee_info()
        print(f'Manager Name: {self.manager_name}')

# Creating an object of the Manager class
manager = Manager("Anthropic", "John Doe", "Jane Smith")
manager.manager_info()



# ==============================================================================================

#* Polymorphism in Python
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Same method name can be used in different classes, and the appropriate method will be called based on the object.
# In simple terms, polymorphism allows different classes to define methods with the same name, and the correct method is called based on the object type.


# Example of Polymorphism in Python

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def make_animal_speak(animal):
    animal.speak()

# Creating objects of Cat and Dog classes
cat = Cat()
dog = Dog()

# Demonstrating polymorphism
make_animal_speak(cat)  # Output: Meow
make_animal_speak(dog)  # Output: Woof

# In this example, both Cat and Dog classes have a method named 'speak'. 
# The make_animal_speak function demonstrates polymorphism by calling the appropriate 'speak' method based on the object type.



# ----------------------------------------------------------------------------------------------

#* Duck Typing in Python
# Duck typing is a concept related to polymorphism where the type or class of an object is determined by its behavior (methods and properties) rather than its inheritance from a specific class.
# The name comes from the saying "If it looks like a duck and quacks like a duck, it must be a duck."

# Example of Duck Typing in Python

class Bird:
    def fly(self):
        print("Flying in the sky")

class Airplane:
    def fly(self):
        print("Flying through the clouds")

def let_it_fly(entity):
    entity.fly()

# Creating objects of Bird and Airplane classes
bird = Bird()
airplane = Airplane()

# Demonstrating duck typing
let_it_fly(bird)      # Output: Flying in the sky
let_it_fly(airplane)  # Output: Flying through the clouds

# In this example, both Bird and Airplane classes have a method named 'fly'.
# The let_it_fly function demonstrates duck typing by calling the appropriate 'fly' method based on the object passed, regardless of its class.

# This allows for flexibility and code reuse, as functions can operate on objects of different types as long as they implement the required behavior (in this case, the 'fly' method).  