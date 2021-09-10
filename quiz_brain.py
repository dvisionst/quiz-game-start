# it will also have one method that will bring up the next question
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list