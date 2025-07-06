import math  # Import the math module

# 1. Ask the user for a number
number = float(input("Enter a number: "))

# 2. Perform calculations using the math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)  # number is in radians

# 3. Display the results
print("\nResults:")
print("Square root of", number, "is:", square_root)
print("Natural logarithm (ln) of", number, "is:", natural_log)
print("Sine of", number, "(in radians) is:", sine_value)
