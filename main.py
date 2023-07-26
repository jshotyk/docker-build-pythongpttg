import logging
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# Замените 'YOUR_TELEGRAM_TOKEN' на ваш токен бота
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'

# Замените 'YOUR_OPENAI_API_KEY' на ваш API ключ от OpenAI
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

# Включаем журналирование для отладки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Устанавливаем API ключ для OpenAI
openai.api_key = OPENAI_API_KEY

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот, который может общаться с чат GPT. Просто отправьте мне ваш вопрос или сообщение.")

# Функция для обработки входящих сообщений
def handle_message(update: Update, context: CallbackContext):
    # Получаем текст сообщения от пользователя
    user_message = update.message.text

    # Отправляем текст сообщения на сервер GPT для получения ответа
    response = openai.Completion.create(
        engine="davinci",  # Выбираем GPT-3.5 engine (davinci)
        prompt=user_message,  # Вопрос от пользователя
        max_tokens=150,  # Максимальное количество токенов в ответе
        temperature=0.7,  # Коэффициент "температуры" для разнообразия ответов (меньше - более точные, больше - более креативные)
    )

    # Извлекаем ответ из полученного объекта ответа
    bot_response = response.choices[0].text.strip()

    # Отправляем ответ пользователю
    update.message.reply_text(bot_response)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Добавляем обработчик сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
