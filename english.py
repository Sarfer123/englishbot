import asyncio
import logging 
import markup as nav

from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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

@dp.callback_query_handler(lambda c: c.data == '28')
async def process_callback_btn28(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "They (visit) us often.", reply_markup = nav.otherMenu8)

@dp.callback_query_handler(lambda c: c.data == '32')
async def process_callback_btn32(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "You (play) basketball once a week.", reply_markup = nav.otherMenu9)

@dp.callback_query_handler(lambda c: c.data == '36')
async def process_callback_btn36(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "Tom (work) every day.", reply_markup = nav.otherMenu10)

@dp.callback_query_handler(lambda c: c.data == '37')
async def process_callback_btn37(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "He always (tell) us funny stories.", reply_markup = nav.otherMenu11)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('29'))
async def process_callback_btn29(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. goes 
Используется для 
he, she, it""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('30'))
async def process_callback_btn30(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. going 
Форма Present Continuous""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('31'))
async def process_callback_btn31(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. visits 
Используется для 
he, she, it""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('33'))
async def process_callback_btn33(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. visiting 
Форма Present Continuous""",
            show_alert=True)



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('34'))
async def process_callback_btn34(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. plays 
Используется для 
he, she, it""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('35'))
async def process_callback_btn35(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. playing 
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('38'))
async def process_callback_btn38(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. working 
Форма Present Continuous""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('39'))
async def process_callback_btn39(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. work 
Используется для 
he, she, it""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('40'))
async def process_callback_btn40(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""Поздравляю!
Ты прошел тест по Present Simple🎉
Выбери следующий урок😉""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('41'))
async def process_callback_btn41(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. telling
Форма Present Continuous""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('42'))
async def process_callback_btn42(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. tell 
Используется для
I, we, you, they""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'presentcontinuous')
async def process_callback_btn58(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id)
		await bot.send_message(callback_query.from_user.id, "His dad and brother (cycle) to the shops.", reply_markup = nav.otherMenu12)

@dp.callback_query_handler(lambda c: c.data == '43')
async def process_callback_btn43(callback_query: types.CallbackQuery):
		await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
		await bot.send_message(callback_query.from_user.id, "We (not travel) in Japan.", reply_markup = nav.otherMenu13)

@dp.callback_query_handler(lambda c: c.data == '46')
async def process_callback_btn46(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "I (sunbathe) on the beach.", reply_markup = nav.otherMenu14)

@dp.callback_query_handler(lambda c: c.data == '50')
async def process_callback_btn50(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "She (not watch) TV.", reply_markup = nav.otherMenu15)

@dp.callback_query_handler(lambda c: c.data == '52')
async def process_callback_btn52(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "They (not swim) in the sea.", reply_markup = nav.otherMenu16)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('55'))
async def process_callback_btn55(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""Поздравляю!
Ты прошел тест по Present Simple🎉
Выбери следующий урок😉""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('44'))
async def process_callback_btn44(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. is cycling
Неправильный вспомогательнный глагол
Используется для he, she, it""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('45'))
async def process_callback_btn45(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. cycles
Форма Present Simple""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('47'))
async def process_callback_btn47(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. doesn't travel
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('48'))
async def process_callback_btn48(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. isn't travelling
Неправильный вспомогательнный глагол
Используется для he, she, it""",
            show_alert=True)



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('49'))
async def process_callback_btn49(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. does sunbathe
Форма Present Simple""",
            show_alert=True)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('51'))
async def process_callback_btn51(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. sunbathing
Нет вспомогательного глагола
(am, is, are)""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('53'))
async def process_callback_btn53(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. doesn't watch
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('54'))
async def process_callback_btn54(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. is watching
Используется для утвердительных предложений """,
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('56'))
async def process_callback_btn53(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. doesn't swim
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('57'))
async def process_callback_btn54(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. is swimming
Используется для утвердительных предложений """,
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'presentperfect')
async def process_callback_btn59(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "(you/speak/?) to the poor soul?", reply_markup = nav.otherMenu19)

@dp.callback_query_handler(lambda c: c.data == '61')
async def process_callback_btn61(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "I (not/do) very much yet.", reply_markup = nav.otherMenu20)

@dp.callback_query_handler(lambda c: c.data == '63')
async def process_callback_btn63(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "One sight more, and we (do).", reply_markup = nav.otherMenu21)

@dp.callback_query_handler(lambda c: c.data == '68')
async def process_callback_btn68(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "He (tell) her things about me.", reply_markup = nav.otherMenu22)

@dp.callback_query_handler(lambda c: c.data == '70')
async def process_callback_btn70(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "This is the first we (hear) of it.", reply_markup = nav.otherMenu23)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('74'))
async def process_callback_btn74(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""Поздравляю!
Ты прошел тест по Present Perfect🎉
Выбери следующий урок😉""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('60'))
async def process_callback_btn60(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. Do you speak
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('62'))
async def process_callback_btn62(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. Are you speaking
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('64'))
async def process_callback_btn64(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. doesn't do
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('65'))
async def process_callback_btn65(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. aren't doing
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('66'))
async def process_callback_btn66(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. does do
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('67'))
async def process_callback_btn67(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. is doing
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('69'))
async def process_callback_btn69(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. have told
Неправильный вспомогательнный глагол
Используется для you, we, they""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('71'))
async def process_callback_btn71(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. are telling
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('72'))
async def process_callback_btn72(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. has been heard
Форма Present Perfect Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('73'))
async def process_callback_btn73(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. has heard
Неправильный вспомогательнный глагол
Используется для he, she, it""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'presentperfectcontinuous')
async def process_callback_btn58(callback_query: types.CallbackQuery):
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, "We (to paint) the fence since morning.", reply_markup = nav.otherMenu25)

@dp.callback_query_handler(lambda c: c.data == '78')
async def process_callback_btn78(callback_query: types.CallbackQuery):
                await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
                await bot.send_message(callback_query.from_user.id, "She (to watch) this film for 2 hours.", reply_markup = nav.otherMenu26)

@dp.callback_query_handler(lambda c: c.data == '80')
async def process_callback_btn80(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "My father (to do) shopping since 3 p.m.", reply_markup = nav.otherMenu27)

@dp.callback_query_handler(lambda c: c.data == '83')
async def process_callback_btn83(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "I (to learn) Japanese for 5 years.", reply_markup = nav.otherMenu28)

@dp.callback_query_handler(lambda c: c.data == '87')
async def process_callback_btn87(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "The cat (to chase) a mouse since afternoon.", reply_markup = nav.otherMenu29)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('88'))
async def process_callback_btn88(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""Поздравляю!
Ты прошел тест по Present Simple🎉
Выбери следующий урок😉""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('76'))
async def process_callback_btn76(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. painted
Нет вспомогательных глаголов""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('77'))
async def process_callback_btn77(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. have painted
Форма Present Perfect""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('79'))
async def process_callback_btn79(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. is watching
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('81'))
async def process_callback_btn81(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. has watching
Нет вспомогательного глагола been""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('82'))
async def process_callback_btn82(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. have been done
Неправильная форма глагола""",
            show_alert=True)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('84'))
