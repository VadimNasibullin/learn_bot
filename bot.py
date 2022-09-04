import logging
from turtle import update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


'''PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}'''

def greet_user(update, context):
    print('Вызван/start')
   
    update.message.reply_text('Здравствуй, пользователь! Ты нажал на кнопку "start"!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True) #при использовании прокси добавить reqwest_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot startoval') # Написал на англ., потому что не читает кирилицу.
    mybot.start_polling() 
    mybot.idle()

main()      
