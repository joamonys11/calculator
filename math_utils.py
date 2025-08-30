def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a,b):
    return a * b

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return x ** 0.5


def log(x, base=10):
    import math
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    return math.log(x, base)

def sin(x):
    import math
    return math.sin(x)


def cos(x):
    import math
    return math.cos(x)


def tan(x):
    import math
    return math.tan(x)


