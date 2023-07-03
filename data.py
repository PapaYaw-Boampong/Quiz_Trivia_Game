import requests
from html import unescape
from question_model import Question


# Option 1
# question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")


def extract_questions():
    parameter = {
        "amount": 10,
        "type": "boolean"
    }
    question_data = requests.get("https://opentdb.com/api.php", params=parameter)
    question_data.raise_for_status()
    questions = question_data.json()
    return questions["results"]


def generate_questions():
    raw_questions = extract_questions()

    question_bank = []
    for question in raw_questions:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(unescape(question_text), unescape(question_answer))
        question_bank.append(new_question)
    return question_bank

