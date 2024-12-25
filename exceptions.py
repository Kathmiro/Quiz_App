class QuizException(Exception):
    """Базовое исключение для викторины."""
    pass

class InvalidAnswerError(QuizException):
    """Ошибка некорректного ответа."""
    pass
