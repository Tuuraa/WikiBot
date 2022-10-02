import telebot, wikipedia

if __name__ == '__main__':
    _url = "5766353345:AAEzoDnO55eLxQ82zb0tRHrAVLx16bYc69E"
    bot = telebot.TeleBot(_url)

    wikipedia.set_lang("ru")


@bot.message_handler(commands=["start"])
def start(m, res=False):

    print("Пользователь ввел: " + m.text)

    bot.send_message(
        m.chat.id,
        'Я на связи. Отправь название, имя или что-то подобное '
        'о чем хочешь найти информацию или биографию (если это человек). Например напиши "Путин", если не боишься)))')



@bot.message_handler(content_types=["text"])
def handle_text(update):

    chatid = update.chat.id
    print("Пользователь ввел: " + update.text + ". ID чата : " + str(chatid))

    try:
        person = wikipedia.suggest(update.text)
        lists = wikipedia.search(update.text)

        if update.text.lower().find("артур") != -1:
            bot.send_message(
                chat_id=chatid,
                text="Он тигр")
            return

        elif update.text.lower() == "путин":
            bot.send_message(
                chat_id=chatid,
                text="А ты храбрец))")

            bot.send_message(
                chat_id=chatid,
                text=wikipedia.summary(person))
            return

            bot.send_message(
                chat_id=chatid,
                text=wikipedia.summary(lists[0]))
            return

        else:
            bot.send_message(
                chat_id=chatid,
                text="Неверно или недоконца введено имя, или вовсе нет такого предмета (человека)")
    except:
        bot.send_message(chat_id=chatid, text="Попробуйте еще раз")


bot.polling(none_stop=True, interval=0)

