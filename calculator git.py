def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator in Python")
print("Operations: +  -  *  /")

while True:
    op = input("Enter operation (+, -, *, /) or 'q' to quit: ")

    if op == 'q':
        print("Exiting Calculator...")
        break

    if op not in ['+', '-', '*', '/']:
        print("Invalid operation! Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", add(num1, num2))
    elif op == '-':
        print("Result:", subtract(num1, num2))
    elif op == '*':
        print("Result:", multiply(num1, num2))
    elif op == '/':
        print("Result:", divide(num1, num2))

    print() 