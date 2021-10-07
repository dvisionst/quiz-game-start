from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creating variables in order to loop through the question_data list
# loop will populate a new list with Question object and respective attributes

question_bank = []
for dictionary in question_data:
    text_q = dictionary["question"]
    text_a = dictionary["correct_answer"]
    question_bank.append(Question(text_q, text_a))

quiz = QuizBrain(question_bank)

# while loop that will keep populating the next question until there are no more questions left in the set

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")