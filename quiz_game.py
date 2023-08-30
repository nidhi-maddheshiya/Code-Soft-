class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            user_answer = input(question.prompt + " ").lower()
            if user_answer == question.answer.lower():
                self.score += 1
        print(f"You got {self.score} out of {len(self.questions)} questions correct!")

if __name__ == "__main__":
    question_list = [
        Question("What is the capital of France? ", "Paris"),
        Question("Which planet is known as the Red Planet? ", "Mars"),
        Question("What is 7 times 8? ", "56")
    ]

    quiz = Quiz(question_list)
    quiz.run_quiz()
