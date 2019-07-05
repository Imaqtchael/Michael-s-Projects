import random
import math
from itertools import permutations


def palindrome():
    user_inp = input("What is the word?: ")
    palin = user_inp[len(user_inp):0:-1]

    print(palin + user_inp[0])
    if palin + user_inp[0] == user_inp:
        print("It is a palindrome!")
    else:
        print("It's not a palindrome!")


def even_detector():
    nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    num_list = []
    for num in nums:
        even = num % 2
        if even == 0:
            num_list.append(num)
    print(num_list)


def even_detector_v2():
    nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    num_list = [num for num in nums if num % 2 == 0]
    return num_list


def pick_pack():
    player1 = input("Player 1\nRock, Paper, or Scissors?: ")
    player2 = input("Player 2\nRock, Paper, or Scissors?: ")
    if player1 == player2:
        print("Draw!")
    elif player1 == "Rock" and player2 == "Paper":
        print("Player 2 wins!")
    elif player1 == "Rock" and player2 == "Scissors":
        print("Player 1 wins!")
    elif player1 == "Paper" and player2 == "Scissors":
        print("Player 2 wins!")
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 wins!")
    elif player1 == "Scissors" and player2 == "Rock":
        print("Player 2 wins!")
    elif player1 == "Scissors" and player2 == "Paper":
        print("Player 1 wins!")
    else:
        print("Invalid input/s.")


def pick_pack_game():
    pick_pack()
    again = input("Do you want to play again?: ")
    if again == "Yes":
        while again == "Yes":
            pick_pack()
            again = input("Do you want to play again?: ")
    else:
        exit()


def prime_num():
    ask = int(input("What is your number?: "))
    prime = list(range(1, ask + 1))
    prime_list = []
    for num in prime:
        if ask % num == 0:
            prime_list.append(num)
    print(prime_list)
    if len(prime_list) == 2:
        print("It is a prime number!")
    else:
        print("It's not a prime number.")


def random_list():
    w = []
    z = range(1, 101)
    x = []
    for num in z:
        r = random.randint(1, 10**3)
        x.append(r)
    y = []
    for num in z:
        r = random.randint(1, 10**3)
        y.append(r)
    for num in x:
        if num in y:
            w.append(num)
    print(w)
    print(x)
    print(y)


def end_list():
    a = [5, 10, 15, 20, 25]
    b = [a[0], a[len(a)-1]]
    print(b)


def seq_generator():
    a = [1, 1]
    ask = int(input("Number of sequence to generate: "))
    for num in range(1, ask - 1):
        b = a[len(a) - 2] + a[len(a) - 1]
        a.append(b)
    print(a)


def sentence_reverse():
    answer = input("The sentence or phrase you want to reverse: ")
    answer = answer.split()
    answer.reverse()
    answer = " ".join(answer)
    print(answer)


def pass_generator():
    a = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    b = "1234567890"
    password = ""
    for num in range(1, 9):
        password += a[random.randint(0, 51)]
    for num in range(1, 5):
        password += b[random.randint(0, 8)]
    print(password)


def num_guesser_bot():
    guess = 50
    num = 50
    num_guess = 0
    print(str(guess))
    user_inp = input()
    if user_inp == "Higher":
        num_guess += 1
        guess += math.ceil(num / 2)
    elif user_inp == "Lower":
        num_guess += 1
        guess -= math.ceil(num / 2)
    elif user_inp == "Right":
        num_guess += 1
        print("Guessed in " + str(num_guess) + " attempt.")
        exit()
    print(str(guess))
    user_inp = input()
    if user_inp == "Higher":
        num_guess += 1
        guess += math.ceil(num / 4)
    elif user_inp == "Lower":
        num_guess += 1
        guess -= math.ceil(num / 4)
    elif user_inp == "Right":
        num_guess += 1
        print("Guessed in " + str(num_guess) + " attempts.")
        exit()
    print(str(guess))
    user_inp = input()
    if user_inp == "Higher":
        num_guess += 1
        guess += math.ceil(num / 8)
    elif user_inp == "Lower":
        num_guess += 1
        guess -= math.ceil(num / 8)
    elif user_inp == "Right":
        num_guess += 1
        print("Guessed in " + str(num_guess) + " attempts.")
        exit()
    print(str(guess))
    user_inp = input()
    if user_inp == "Higher":
        num_guess += 1
        guess += math.ceil(num / 16)
    elif user_inp == "Lower":
        num_guess += 1
        guess -= math.ceil(num / 16)
    elif user_inp == "Right":
        num_guess += 1
        print("Guessed in " + str(num_guess) + " attempts.")
        exit()
    print(str(guess))
    user_inp = input()
    if user_inp == "Higher":
        num_guess += 1
        guess += math.ceil(num / 32)
    elif user_inp == "Lower":
        num_guess += 1
        guess -= math.ceil(num / 32)
    elif user_inp == "Right":
        num_guess += 1
        print("Guessed in " + str(num_guess) + " attempts.")
        exit()
    print(str(guess))
    user_inp = input()
    if user_inp == "Higher":
        num_guess += 1
        guess += math.ceil(num / 64)
    elif user_inp == "Lower":
        num_guess += 1
        guess -= math.ceil(num / 64)
    elif user_inp == "Right":
        num_guess += 1
        print("Guessed in " + str(num_guess) + " attempts.")
        exit()
    print(str(guess))
    num_guess += 1
    print("Guessed in " + str(num_guess) + " attempts.")
    exit()


def randomize_name():
    attempts = 0
    while True:
        attempts += 1
        a = "IMHCLEA"
        b = ""
        for num in range(1, 8):
            b += a[random.randint(0, 6)]
        print(b)
        if b == "MICHAEL":
            print("Done in " + str(attempts) + " attempts.")
            break


class Student:
    def __init__(self, name, age, address, grade):
        self.name = name
        self.age = age
        self.address = address
        self.grade = grade


students = [
    Student("Kirwen", 20, "Kasiglahan", 90),
    Student("Michael", 17, "Urban", 90),
    Student("Jerico", 18, "Urban", 85),
    Student("Clyde", 18, "Kasiglahan", 90),
    Student("Jensen", 18, "Payatas", 85),
    Student("Garado", 19, "Manggahan", 85)
]


def school_name_finder():
    name1 = input("Who are you looking for?: ")
    for x in students:
        if name1 == x.name:
            print("Yes he's here!")
            ask = input("Do you want to see his profile?: ")
            while ask != "Yes" and ask != "No":
                ask = input("Please input \"Yes\" or \"No\": ")
            if ask == "Yes":
                print("Name:", x.name, "\nAddress:", x.address, "\nAge:", x.age, "\nGrade:", x.grade)
                exit()
            elif ask == "No":
                exit()
        elif name1 != x.name:
            continue
    print("He's not here!")


