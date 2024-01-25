# Can you create a program to add and multiply two numbers?
# For this, create two functions add_numbers() and multiply_numbers().
# These functions should compute the result and return them to the function call and should print from outside the function.

def add_numbers(a, b):
    numbers_added = a + b
    return numbers_added

def multiply_numbers(a, b):
    numbers_multiplied = a * b
    return numbers_multiplied

a = 10
b = 6

print(add_numbers(a, b))
print(multiply_numbers(a, b))