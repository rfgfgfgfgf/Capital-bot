import telebot
from config import TOKEN
from logic import GeoQuiz

bot = telebot.TeleBot(TOKEN) 
geo_quiz = GeoQuiz() 

@bot.message_handler(commands=['quiz'])
def handle_quiz(message):
    """Начинает викторину"""
    question = geo_quiz.start_quiz(message.chat.id)
    bot.send_message(message.chat.id, question if question else "Вопросы закончились!")

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    """Останавливает викторину"""
    result = geo_quiz.stop_quiz(message.chat.id)
    bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обрабатывает ответы пользователя"""
    result = geo_quiz.check_answer(message.chat.id, message.text)
    bot.send_message(message.chat.id, result)
    
    if "Правильно!" in result or "Неправильно." in result:
        next_question = geo_quiz.get_next_question(message.chat.id)
        bot.send_message(message.chat.id, next_question if next_question else "Викторина завершена!")

if __name__ == "__main__":
    bot.polling(none_stop=True)


