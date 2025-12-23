"""
Build a calculator that supports basic arithmetic using lambda functions and uses map to apply operations over lists.
"""

# Lambda function for basic operations

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else 'Undefined (division by zero)'

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

# apply operations over lists using map
addition = list(map(lambda a, b: add(a, b), list1, list2))
subtraction = list(map(lambda a, b: sub(a, b), list1, list2))
multiplication = list(map(lambda a, b: mul(a, b), list1, list2))
division = list(map(lambda a, b: div(a, b), list1, list2))

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
