import random


def dice():
    return random.randrange(1, 7)


inp = input("Do you wanna play the Dice Simulator?: ")
if inp == "Yes":
    print(dice())
elif inp == "No":
    print("OK have a nice day!")
    exit()
inp2 = input("Do you wanna play again?: ")
while inp2 == "Yes":
    print("The number this time is ", dice())
    inp2 = input("Do you wanna play again?: ")
if inp2 == "No":
    print("Thank you for playing!")