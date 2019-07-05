
def calc():
    if operation == "+":
        print(str(num1 + num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "-":
        print(str(num1 - num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "*":
        print(str(num1 * num2) + "\nDone in " + str(attempt) + " attempts.")
    elif operation == "/":
        print(str(num1 / num2) + "\nDone in " + str(attempt) + " attempts.")


err = True
attempt = 0
while err:
    try:
        if attempt == 0:
            attempt += 1
            num1 = float(input("Enter your first number: "))
            operation = input("What operation you want to perform?: ")
            while operation not in "+-*/":
                attempt += 1
                operation = input("Invalid operation! What operation you want to perform: ")
            num2 = float(input("Enter your second number: "))
            calc()
            err = False
        else:
            attempt += 1
            num1 = float(input("Try again! Enter your first number: "))
            operation = input("What operation you want to perform?: ")
            while operation not in "+-*/":
                attempt += 1
                operation = input("Invalid operation! What operation you want to perform: ")
            num2 = float(input("Enter your second number: "))
            calc()
            err = False
    except ValueError:
        print("You cannot do something with a letter")
    except ZeroDivisionError:
        print("You cannot divide with ZERO!")