from question_model import Question
from data import question_data

# Creating variables in order to loop through the question_data list
# loop will populate a new list with Question object and respective attributes

question_bank = []
i = 0
for dictionary in question_data:
    text_q = question_data[i]["text"]
    text_a = question_data[i]["answer"]
    question_bank.append(Question(text_q, text_a))
    i += 1
print(len(question_bank))

print(question_bank[11].text)
