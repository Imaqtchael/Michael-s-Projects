secret = "Amethyst"
entry = ""
entry_count = 0
out_of_entry = False
while entry != secret and not out_of_entry:
    if entry_count == 0:
        entry = input("Guess the secret word: ")
        entry_count += 1
    elif entry_count < 5:
        entry = input("Try again!: ")
        entry_count += 1
    elif entry_count == 5:
        print("Hint: It is a precious stone")
        entry = input("Try again: ")
        entry_count += 1
    elif 5 < entry_count < 10:
        entry = input("Try again: ")
        entry_count += 1
    elif entry_count == 10:
        print("Hint: It starts with a letter \"A\"")
        entry = input("Try again: ")
        entry_count += 1
    elif 10 < entry_count < 14:
        entry = input("Try again: ")
        entry_count += 1
    elif entry_count == 14:
        print("Last Hint!: It ends with a letter \"T\"")
        entry = input("Try again: ")
        entry_count += 1
    elif entry_count == 15:
        entry = input("Last guess: ")
        entry_count += 1
    else:
        out_of_entry = True
if out_of_entry:
    print("You lose!")
else:
    print("Great!")




