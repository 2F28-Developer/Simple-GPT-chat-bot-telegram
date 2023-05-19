from telegram.ext import Updater, MessageHandler, Filters
import openai

openai.api_key = ''

telegram_token = ''

def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=3900,
        n=1,
        stop=None,
        temperature=0.7,
    )
    bot_message = response.choices[0].text.strip()[:4000]

    if len(bot_message) > 4000:
        bot_message = bot_message[:4000]

    bot_message = bot_message.strip()

    return bot_message


def handle_message(update, context):
    user_message = update.message.text
    bot_message = generate_response(user_message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_message)

def main():
    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()