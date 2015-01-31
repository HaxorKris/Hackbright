import math

def add(num1, num2):
    return int(num1) + int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return float(num1 / num2)

def square(num1):
    return int(num1) * int(num1)

def cube(num1):
    return int(num1) * int(num1) * int(num1)

def power(num1, num2):
    return math.pow(int(num1), int(num2))

def mod(num1, num2):
    return int(num1) % int(num2)