# Can you create a program to add and multiply two numbers?
# For this, create two functions add_numbers() and multiply_numbers().
# These functions should compute the result and return them to the function call and should print from outside the function.

def add_numbers(a, b):
     return a + b


def multiply_numbers(a, b):
     return a * b
     

a = 10
b = 6

print(f'Sum is: {add_numbers(a, b)}')
print(f'Product is: {multiply_numbers(a, b)}')