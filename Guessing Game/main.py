import random
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_list = question_data["results"]
random.shuffle(question_list)
question_bank = []


for question in question_list:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}")
