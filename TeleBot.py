import telebot


TOKEN = "7169964806:AAFjazC-ArySYWk5PYyn3YQ8RtZ2HFmsdzc"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')
keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу, введите команду бота в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>')
    bot.reply_to(message, text)


bot.polling(none_stop=True)
