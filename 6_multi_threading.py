

#* Multi-threading in Python
# Multi-threading allows concurrent execution of code, which can improve performance for I/O-bound tasks. 
# However, due to the Global Interpreter Lock (GIL), CPU-bound tasks may not see significant performance gains.

#Use case:
# Multi-threading is useful when you have tasks that are I/O-bound, such as reading/writing files, making network requests, or interacting with databases. 
# It allows these tasks to run concurrently, improving overall performance.




#Example without using multi-threading
import time  # Added import for time module, required for sleep function in multi-threading examples

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

print_numbers()
print_letters()



# # Example of multi-threading in Python using the threading module:
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Both threads have completed.")

# -----------------------------------------------------------------------------------------------------------------------


# Example of multi-threading using a threadpool Executor from the concurrent.futures module:
import concurrent.futures

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

# Using ThreadPoolExecutor to run the functions concurrently with a maximum of 2 worker threads(max_workers ideally should match the number of concurrent tasks but maximum is system dependent)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(print_numbers)
    executor.submit(print_letters)

print("Both threads have completed using ThreadPoolExecutor.")

