from greetings_module import greet_user
from math_utils import add_numbers

# Using positional arguments
greet_user("Charles", "AWS Developer")

# Using keyword arguments
greet_user(role="AWS Architect", name="Charles")

# Using default argument
greet_user("Charles")

# Mathematical operation
result = add_numbers(5, 7)
print(f"5 + 7 = {result}")

