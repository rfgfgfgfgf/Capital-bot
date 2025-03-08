import random

class GeoQuiz:
    def __init__(self):
        self.questions = [
            {"question": "Какая столица Франции?", "answer": "Париж"},
            {"question": "Какая столица Германии?", "answer": "Берлин"},
            {"question": "Какая столица Италии?", "answer": "Рим"},
            {"question": "Какая столица Азербайджана?", "answer": "Баку"},
            {"question": "Какая столица Турции?", "answer": "Анкара"},
            {"question": "Какая столица России?", "answer": "Москва"}
        ]
        self.user_scores = {}  
        self.current_questions = {}  

    def start_quiz(self, user_id):
        """Начинает викторину и отправляет первый вопрос"""
        self.user_scores[user_id] = 0
        return self.get_next_question(user_id)

    def get_next_question(self, user_id):
        """Выбирает случайный вопрос"""
        if not self.questions:
            return "Вопросы закончились!"  

        question_data = random.choice(self.questions)
        self.current_questions[user_id] = question_data
        return question_data["question"]

    def check_answer(self, user_id, answer):
        """Проверяет ответ пользователя"""
        if user_id not in self.current_questions:
            return "Напишите /quiz, чтобы начать викторину."

        correct_answer = self.current_questions[user_id]["answer"]
        if answer.lower().strip() == correct_answer.lower():
            self.user_scores[user_id] += 1
            response = f"Правильно! Очки: {self.user_scores[user_id]}"
        else:
            response = f"Неправильно. Правильный ответ: {correct_answer}"

        return response

    def stop_quiz(self, user_id):
        """Останавливает викторину для пользователя"""
        if user_id in self.user_scores:
            score = self.user_scores.pop(user_id)
            self.current_questions.pop(user_id, None)
            return f"Вы завершили квиз. Ваш итоговый счёт: {score}"
        return "Вы ещё не начинали квиз. Напишите /quiz, чтобы начать!"
