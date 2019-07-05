num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))
operation = input("What do you wanna perform with these two numbers?: (Remember choices are CASE SENSITIVE!)\n A. Addition\n B. Subtraction\n C. Multiplication\n D. Division\n")
if operation == "A":
    print(num_1 + num_2)
elif operation == "B":
    print(num_1 - num_2)
elif operation == "C":
    print(num_1 * num_2)
elif operation == "D":
    print(num_1 / num_2)
else:
    print("Invalid operation!")