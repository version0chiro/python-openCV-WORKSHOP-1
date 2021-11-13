from telegram.ext import CommandHandler
import logging
from telegram.ext import Updater
import telegram


bot = telegram.Bot(token='2022203625:AAHR-k13FXDW8IdKIOZCZf-eOxC5Dd3n_sI')



bot.send_message(chat_id=1829778200, text="!!")

updater = Updater(
    token='2022203625:AAHR-k13FXDW8IdKIOZCZf-eOxC5Dd3n_sI', use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot x2!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
