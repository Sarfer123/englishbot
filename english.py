import asyncio
import logging 

from aiogram import Bot, Dispatcher, executor, types

from random import choice

import markup as nav

TOKEN = '5166630869:AAGl1Maq4ELZuOszKi828IHPDPLTuUWnRcI'
CHANNEL_ID = "@englishlanguageforlife"
NOTSUB_MESSAGE = """Подпишись на канал✔️
Чтобы начать учить английский🇬🇧"""

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

def check_sub_channel(chat_member):
	print(chat_member['status'])
	if chat_member['status'] != 'left':
		return True
	else:
		return False

@dp.message_handler(commands = ['start'])
async def command_start(message: types.Message):
	if check_sub_channel(await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = message.from_user.id)):
		await bot.send_message(message.from_user.id, """Привет, {0.first_name}👋 
Выбери тему:""".format(message.from_user), reply_markup = nav.mainMenu)
	else: 
		await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup = nav.otherMenu5)

@dp.callback_query_handler(lambda c: c.data == 'subchanneldone')
async def process_callback_btn24(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, """Привет👋 
Выбери тему:""", reply_markup = nav.mainMenu)
questions = {I usually (go) to school. : [nav.otherMenu7]
@dp.message_handler()
async def bot_message(message: types.Message):
	if message.text == '🖋 Грамматика':
		await bot.send_message(message.from_user.id, '🖋 Грамматика', reply_markup = nav.otherMenu)

	elif message.text == '📚 Лексика':
		await bot.send_message(message.from_user.id, '📚 Лексика', reply_markup = nav.otherMenu1)
	
	elif message.text == '🌐 Будущие обновления':
		await bot.send_message(message.from_user.id, """Скоро будет добавлен
герундий и пассивный залог""")

	elif message.text == '✅ Present':
		await bot.send_message(message.from_user.id, '✅ Present', reply_markup = nav.otherMenu2)

	elif message.text == '✅ Past':
		await bot.send_message(message.from_user.id, '✅ Past', reply_markup = nav.otherMenu3)

	elif message.text == '✅ Future':
		await bot.send_message(message.from_user.id, '✅ Future', reply_markup = nav.otherMenu4)

	elif message.text == '📖 Существительные':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Top-100-CHasto-ispolzuemyh-slov-02-06")

	elif message.text == '📖 Прилагательные':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Samye-chastye-prilagatelnye-02-06")

	elif message.text == '📖 Глаголы':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Samye-chastye-glagoly-v-anglijskom-yazyke-02-06")

	elif message.text == '✅ Present Simple':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Simple-02-06", reply_markup = nav.otherMenu6)

	elif message.text == '✅ Present Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Continuous-02-06")

	elif message.text == '✅ Present Perfect':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Perfect-02-06")

	elif message.text == '✅ Present Perfect Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Perfect-Continuous-02-06")

	elif message.text == '✅ Past Simple':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Past-Simple-02-06")

	elif message.text == '✅ Past Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Past-Continuous-02-06")

	elif message.text == '✅ Past Perfect':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Past-Perfect-02-06")

	elif message.text == '✅ Past Perfect Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Past-Perfect-Continuous-02-06")

	elif message.text == '✅ Future Simple':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Future-Simple-02-06")

	elif message.text == '✅ Future Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Future-Continuous-02-06")

	elif message.text == '✅ Future Perfect':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Future-Perfect-02-06")

	elif message.text == '✅ Future Perfect Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Future-Perfect-Continuous-02-06")

	elif message.text == '🔙Назад':
		await bot.send_message(message.from_user.id, '🔙Назад', reply_markup = nav.mainMenu)
	
	elif message.text == '🔙Выбор времени':
		await bot.send_message(message.from_user.id, '🔙Выбор времени', reply_markup = nav.otherMenu)

	elif message.text == 'I usually (go) to school.':
		await bot.send_message(message.from_user.id, "Вариант ответа:", reply_markup = nav.otherMenu7)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)