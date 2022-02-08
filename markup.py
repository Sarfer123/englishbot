from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn3 = KeyboardButton('🔙Назад')

btn25 = KeyboardButton('🔙Выбор времени')

btn1 = KeyboardButton('🖋 Грамматика')
btn2 = KeyboardButton('📚 Лексика')
btn22 = KeyboardButton('🌐 Будущие обновления')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn1, btn2, btn22)

btn4 = KeyboardButton('✅ Present')
btn5 = KeyboardButton('✅ Past')
btn6 = KeyboardButton('✅ Future')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn4, btn5, btn6, btn3)

btn7 = KeyboardButton('📖 Существительные')
btn8 = KeyboardButton('📖 Прилагательные')
btn9 = KeyboardButton('📖 Глаголы')
otherMenu1 = ReplyKeyboardMarkup(resize_keyboard = True).add(btn7, btn8, btn9, btn3)

btn10 = KeyboardButton('✅ Present Simple')
btn11 = KeyboardButton('✅ Present Continuous')
btn12 = KeyboardButton('✅ Present Perfect')
btn13 = KeyboardButton('✅ Present Perfect Continuous')
otherMenu2 = ReplyKeyboardMarkup(resize_keyboard = True).add(btn10, btn11, btn12, btn13, btn25)

btn14 = KeyboardButton('✅ Past Simple')
btn15 = KeyboardButton('✅ Past Continuous')
btn16 = KeyboardButton('✅ Past Perfect')
btn17 = KeyboardButton('✅ Past Perfect Continuous')
otherMenu3 = ReplyKeyboardMarkup(resize_keyboard = True).add(btn14, btn15, btn16, btn17, btn25)

btn18 = KeyboardButton('✅ Future Simple')
btn19 = KeyboardButton('✅ Future Continuous')
btn20 = KeyboardButton('✅ Future Perfect')
btn21 = KeyboardButton('✅ Future Perfect Continuous')
otherMenu4 = ReplyKeyboardMarkup(resize_keyboard = True).add(btn18, btn19, btn20, btn21, btn25)

btn23 = InlineKeyboardButton('Подпишись!', url = "https://t.me/englishlanguageforlife")
btn24 = InlineKeyboardButton('Начать учить английский!', callback_data = 'subchanneldone')

otherMenu5 = InlineKeyboardMarkup(row_width = 1)
otherMenu5.insert(btn23)
otherMenu5.insert(btn24)

btn27 = InlineKeyboardButton('Пройти тест Present Simple ✅', callback_data = 'presentsimple')
otherMenu6 = InlineKeyboardMarkup(row_width = 1)
otherMenu6.insert(btn27)

btn28 = KeyboardButton('go', callback_data = '1')
btn29 = KeyboardButton('goes', callback_data = '2')
btn30 = KeyboardButton('going', callback_data = '3')

otherMenu7 = InlineKeyboardMarkup(row_width = 1)
otherMenu7.insert(btn28)
otherMenu7.insert(btn29)
otherMenu7.insert(btn30)

btn31 = KeyboardButton('visits', callback_data = '4')
btn32 = KeyboardButton('visit', callback_data = '5')
btn33 = KeyboardButton('visiting', callback_data = '6')

otherMenu8 = InlineKeyboardMarkup(row_width = 1)
otherMenu8.insert(btn31)
otherMenu8.insert(btn32)
otherMenu8.insert(btn33)

btn34 = KeyboardButton('plays', callback_data = '7')
btn35 = KeyboardButton('playing', callback_data = '8')
btn36 = KeyboardButton('play', callback_data = '9')

otherMenu9 = InlineKeyboardMarkup(row_width = 1)
otherMenu9.insert(btn34)
otherMenu9.insert(btn35)
otherMenu9.insert(btn36)

btn37 = KeyboardButton('works', callback_data = '10')
btn38 = KeyboardButton('working', callback_data = '11')
btn39 = KeyboardButton('work', callback_data = '12')

otherMenu10 = InlineKeyboardMarkup(row_width = 1)
otherMenu10.insert(btn37)
otherMenu10.insert(btn38)
otherMenu10.insert(btn39)

btn40 = KeyboardButton('tells', callback_data = '13')
btn41 = KeyboardButton('telling', callback_data = '14')
btn42 = KeyboardButton('tell', callback_data = '15')

otherMenu11 = InlineKeyboardMarkup(row_width = 1)
otherMenu11.insert(btn40)
otherMenu11.insert(btn41)
otherMenu11.insert(btn42)
