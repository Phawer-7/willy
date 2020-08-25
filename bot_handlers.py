from bot import *
import db
import keyboards
import horoscope_parser

@bot.message_handler(commands=["developer"])
def who_developer(message):
    bot.send_message(message.chat.id, "Разработчик ботов - t.me/mrfire7")

@bot.message_handler(commands=["channel"])
def who_developer(message):
    bot.send_message(message.chat.id, "Наш канал t.me/Horoskope_Willy")

@bot.message_handler(commands=["start"])
def start_handler(message):
    if not db.Users().exists(message.chat.id):
        db.Users().add(message.chat.id, message.from_user.username)
    bot.send_message(message.chat.id, "Выберите знак зодиака", reply_markup=keyboards.inline_horoscope)
    db.Users().update_interface_state(message.chat.id, 0)


@bot.message_handler(commands=["post"], func=lambda message: message.chat.id == config.BOT_ADMIN_ID)
def post_handler(message):
    msg = bot.send_message(message.chat.id, "Что отправлять?")
    bot.register_next_step_handler(msg, send_post)


@bot.callback_query_handler(func=lambda callback: callback.data in keyboards.HOROSCOPE.values())
def callback_handler(callback):
    bot.delete_message(callback.from_user.id, callback.message.message_id)
    bot.send_message(callback.from_user.id, horoscope_parser.get_today(callback.data),
                     reply_markup=keyboards.inline_horoscope)


def send_post(message):
    for user in db.Users():
        try:
            bot.forward_message(user.user_id, message.chat.id, message.message_id)
        except:
            bot.send_message(message.chat.id, f"Не удалось отправить пост пользователю @{user.user_name}")

@bot.message_handler(content_types=['text'])
def spam(message):
    bot.send_message(message.chat.id,  "Шо? Доступные команды: /start , /developer и /channel ") 

def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
