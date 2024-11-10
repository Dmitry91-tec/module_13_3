from aiogram import Bot, Dispatcher, executor, types            #Импортируем сущность бота, диспетчера, «executor», типы
from aiogram.contrib.fsm_storage.memory import MemoryStorage    #блока работы с памятью
import asyncio

api = ""
bot = Bot(token = api)                                  #Дальше понадобится api ключ, который мы получили в «BotFather». Так же переменная бота, она будет хранить объект бота, «token» будет равен вписанному ключу
dp = Dispatcher(bot, storage = MemoryStorage())          #Понадобится «Dispatcher», который будет объектом «Dispatcher», у него будет наш бот в качестве аргументов. В качестве «Storage» будет «MemoryStorage»

# @dp.message_handler(text = ["Urban","ff"])              #«text» — это текст
# async def start_message(message):
#     print("Urban message!")
#     await message.answer("Urban message!")               #Сделаем так, чтобы на сообщение типа «urban» мы отвечали неким сообщением

@dp.message_handler(commands = ["Start"])              #«commands» — это команды, начинающиеся с "/"
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()                                       # декоратор, который позволяет работать с сообщениями
async def all_message(message):                              #функцию, которая будет обрабатывать все сообщения «all_message»
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")                       #эхо-ответы

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)          #Запускаем «executor», у которого есть функция «start_polling». Объясняем, через кого ему запускаться

