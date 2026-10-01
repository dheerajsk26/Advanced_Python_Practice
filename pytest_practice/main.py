
#* Sample application code
# This is just a small, plain module with a few functions/classes that
# we'll write pytest tests against in test_main.py (in this same folder).
# There's nothing pytest-specific here - pytest tests work against
# ordinary Python code, that's the whole point.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


def greet(name):
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


class Counter:
    """A tiny stateful class - useful for demonstrating fixtures,
    since a fixture can hand each test a fresh Counter instance."""

    def __init__(self, start=0):
        self.value = start

    def increment(self, step=1):
        self.value += step
        return self.value

    def reset(self):
        self.value = 0
