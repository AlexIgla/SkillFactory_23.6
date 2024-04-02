import telebot


TOKEN = "7169964806:AAFjazC-ArySYWk5PYyn3YQ8RtZ2HFmsdzc"


bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду бота в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = ('Доступные валюты:')
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


bot.polling(none_stop=True)
