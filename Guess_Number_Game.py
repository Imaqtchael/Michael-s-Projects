import random


def guess_num_game():
    print("In this game you will guess the secret number and you only have 8 lives!\nGood Luck!")
    x = ""
    x += str(random.randint(0, 100))
    lives = 1
    err_limit = 8
    print(x)
    ans = int(input("Guess the secret number: "))
    while ans != int(x) and err_limit != lives:
        print("You only have", err_limit - lives, "lives left!")
        if ans > int(x):
            lives += 1
            ans = int(input("Your guess is higher than the secret number: "))
        elif ans < int(x):
            lives += 1
            ans = int(input("Your guess is lower than the secret number, Try again: "))
    if lives == err_limit:
        print("You lose!")
    else:
        print("You win!")


ques = input("Do you want to play the Guess the Number Game?: ")
while ques != "Yes" and ques != "No":
    ques = input("Please type \"Yes\" or \"No\": ")
if ques == "Yes":
    guess_num_game()
elif ques == "No":
    exit()
ques1 = input("Do you want to play again?: ")
while ques1 != "Yes" and ques1 != "No":
    ques1 = input("Please type \"Yes\" or \"No\": ")
while ques1 == "Yes":
    guess_num_game()
    ques1 = input("Do you want to play again?: ")
if ques1 == "No":
    exit()
