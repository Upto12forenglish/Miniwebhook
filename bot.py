from bottle import run, post, request as bottle_request  # <--- we add bottle request
import telebot

# Replace 'YOUR_TOKEN' with your actual Telegram Bot token
bot = telebot.TeleBot('6092786649:AAGsiM_0resGLglZTtRc-9iJtod2TagIhNE')

def change_text_message(text):
    # Custom function to manipulate the text (e.g., reverse it)
    return text[::-1]

@post('/')  # our python function based endpoint
def main():
    data = bottle_request.json  # <--- extract all request data
    print(data)

    # Process the message (you may include additional logic here)
    if 'message' in data:
        message = data['message']
        print('Message: ', message)
        # Extract message text
        message_text = data['message']['text']
        print('Message text: ', message_text)
        # Chat ID from the received message
        chat_id = data['message']['chat']['id']
        print('Chat id: ', chat_id)

        # # Change the message text (e.g., reverse it)
        # message_text = change_text_message(message_text)

        # # Send the modified message back to the chat
        bot.send_message(chat_id, message_text)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)