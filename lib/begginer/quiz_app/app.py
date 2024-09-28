from question import Question

question_prompts = [
    "What color are the apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "Which animal is known as man's best friend?\n(a) Cat\n(b) Dog\n(c) Rabbit\n\n",
    "What is the capital of France?\n(a) Rome\n(b) Madrid\n(c) Paris\n\n",
    "Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n\n",
    "How many continents are there on Earth?\n(a) Five\n(b) Six\n(c) Seven\n\n",
    "Which of the following is the largest ocean?\n(a) Atlantic Ocean\n(b) Indian Ocean\n(c) Pacific Ocean\n\n",
]

questions = [
    Question(question_prompts[0], "a"),  # Apples are Red/Green (a)
    Question(question_prompts[1], "b"),  # Man's best friend is Dog (b)
    Question(question_prompts[2], "c"),  # Capital of France is Paris (c)
    Question(question_prompts[3], "b"),  # Mars is the Red Planet (b)
    Question(question_prompts[4], "c"),  # Seven continents on Earth (c)
    Question(question_prompts[5], "c"),  # Pacific Ocean is the largest (c)
]


def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
