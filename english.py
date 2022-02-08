import asyncio
import logging 

from aiogram import Bot, Dispatcher, executor, types

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

@dp.callback_query_handler(lambda c: c.data == 'presentsimple')
async def process_callback_btn27(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id)
		await bot.send_message(callback_query.from_user.id, "I usually (go) to school.", reply_markup = nav.otherMenu7)

@dp.callback_query_handler(lambda c: c.data == '1')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
		await bot.send_message(callback_query.from_user.id, "They (visit) us often.", reply_markup = nav.otherMenu8)

@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. goes 
Используется для 
he, she, it""")

@dp.callback_query_handler(lambda c: c.data == '3')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. going 
Форма Present Continuous""")

@dp.callback_query_handler(lambda c: c.data == '4')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. visits 
Используется для 
he, she, it""")

@dp.callback_query_handler(lambda c: c.data == '5')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
		await bot.send_message(callback_query.from_user.id, "You (play) basketball once a week.", reply_markup = nav.otherMenu9)

@dp.callback_query_handler(lambda c: c.data == '6')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. visiting 
Форма Present Continuous""")

@dp.callback_query_handler(lambda c: c.data == '7')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. plays 
Используется для 
he, she, it""")

@dp.callback_query_handler(lambda c: c.data == '8')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. playing 
Форма Present Continuous""")

@dp.callback_query_handler(lambda c: c.data == '9')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
		await bot.send_message(callback_query.from_user.id, "Tom (work) every day.", reply_markup = nav.otherMenu10)

@dp.callback_query_handler(lambda c: c.data == '10')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
		await bot.send_message(callback_query.from_user.id, "He always (tell) us funny stories.", reply_markup = nav.otherMenu11)

@dp.callback_query_handler(lambda c: c.data == '11')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. working 
Форма Present Continuous""")

@dp.callback_query_handler(lambda c: c.data == '12')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. work 
Используется для 
he, she, it""")

@dp.callback_query_handler(lambda c: c.data == '13')
async def process_callback_btn28(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
		await bot.send_message(callback_query.from_user.id, """Поздравляю!
Ты прошел тест по Present Simple""")

@dp.callback_query_handler(lambda c: c.data == '14')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. telling 
Форма Present Continuous""")

@dp.callback_query_handler(lambda c: c.data == '15')
async def process_callback_btn29(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "❌НЕВЕРНЫЙ ОТВЕТ❌")
		await bot.send_message(callback_query.from_user.id, """❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. tell 
Используется для 
I, we, you, they""")

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
