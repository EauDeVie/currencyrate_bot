import telebot
import config
import pars_val

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Доллар США', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Евро', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Фунт Стерлингов', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Китайский Юань', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Швейцарский Франк', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='Турецкая Лира', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='Японская Йена', callback_data=7))
    bot.send_message(message.chat.id, text="Выберите валюту, по которой хотите узнать курс", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за выбор бота')
    answer = ''
    if call.data == '1':
        answer = 'Доллар США   ' + pars_val.dollar + '   за одну условную единицу в рублях'
    elif call.data == '2':
        answer = 'Евро   ' + pars_val.euro + '   за одну условную единицу в рублях'
    elif call.data == '3':
        answer = 'Фунт Стерлингов   ' + pars_val.funt + '   за одну условную единицу в рублях'
    elif call.data == '4':
        answer = 'Китайский Юань   ' + pars_val.kit + '   за одну условную единицу в рублях'
    elif call.data == '5':
        answer = 'Швейцарский франк   ' + pars_val.frank + '   за одну условную единицу в рублях'
    elif call.data == '6':
        answer = 'Турецкая лира   ' + pars_val.lira + '   за одну условную единицу в рублях'
    elif call.data == '7':
        answer = 'Японская йена   ' + pars_val.yena + '   за одну условную единицу в рублях'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.infinity_polling()


