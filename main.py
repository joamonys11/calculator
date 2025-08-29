# main.py
from math_utils import add, subtract, multiply, divide

if __name__ == "__main__":
    input_data = input("Enter two numbers separated by space: ")
    a, b = map(float, input_data.split())

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")

