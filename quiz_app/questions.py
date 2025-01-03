import random

class QuestionManager:
    def __init__(self):
        self.questions = [
            {"text": "Какой фрукт часто называют королем фруктов?", "answer": "дуриан"},
            {"text": "Как называется японский суп с лапшой?", "answer": "рамен"},
            {"text": "Какой овощ является основным ингредиентом для гуакамоле?", "answer": "авокадо"},
            {"text": "Как называется итальянский десерт из кофе и сыра маскарпоне?", "answer": "тирамису"},
            {"text": "Какой орех является основным ингредиентом для пасты песто?", "answer": "кедровый"},
            {"text": "Как называется одичавшая клубника?", "answer": "земляника"},
            {"text": "Какой молочный продукт получают из молока путем сквашивания?", "answer": "йогурт"},
            {"text": "Изготовление какого блюда никогда не удается с первой попытки?", "answer": "блин"},
            {"text": "Самый популярный фрукт в мире?", "answer": "манго"},
            {"text": "В какой стране были созданы все классические соусы?", "answer": "Франция"},
        ]

    def load_questions(self):
        """Перемешивание вопросов."""
        random.shuffle(self.questions)
