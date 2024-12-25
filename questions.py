import random

class QuestionManager:
    """"list of the questions"""
    def __init__(self):
        self.questions = [
            {"text": "Какова столица Франции?", "answer": "Париж"},
            {"text": "Сколько будет 2 + 2?", "answer": "4"},
            {"text": "Какого цвета небо?", "answer": "синий"}
        ]

    def load_questions(self):
        """Перемешивание вопросов."""
        random.shuffle(self.questions)