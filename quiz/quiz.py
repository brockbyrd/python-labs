class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "How many yards are between each endzone on an American Football field?\n(a) 100yds\n(b) 50yds\n(c) 120yds\n",
    "How many players are on the field at one time for each team?\n(a) 11\n(b) 9\n(c) 15\n",
    "What position stands behind the center and leads the offense?\n(a) Left Tackle\n(b) Linebacker\n(c) Quarterback\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions)) + " correct")

run_quiz(questions)