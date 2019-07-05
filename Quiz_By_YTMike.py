class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is the color of apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What is the color of bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What is the color of strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", str(score) + "/" + str(len(questions)) + " correct answer.")


run()

