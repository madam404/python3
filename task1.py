def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # same as result = result * i
    return result

# Example usage:
number = int(input("Enter a number: "))
fact = factorial(number)
print(f"The factorial of {number} is: {fact}")
