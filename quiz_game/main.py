from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]

for i in question_data:
    new_ques = Question(i["text"],i["answer"])
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()