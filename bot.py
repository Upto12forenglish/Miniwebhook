import telebot
from flask import Flask, request

token = '6092786649:AAGsiM_0resGLglZTtRc-9iJtod2TagIhNE'
secret = 'uigwd98w90dw099dwer'
url = 'https://ut12-miniwebhook.streamlit.app/' + secret

bot = telebot.TeleBot(token, threaded = False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)
@app.route('/'+secret, methods=['Post'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, Welcome to the bot!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'How can I help you?')

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
