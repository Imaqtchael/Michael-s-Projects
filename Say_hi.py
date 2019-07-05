def say_hi(name):
    age = input("How old are you " + name + "?:\n")
    birth = 2019 - int(age)
    year = birth + 100
    print("Hello " + name + ", you are born in " + str(birth) + " and are " + age + " years old!")
    print("You will be 100 years old in the year " + str(year) + "!")
ans, ans2 = "Yes", "No"
user_ans = input("This is a program to know when will you be 100 years old!\nAre you ready?: ")
while user_ans != ans and user_ans != ans2:
    print("Please be specific")
    user_ans = input("Are you ready?: ")
if user_ans == ans:
    say_hi(input("Enter your name: \n"))
elif user_ans == ans2:
    print("Oh sorry!") and exit()