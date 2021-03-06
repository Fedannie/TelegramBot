import telebot

bot = telebot.TeleBot('1674545727:AAEgn79V1ae8ALH4OA2N5HRb7NV-SkvsTk0')
current_status = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Если хочешь добавить несколько занятий, введи количество занятий, добавив в начало \'+\'\n' +
                          f'Если хочешь отметить несколько занятий как оплаченные, введи количество оплаченных занятий, добавив в начало \'-\'\n' +
                          f'Если увидеть текущий статус, введи команду \'\\status\'')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    global current_status
    courses = int(message.text[1:])
    if message.text[0] == "+":
        current_status += courses
        bot.reply_to(message, f'Добавлено ' + str(courses) + f' занятий')
    elif message.text[0] == "-":
        current_status -= courses
        bot.reply_to(message, f'Оплачено ' + str(courses) + f' занятий')


@bot.message_handler(commands=['status'])
def get_current_status(message):
    if current_status > 0:
        bot.reply_to(message, f'У тебя ' + str(current_status) + f' неоплаченных занятий')
    elif current_status == 0:
        bot.reply_to(message, f'У тебя нет неоплаченных занятий')
    else:
        bot.reply_to(message, f'У тебя ' + str(-current_status) + f' переплаченных занятий')


bot.polling(none_stop=True)