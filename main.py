import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize the bot and dispatcher
bot = Bot(token='6029482442:AAGpyt01Y4xXhF6wuT4d6kWAlm-tFjkoDEc')
dispatcher = Dispatcher(bot)

# Define a function for the /start command
@dispatcher.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Hi, I am an echo bot!')

# Define a function for the /help command
@dispatcher.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Send me a message and I will echo it back to you!')

# Define a function for echoing messages
@dispatcher.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dispatcher)
