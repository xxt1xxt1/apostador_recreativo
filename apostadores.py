import requests
import time
import telepot
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg) 
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, teste(msg))

def teste(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    telegran = msg['text']
    mensagem = '/start'
    if mensagem == telegran:
        return "seu Bot está funcionando"

TOKEN = "1433851093:AAHJCjOYyqC_t1XBkNyqZAgWx8YuK8f96ZM"
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('processando...')

while 1:
    time.sleep(10)