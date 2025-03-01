import telebot
from config import TOKEN, DATABASE
from logic import DB_Manager

bot = telebot.TeleBot(TOKEN)
manager = DB_Manager(DATABASE)  

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может показывать столицы стран. Напиши /help для списка команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды: /capital - показать столицу указанной страны")

@bot.message_handler(commands=['capital'])
def handle_capital(message):
    country_name = ' '.join(message.text.split()[1:])  
    capital = manager.get_capital(country_name)
    
    if capital:
        bot.send_message(message.chat.id, f'Столица {country_name}: {capital}')
    else:
        bot.send_message(message.chat.id, 'Такой страны нет в базе данных или допущена ошибка в названии.')

# Запуск бота
if __name__ == "__main__":
    bot.polling()
