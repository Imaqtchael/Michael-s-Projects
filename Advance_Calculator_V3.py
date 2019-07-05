def calculator():
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    elif operation == "**":
        print(num1 ** num2)


in_num2 = 0
err = True
while err:
    try:
        num1 = int(input("Type your first number: "))
        operation = input("Type the operation you want to perform: ")
        while operation not in "+-*/**" or operation == "":
            operation = input("Please input a valid operation: ")
        in_num2 += 1
        num2 = int(input("Type your second number: "))
        calculator()
        err = False
    except ValueError:
        if in_num2 == 0:
            print("Please input a number!")
        elif in_num2 > 0:
            num2_err = True
            while num2_err:
                try:
                    num2 = int(input("Type your second number: "))
                    calculator()
                    num2_err = False
                    err = False
                except ValueError:
                    print("Please input a number!")
    except ZeroDivisionError:
        print("Can't divide with ZERO!")
