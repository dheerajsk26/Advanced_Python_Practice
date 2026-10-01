

#* Pydantic in Python
# Pydantic is a Python library mainly used for data validation, parsing, and defining the expected structure (schema) of data using Python type hints.
# It is built on top of Python type hints and provides a robust way to define and validate data structures.
# It is especially important in APIs, data engineering, FastAPI, configuration management, and AI/LLM applications.
# It is commonly used in FastAPI for request validation and response serialization.
# Think of Pydantic as sitting between untrusted external data and your trusted Python application, ensuring that only valid and correctly structured data reaches your code.
# It helps ensure that the data your application works with is correct and follows the expected structure.
# Pydantic can also enforce constraints -- Constraints can include things like minimum and maximum values for numbers, string length limits, and more.
    # If you don't validate early, the bad data might travel through your pipeline and fail much later.
    # This proactive validation helps catch errors early and maintain data integrity throughout your application.
    #You can catch the problem at the ingestion boundary. 
    # That's a very useful data-engineering principle: Validate data as early as possible.

#* Key Features of Pydantic:
# 1. Data validation using Python type hints.
# 2. Automatic parsing and conversion of input data.
# 3. Integration with frameworks like FastAPI.
# 4. Clear error messages for invalid data. 


#* Type Hints
# Type hints specify the expected data types for variables, function arguments, and return values.
# They help improve code readability, enable static type checking, and assist tools like Pydantic in validating data.
# Example:
# def greet(name: str) -> str:
#     return f"Hello, {name}"

# print(greet("Alice"))


# -----------------------------------------------------------------------------------------------------------------------------------------

# Pydantic Example usage:
from typing import Optional

from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str

try:
    user = User(id=1, name="John Doe", email="john.doe@example.com")
    print(user)
except ValidationError as e:
    print(e)

# Invalid data example, strictly enforcing type constraints
try:
    user = User(id="one", name="John", email="john@example.com")
    print(user)
except ValidationError as e:
    print(e)

#Coercion example, where a string ID is automatically converted to an integer
try:
    user = User(id="2", name="Alice", email="alice@example.com")
    print(user)
except ValidationError as e:
    print(e)


# -----------------------------------------------------------------------------------------------------------------------------------------


#* Field Validation
# Pydantic allows you to define custom validation rules for individual fields using the `@validator` decorator.
# This ensures that the data meets specific criteria beyond basic type checking.
# Example:

from pydantic import BaseModel, Field, ValidationError, EmailStr
from typing import Optional, Literal

class UserWithFieldValidation(BaseModel):
    #BaseModel provides data validation and parsing based on the defined fields

    id: int = Field(..., gt=0, description="The ID must be a positive integer")
    name: str = Field(..., min_length=3, max_length=50, description="The name must not be empty")
    email: EmailStr = Field(..., description="The email must be a valid email address")
    age: int = Field(..., gt=0, description="The age must be a positive integer")
    city: Optional[str] = Field(None, description="The city is optional")
    gender: Literal["male", "female", "other"] = Field(None, description="The gender is optional and must be 'male', 'female', or 'other'")

try:
    user = UserWithFieldValidation(id=1, name="John Doe", email="john.doe@example.com", age=30, city="New York", gender="male")
    print(user)
except ValidationError as e:
    print(e)

try:
    user = UserWithFieldValidation(id=-1, name="", email="invalid-email", age=-5, city="", gender="unknown")
    print(user)
except ValidationError as e:
    print(e)

# -----------------------------------------------------------------------------------------------------------------------------------------


