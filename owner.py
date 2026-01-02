import telebot

#bot api token
teleapi="8573842944:AAGS_zH02KrY520almaXu0oID_0WthaiFgU"
#connect the tele sever
rio=telebot.TeleBot(teleapi)
web="animerio.com"
@rio.message_handler(commands=['start'])
def wellcome_message(message):
    name = message.from_user.first_name
    rio.reply_to(message,f"Hey {name}....\nI am Rio If You Access Me Please vsit.... \n{web}")
@rio.message_handler(commands=['anime'])
def send_msg(message):
    rio.copy_message(
        chat_id=message.chat.id,
        from_chat_id="@animeriochanel",
        message_id=8
    )


#bot running pool
rio.infinity_polling()
