
#* Async in Python

# Async allows you to write concurrent code using the async/await syntax.
# Async Python means writing Python programs that can start another task while waiting for the current task to finish.
# The key idea is: Async is mainly about efficiently handling waiting time, not making Python code magically execute faster.
# This becomes especially useful for APIs, web applications, network calls, databases, and other I/O-heavy workloads.
# Frameworks such as FastAPI heavily use async Python.
# Coroutine = worker/task
# Event loop = coordinator


# Coroutine = a task that can pause and resume.
# Event loop = the coordinator that decides which paused/runnable task gets to asyncio.run next.
    # That ability to pause at await and later continue from where it stopped is fundamental.

# Example without a coroutine:
import asyncio

# Define an asynchronous main function and run it using asyncio.
async def main():
    print("Hello") # Print "Hello" immediately
    asyncio.sleep(1) # Wait for 1 second asynchronously
    print("World") # Print "World" after a 1-second delay

# Run the asynchronous main function using asyncio.
asyncio.run(main())


# -----------------------------------------------------------------------------------------------------------------------------------------

# Coroutine functions are defined using the async def syntax and can be awaited using the await keyword. 
# The await keyword is used to pause the execution of the coroutine until the awaited task is complete.

# Example of a coroutine function:
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Run the coroutine function using asyncio.
asyncio.run(say_hello())


