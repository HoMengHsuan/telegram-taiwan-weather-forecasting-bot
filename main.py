from telegram.ext import Updater, CommandHandler
from crawlerweather import *

def weather(bot, update):
    text = update.message.text[9:].replace('\n', ' ')
    update.message.reply_text(text + "天氣如下：")
    update.message.reply_text(parse_mode='HTML', text='<pre>'+the_weather(text)+'</pre>')

updater = Updater('Please Paste Your Token Here')

updater.dispatcher.add_handler(CommandHandler("weather", weather))

updater.start_polling()
updater.idle()
