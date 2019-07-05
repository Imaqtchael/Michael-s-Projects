err = True
attempt = 0
operation_out = 0


def calc(num1, operation, num2):
    if operation == "+":
        if attempt == 1:
            print(str(num1 + num2) + "\nDone in " + str(attempt) + " attempt.")
        else:
            print(str(num1 + num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "-":
        if attempt == 1:
            print(str(num1 - num2) + "\nDone in " + str(attempt) + " attempt.")
        else:
            print(str(num1 - num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "*":
        if attempt == 1:
            print(str(num1 * num2) + "\nDone in " + str(attempt) + " attempt.")
        else:
            print(str(num1 * num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "/":
        if attempt == 1:
            print(str(num1 / num2) + "\nDone in " + str(attempt) + " attempt.")
        else:
            print(str(num1 / num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "**":
        if attempt == 1:
            print(str(num1 ** num2) + "\nDone in " + str(attempt) + " attempt.")
        else:
            print(str(num1 ** num2) + "\nDone in " + str(attempt) + " attempts.")


while err:
    try:
        if attempt == 0:
            attempt += 1
            num1 = float(input("Enter your first number: "))
            operation = input("What operation you want to perform?: ")
            while operation not in "+-*/**" or operation == "":
                if operation == "":
                    attempt += 1
                    operation = input("You cannot leave the operation BLANK! Try again: ")
                else:
                    attempt += 1
                    operation = input("Invalid operation! Try again: ")
            operation_out += 1
            num2 = float(input("Enter your second number: "))
            calc()
            err = False
        elif attempt > 0:
            attempt += 1
            num1 = float(input("Enter your first number again: "))
            operation = input("What operation you want to perform?: ")
            while operation not in "+-*/" or operation == "":
                if operation == "":
                    attempt += 1
                    operation = input("You cannot leave the operation BLANK! Try again: ")
                else:
                    attempt += 1
                    operation = input("Invalid operation! Try again: ")
            operation_out += 1
            num2 = float(input("Enter your second number: "))
            calc()
            err = False
    except ValueError:
        if operation_out > 0:
            num2_err = True
            while num2_err:
                attempt += 1
                try:
                    num2 = float(input("Try again! Enter your second number: "))
                    calc()
                    num2_err = False
                    err = False
                except ValueError:
                    print("Invalid! Please input a NUMBER!")
        else:
            print("Invalid! Please input a NUMBER!")
    except ZeroDivisionError:
        print("You cannot divide with ZERO!")