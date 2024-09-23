from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)
    
# print(question_bank[0].answer)

quiz=Quiz_Brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
