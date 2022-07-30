class QuizBrain():
    def __init__(self, question_list):
        self.question_number =0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        answer =input(f"Q {self.question_number }: {current_question.text} (True/False)")
        correct_answer = current_question.answer
        self.check_answer(answer, correct_answer)

    def check_answer(self,answer,correct_answer):
        if(answer == correct_answer):
            print("You Are Correct")
            self.score+=1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("You Are Wrong")
            print(f"Your current score is {self.score}/{self.question_number}")