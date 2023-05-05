import math

while True:
    num1 = float(input("Enter num1: "))
    op = input("Enter your desired operation (+, -, *, /, radical, sin, cos, tan, cot, factorial, or exit)") 

    if op == "+":
        num2 = float(input("Enter num2: "))
        result = num1 + num2

    elif op == "-":
        num2 = float(input("Enter num2: "))
        result = num1 - num2

    elif op == "*":
        num2 = float(input("Enter num2: "))
        result = num1 * num2

    elif op == "/":
        num2 = float(input("Enter num2: "))
        if num2 == 0:
            result = "Error"
        else :
            result = num1 / num2

    elif op == "radical":
        if num1 < 0:
            result = "Error"
        else:
            result = math.sqrt(num1)

    elif op == "sin":
        result = math.tan(num1)

    elif op == "cos":
        result = math.cos(num1)

    elif op == "tan":
        result = math.tan(num1)

    elif op == "cot":
        result = math.cot(num1)

    elif op == "factorial":
        if num1 < 0:
            result = "Error"
        else:
            result = math.factorial(num1)
    
    elif op == "exit":
        break

    print(result)