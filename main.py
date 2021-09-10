from question_model import Question
from data import question_data

# Creating variables in order to loop through the question_data list
# loop will populate a new list with Question object and respective attributes

question_bank = []
for dictionary in question_data:
    text_q = dictionary["text"]
    text_a = dictionary["answer"]
    question_bank.append(Question(text_q, text_a))