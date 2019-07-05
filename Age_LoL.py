def ask_age():
    age = input("How old are you?: ")
    if int(age) == 1:
        print("You are " + age, "year old")
    else:
        print("You are " + age, "years old")
ask_age()