import tkinter as tk
from tkinter import messagebox
from quiz_app.questions import QuestionManager
from quiz_app.exceptions import InvalidAnswerError
import platform


class QuizApp:
    """Initialize the quiz application"""
    def __init__(self, root):
        self.root = root
        self.root.title("Викторина")
        self.manager = QuestionManager()
        self.manager.load_questions()
        self.current_question_index = 0
        self.score = 0

        # Настройка окна
        self.root.configure(bg="palevioletred")  # Насыщенный розовый фон
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = screen_width // 2
        window_height = screen_height // 2
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Четверть экрана, по центру

        # Интерфейс
        font_name = "Calibri" if platform.system() == "Windows" else "Helvetica"  # Поддержка разных шрифтов в разных ОС
        question_font_color = "midnightblue"  # Цвет шрифта вопроса
        question_font_hex = "#191970" # шестнадцатеричный код цвета midnightblue
        self.question_label = tk.Label(root, text="", font=(font_name, 24, "bold"), wraplength=600,
                                       bg="palevioletred",
                                       fg=question_font_color)  # шрифт, цвет фона и текста
        self.question_label.pack(pady=20, padx=20, fill="x", anchor="center")  # отступ по горизонтали + fill x + anchor

        self.answer_entry = tk.Entry(root, font=(font_name, 20, "bold"), bg="white", fg="darkslategray")  # Шрифт ввода
        self.answer_entry.pack(pady=10, padx=20)

        button_color = question_font_hex  # Цвет для кнопки "Ответить"
        next_button_color = self.lighten_color(button_color, 0.7)  # Цвет для кнопки "Следующий вопрос" - осветленный

        self.submit_button = tk.Button(root, text="Ответить", command=self.submit_answer,
                                       font=(font_name, 16, "bold"), bg=button_color, fg="white")
        self.submit_button.pack(pady=10, padx=20)

        self.next_button = tk.Button(root, text="Следующий вопрос", command=self.next_question,
                                     font=(font_name, 16, "bold"), bg=next_button_color, fg="white")
        self.next_button.pack(pady=10, padx=20)
        self.next_button["state"] = "disabled"  # Отключён по умолчанию

        self.result_label = tk.Label(root, text="", font=(font_name, 16, "bold"), bg="palevioletred",
                                     fg="midnightblue")  # шрифт, цвет фона и текста
        self.result_label.pack(pady=10, padx=20, fill="x", anchor="center")  # отступ по горизонтали + fill x + anchor

        self.display_question()

    """Display the current question"""
    def display_question(self):
        if self.current_question_index < len(self.manager.questions):
            question = self.manager.questions[self.current_question_index]["text"]
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_final_score()

    """Process the user's answer"""
    def submit_answer(self):
        answer = self.answer_entry.get().strip()
        try:
            if not answer:
                raise InvalidAnswerError("Ответ не может быть пустым!")

            correct_answer = self.manager.questions[self.current_question_index]["answer"]
            if answer.lower() == correct_answer.lower():
                self.score += 1
                messagebox.showinfo("Результат", "Правильно!")
            else:
                messagebox.showinfo("Результат", f"Неправильно! Правильный ответ: {correct_answer}")
            self.submit_button["state"] = "disabled"
            self.next_button["state"] = "normal"
        except InvalidAnswerError as e:
            messagebox.showerror("Ошибка", str(e))

    """Move to the next question"""
    def next_question(self):
        self.current_question_index += 1
        self.submit_button["state"] = "normal"
        self.next_button["state"] = "disabled"
        self.display_question()

    """Display the final score of the quiz"""
    def show_final_score(self):
        self.question_label.config(
            text=f"Вы завершили викторину!\nВаш результат: {self.score} из {len(self.manager.questions)}\nТак держать!")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()

    """Lighten a given color by a specified factor"""
    def lighten_color(self, color, factor=0.6):
        """Осветляет цвет."""
        if color.startswith("#"):
            color = color.lstrip("#")
            r, g, b = (int(color[i:i+2], 16) for i in (0, 2, 4))
            r = int(min(255, r + (255 - r) * factor))
            g = int(min(255, g + (255 - g) * factor))
            b = int(min(255, b + (255 - b) * factor))
            return f'#{r:02x}{g:02x}{b:02x}'
        else:
            # Используем метод winfo_rgb для получения RGB значений
            rgb = self.root.winfo_rgb(color)
            r,g,b = (int(c/256) for c in rgb) # делим на 256, чтобы rgb был от 0 до 255
            r = int(min(255, r + (255 - r) * factor))
            g = int(min(255, g + (255 - g) * factor))
            b = int(min(255, b + (255 - b) * factor))
            return f'#{r:02x}{g:02x}{b:02x}'


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()