async def process_callback_btn84(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. have been doing
Неправильный вспомогательный глагол
Используется для they, you, we""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('85'))
async def process_callback_btn85(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. have learned
Нет вспомогательного глагола been""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('86'))
async def process_callback_btn86(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. has learning
Вспомогательный глагол используется для he, she, it
Нет вспомогательного глагола been""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('89'))
async def process_callback_btn89(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. has chased
Форма Present Perfect""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('90'))
async def process_callback_btn90(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. have been chasing
Неправильный вспомогательный глагол
Используется для they, you, we""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'pastsimple')
async def process_callback_btn166(callback_query: types.CallbackQuery):
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, "I (not / drink) any beer last night.", reply_markup = nav.otherMenu30)

@dp.callback_query_handler(lambda c: c.data == '91')
async def process_callback_btn91(callback_query: types.CallbackQuery):
                await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
                await bot.send_message(callback_query.from_user.id, "She (get on) the bus in the centre of the city.", reply_markup = nav.otherMenu31)

@dp.callback_query_handler(lambda c: c.data == '95')
async def process_callback_btn95(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "What time did (he / get up) yesterday?", reply_markup = nav.otherMenu32)

@dp.callback_query_handler(lambda c: c.data == '99')
async def process_callback_btn99(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "Where did (you / get off) the train?", reply_markup = nav.otherMenu33)

