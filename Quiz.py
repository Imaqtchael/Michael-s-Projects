ques = ["1.) The satellite of the Earth is _______.\n(a) Moon\n(b) Asteroid\n(c) Sun\n(d) None of the above.", "2.) The color of Apples is _______.\n(a) White\n(b) Purple\n(c) Brown\n(d) Red/Green",
        "3.) Earth is the _____ planet from the Sun.\n(a) First\n(b) Second\n(c) Third\n(d) The Earth is not in the Solar System."]
score = 0
print(ques[0])
ans1 = input("Your answer in question number 1: ")
if ans1 == "a":
    print("Your answer is correct!\n\n")
    score += 1
else:
    print("Your answer is wrong, The correct answer is Moon.\n\n")

print(ques[1])
ans2 = input("Your answer in question number 2: ")
if ans2 == "d":
    print("Your answer is correct!\n\n")
    score += 1
else:
    print("Your answer is wrong, The correct answer is Red/Green.\n\n")

print(ques[2])
ans3 = input("Your answer in question number 3: ")
if ans3 == "c":
    print("Your answer is correct!\n\n")
    score += 1
else:
    print("Your answer is wrong, The correct answer is Third.\n\n")
print("Test is done!")
if score == 0 or score == 1:
    print("You've got", score, "correct answer!")
elif score > 1:
    print("You've got", score, "correct answers!")