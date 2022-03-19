from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Defaults
from telegram import Update, ParseMode, MessageEntity
from telegram.ext import CallbackContext
import logging


def main():

    TOKEN = "5206805580:AAG_9NXRkinVcLS0PyOnv3ksjvToRyAWIF0"

    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

    defaults = Defaults(parse_mode=ParseMode.HTML)
    updater = Updater(token=TOKEN, defaults=defaults)
    dispatcher = updater.dispatcher

    def photo_or_video(update, context):
        update.message.reply_text('Классное фото. Или это видео??')

    def audio(update, context):
        update.message.reply_text('Послушаю позже...')

    def forwarded_ph_or_vid(update, context):
        update.message.reply_text(f'<b>Получил от тебя либо фото, либо видео. Чего ты добиваешься?</b>')

    def link(update, context):
        update.message.reply_text('Твоё сообщение содержит ссылку.')

    def number(update, context):
        try:
            num = float(context.args[1])
            context.user_data[context.args[0]] = num
        except:
            update.message.reply_text('Корректно введите ключ и число!')

    def summarize(update, context):
        try:
            a = context.user_data[context.args[0]]
            b = context.user_data[context.args[1]]
            update.message.reply_text(f'Сумма: {a + b}')
        except:
            update.message.reply_text('Ошибка!')

    dispatcher.add_handler(MessageHandler(~Filters.forwarded & (Filters.photo | Filters.video), photo_or_video))
    dispatcher.add_handler(MessageHandler(Filters.audio, audio))
    dispatcher.add_handler(MessageHandler(Filters.forwarded & (Filters.photo | Filters.video), forwarded_ph_or_vid))
    dispatcher.add_handler(MessageHandler(Filters.entity(MessageEntity.URL), link))

    dispatcher.add_handler(CommandHandler('number', number))  # /number [key1] [x]
    dispatcher.add_handler(CommandHandler('sum', summarize))  # /sum [key1] [key2]

    updater.start_polling()


if __name__ == "__main__":
    main()