@dp.callback_query_handler(lambda c: c.data == '102')
async def process_callback_btn102(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "I (not / change) trains at Victoria.", reply_markup = nav.otherMenu34)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('103'))
async def process_callback_btn103(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""Поздравляю!
Ты прошел тест по Past Simple🎉
Выбери следующий урок😉""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('92'))
async def process_callback_btn92(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. don't drink
Форма Present Simple""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('93'))
async def process_callback_btn93(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. haven't drunk
Форма Present Perfect""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('94'))
async def process_callback_btn94(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. get on
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('96'))
async def process_callback_btn96(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. is getting on
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('97'))
async def process_callback_btn97(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. have got up
Форма Present Perfect""",
            show_alert=True)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('98'))
async def process_callback_btn98(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. got up
Неправильная форма
(обратите внимание на did)""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('100'))
async def process_callback_btn100(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. got off
Неправильная форма
(обратите внимание на did)""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('101'))
async def process_callback_btn101(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. are getting of
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('104'))
async def process_callback_btn104(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. haven't changed
Форма Present Perfect""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('105'))
async def process_callback_btn105(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. don't changed
Форма Present Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'pastcontinuous')
async def process_callback_btn166(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "The poor woman (shake) her head.", reply_markup = nav.otherMenu35)

@dp.callback_query_handler(lambda c: c.data == '107')
async def process_callback_btn107(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "The next moment he (rise) in the air.", reply_markup = nav.otherMenu36)

@dp.callback_query_handler(lambda c: c.data == '111')
async def process_callback_btn111(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "It seemed to him that he (not/really/exist) but only seeming to exist.", reply_markup = nav.otherMenu37)

@dp.callback_query_handler(lambda c: c.data == '112')
async def process_callback_btn112(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "I (take) it for my blood.", reply_markup = nav.otherMenu38)

@dp.callback_query_handler(lambda c: c.data == '116')
async def process_callback_btn116(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id, text = "✅ПРАВИЛЬНЫЙ ОТВЕТ✅")
        await bot.send_message(callback_query.from_user.id, "He (not/look) for any one.", reply_markup = nav.otherMenu39)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('120'))
async def process_callback_btn120(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""Поздравляю!
Ты прошел тест по Past Continuous🎉
Выбери следующий урок😉""",
            show_alert=True)                                                                                                                                                           

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('106'))
async def process_callback_btn106(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. shaked
Форма Past Simple""",
            show_alert=True)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('108'))
async def process_callback_btn108(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. has been shaking
Форма Present Perfect Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('109'))
async def process_callback_btn109(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. is rising
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('110'))
async def process_callback_btn110(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. has been rising
Форма Present Perfect Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('113'))
async def process_callback_btn113(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. has been really existing
Форма Present Perfect Continuous""",
            show_alert=True)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('114'))
async def process_callback_btn114(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. is really existing
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('115'))
async def process_callback_btn115(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

1. took
Форма Past Simple""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('117'))
async def process_callback_btn117(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. has been taking
Форма Present Perfect Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('118'))
async def process_callback_btn118(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

2. isn't looking
Форма Present Continuous""",
            show_alert=True)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('119'))
async def process_callback_btn119(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text="""❌ПОПРОБУЙ ЕЩЕ РАЗ❌

Объяснение неправильного ответа:

3. hasn't been looking
Форма Present Perfect Continuous""",
            show_alert=True)

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
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Continuous-02-06", reply_markup = nav.otherMenu17)

	elif message.text == '✅ Present Perfect':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Perfect-02-06", reply_markup = nav.otherMenu18)

	elif message.text == '✅ Present Perfect Continuous':
		await bot.send_message(message.from_user.id, "https://telegra.ph/Present-Perfect-Continuous-02-06", reply_markup = nav.otherMenu24)

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
