import telebot
from telebot import types
import mat_generator as mg

bot = telebot.TeleBot('5852065316:AAGml8RIsPfrbRMHZ4tz9ZY2Tde7DCXVDF0')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Девочек")
    item2 = types.KeyboardButton("Мальчиков")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Кого обзываем?', reply_markup=markup)


@bot.message_handler()
def text(message):
    print(message)
    response = 'Нахуй я кнопки делал? Ты можешь на них тыкнуть?'
    request = message.text

    if request == 'Девочек':
        response = mg.generate(False)
    elif request == 'Мальчиков':
        response = mg.generate(True)

    bot.send_message(message.chat.id, response, parse_mode='html')


bot.polling(none_stop=True)
