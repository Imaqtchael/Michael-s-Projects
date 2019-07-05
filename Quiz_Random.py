import random


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Jenny ___________ tired.\n",
    "\" ___________ is she?\" \"She's my friend from London\"\n",
    "Today is Wednesday. Yesterday it ___________ Tuesday.\n",
    "It's Thursday today. Tomorrow it ___________ Friday.\n",
    "___________ lots of animals in the zoo.\n",
    "How many people ___________ in your family?\n",
    "\"Has Steve got a sister?\" \"No, he ___________, but he's got 2 brothers.\"\n",
    "Where ___________ Sarah live?\n",
    "Did Mary ___________ to London on the train yesterday?\n",
    "Jack ___________ English, Spanish and a bit of French.\n"
]
questions = [
    Question(question_prompts[0], "is"),
    Question(question_prompts[1], "Who"),
    Question(question_prompts[2], "was"),
    Question(question_prompts[3], "will be"),
    Question(question_prompts[4], "There are"),
    Question(question_prompts[5], "are there"),
    Question(question_prompts[6], "hasn't"),
    Question(question_prompts[7], "does"),
    Question(question_prompts[8], "went"),
    Question(question_prompts[9], "speaks"),
]
x = ""
x += str(random.randint(0, len(questions) - 1))
answer1 = input(questions[int(x)].prompt)
if answer1 == questions[int(x)].answer:
    print("You'r answer is correct!")
else:
    print("Your answer is wrong, it should be " + "\"" + questions[int(x)].answer + "\".")


