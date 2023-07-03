import data
import requests


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.next_question()
        self.has_question = self.question_number < len(self.question_list)

    def update_has_question(self):
        self.has_question = self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        self.current_question = self.question_list[self.question_number - 1]
        return self.current_question

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def reset_quiz(self, questions):
        self.__init__(questions)


