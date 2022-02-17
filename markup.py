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

btn28 = KeyboardButton('go', callback_data = '28')
btn29 = KeyboardButton('goes', callback_data = '29')
btn30 = KeyboardButton('going', callback_data = '30')

otherMenu7 = InlineKeyboardMarkup(row_width = 1)
otherMenu7.insert(btn28)
otherMenu7.insert(btn29)
otherMenu7.insert(btn30)

btn31 = KeyboardButton('visits', callback_data = '31')
btn32 = KeyboardButton('visit', callback_data = '32')
btn33 = KeyboardButton('visiting', callback_data = '33')

otherMenu8 = InlineKeyboardMarkup(row_width = 1)
otherMenu8.insert(btn31)
otherMenu8.insert(btn32)
otherMenu8.insert(btn33)

btn34 = KeyboardButton('plays', callback_data = '34')
btn35 = KeyboardButton('playing', callback_data = '35')
btn36 = KeyboardButton('play', callback_data = '36')

otherMenu9 = InlineKeyboardMarkup(row_width = 1)
otherMenu9.insert(btn34)
otherMenu9.insert(btn35)
otherMenu9.insert(btn36)

btn37 = KeyboardButton('works', callback_data = '37')
btn38 = KeyboardButton('working', callback_data = '38')
btn39 = KeyboardButton('work', callback_data = '39')

otherMenu10 = InlineKeyboardMarkup(row_width = 1)
otherMenu10.insert(btn37)
otherMenu10.insert(btn38)
otherMenu10.insert(btn39)

btn40 = KeyboardButton('tells', callback_data = '40')
btn41 = KeyboardButton('telling', callback_data = '41')
btn42 = KeyboardButton('tell', callback_data = '42')

otherMenu11 = InlineKeyboardMarkup(row_width = 1)
otherMenu11.insert(btn40)
otherMenu11.insert(btn41)
otherMenu11.insert(btn42)

btn43 = KeyboardButton('are cycling', callback_data = '43')
btn44 = KeyboardButton('is cycling', callback_data = '44')
btn45 = KeyboardButton('cycles', callback_data = '45')

otherMenu12 = InlineKeyboardMarkup(row_width = 1)
otherMenu12.insert(btn43)
otherMenu12.insert(btn44)
otherMenu12.insert(btn45)

btn46 = KeyboardButton("aren't travelling", callback_data = '46')
btn47 = KeyboardButton("doesn't travel", callback_data = '47')
btn48 = KeyboardButton("isn't travelling", callback_data = '48')

otherMenu13 = InlineKeyboardMarkup(row_width = 1)
otherMenu13.insert(btn46)
otherMenu13.insert(btn47)
otherMenu13.insert(btn48)

btn49 = KeyboardButton('does sunbathe', callback_data = '49')
btn50 = KeyboardButton('am sunbathing', callback_data = '50')
btn51 = KeyboardButton('sunbathing', callback_data = '51')

otherMenu14 = InlineKeyboardMarkup(row_width = 1)
otherMenu14.insert(btn49)
otherMenu14.insert(btn50)
otherMenu14.insert(btn51)

btn52 = KeyboardButton("isn't watching", callback_data = '52')
btn53 = KeyboardButton("doesn't watch", callback_data = '53')
btn54 = KeyboardButton("is watching", callback_data = '54')

otherMenu15 = InlineKeyboardMarkup(row_width = 1)
otherMenu15.insert(btn52)
otherMenu15.insert(btn53)
otherMenu15.insert(btn54)

btn55 = KeyboardButton("aren't swimming", callback_data = '55')
btn56 = KeyboardButton("doesn't swim", callback_data = '56')
btn57 = KeyboardButton("is swimming", callback_data = '57')

otherMenu16 = InlineKeyboardMarkup(row_width = 1)
otherMenu16.insert(btn55)
otherMenu16.insert(btn56)
otherMenu16.insert(btn57)

btn58 = InlineKeyboardButton('Пройти тест Present Continuous ✅', callback_data = 'presentcontinuous')

otherMenu17 = InlineKeyboardMarkup(row_width = 1)
otherMenu17.insert(btn58)

btn59 = InlineKeyboardButton('Пройти тест Present Perfect ✅', callback_data = 'presentperfect')

otherMenu18 = InlineKeyboardMarkup(row_width = 1)
otherMenu18.insert(btn59)

btn60 = KeyboardButton('Do you speak', callback_data = '60')
btn61 = KeyboardButton('Have you spoken', callback_data = '61')
btn62 = KeyboardButton('Are you speaking', callback_data = '62')

otherMenu19 = InlineKeyboardMarkup(row_width = 1)
otherMenu19.insert(btn60)
otherMenu19.insert(btn61)
otherMenu19.insert(btn62)

btn63 = KeyboardButton("haven't done", callback_data = '63')
btn64 = KeyboardButton("doesn't do", callback_data = '64')
btn65 = KeyboardButton("aren't doing", callback_data = '65')

otherMenu20 = InlineKeyboardMarkup(row_width = 1)
otherMenu20.insert(btn63)
otherMenu20.insert(btn64)
otherMenu20.insert(btn65)

btn66 = KeyboardButton('does do', callback_data = '66')
btn67 = KeyboardButton('is doing', callback_data = '67')
btn68 = KeyboardButton('have done', callback_data = '68')

otherMenu21 = InlineKeyboardMarkup(row_width = 1)
otherMenu21.insert(btn66)
otherMenu21.insert(btn67)
otherMenu21.insert(btn68)

btn69 = KeyboardButton('have told', callback_data = '69')
btn70 = KeyboardButton('has told', callback_data = '70')
btn71 = KeyboardButton('are telling', callback_data = '71')

otherMenu22 = InlineKeyboardMarkup(row_width = 1)
otherMenu22.insert(btn69)
otherMenu22.insert(btn70)
otherMenu22.insert(btn71)

btn72 = KeyboardButton('has been heard', callback_data = '72')
btn73 = KeyboardButton('has heard', callback_data = '73')
btn74 = KeyboardButton('have heard', callback_data = '74')

otherMenu23 = InlineKeyboardMarkup(row_width = 1)
otherMenu23.insert(btn72)
otherMenu23.insert(btn73)
otherMenu23.insert(btn74)

btn75 = InlineKeyboardButton('Пройти тест Present Perfect Continuous✅', callback_data = 'presentperfectcontinuous')

otherMenu24 = InlineKeyboardMarkup(row_width = 1)
otherMenu24.insert(btn75)

btn76 = KeyboardButton('painted', callback_data = '76')
btn77 = KeyboardButton('have painted', callback_data = '77')
btn78 = KeyboardButton('have been painting', callback_data = '78')

otherMenu25 = InlineKeyboardMarkup(row_width = 1)
otherMenu25.insert(btn76)
otherMenu25.insert(btn77)
otherMenu25.insert(btn78)

btn79 = KeyboardButton("is watching", callback_data = '79')
btn80 = KeyboardButton("has been watching", callback_data = '80')
btn81 = KeyboardButton("has watching", callback_data = '81')

otherMenu26 = InlineKeyboardMarkup(row_width = 1)
otherMenu26.insert(btn79)
otherMenu26.insert(btn80)
otherMenu26.insert(btn81)

btn82 = KeyboardButton('have been done', callback_data = '82')
btn83 = KeyboardButton('has been doing', callback_data = '83')
btn84 = KeyboardButton('have been doing', callback_data = '84')

otherMenu27 = InlineKeyboardMarkup(row_width = 1)
otherMenu27.insert(btn82)
otherMenu27.insert(btn83)
otherMenu27.insert(btn84)

btn85 = KeyboardButton('have learned', callback_data = '85')
btn86 = KeyboardButton('has learning', callback_data = '86')
btn87 = KeyboardButton('have been learning', callback_data = '87')

otherMenu28 = InlineKeyboardMarkup(row_width = 1)
otherMenu28.insert(btn85)
otherMenu28.insert(btn86)
otherMenu28.insert(btn87)

btn88 = KeyboardButton('has been chasing', callback_data = '88')
btn89 = KeyboardButton('has chased', callback_data = '89')
btn90 = KeyboardButton('have been chasing', callback_data = '90')

otherMenu29 = InlineKeyboardMarkup(row_width = 1)
otherMenu29.insert(btn88)
otherMenu29.insert(btn89)
otherMenu29.insert(btn90)

btn91 = KeyboardButton('didn’t drink', callback_data = '91')
btn92 = KeyboardButton("don't drink", callback_data = '92')
btn93 = KeyboardButton("haven't drunk", callback_data = '93')

otherMenu30 = InlineKeyboardMarkup(row_width = 1)
otherMenu30.insert(btn91)
otherMenu30.insert(btn92)
otherMenu30.insert(btn93)

btn94 = KeyboardButton("get on", callback_data = '94')
btn95 = KeyboardButton("got on", callback_data = '95')
btn96 = KeyboardButton("is getting on", callback_data = '96')

otherMenu31 = InlineKeyboardMarkup(row_width = 1)
otherMenu31.insert(btn94)
otherMenu31.insert(btn95)
otherMenu31.insert(btn96)

btn97 = KeyboardButton('have got up', callback_data = '97')
btn98 = KeyboardButton('got up', callback_data = '98')
btn99 = KeyboardButton('get up', callback_data = '99')

otherMenu32 = InlineKeyboardMarkup(row_width = 1)
otherMenu32.insert(btn97)
otherMenu32.insert(btn98)
otherMenu32.insert(btn99)

btn100 = KeyboardButton('got off', callback_data = '100')
btn101 = KeyboardButton('are getting of', callback_data = '101')
btn102 = KeyboardButton('get off', callback_data = '102')

otherMenu33 = InlineKeyboardMarkup(row_width = 1)
otherMenu33.insert(btn100)
otherMenu33.insert(btn101)
otherMenu33.insert(btn102)

btn103 = KeyboardButton("didn't change", callback_data = '103')
btn104 = KeyboardButton("haven't changed", callback_data = '104')
btn105 = KeyboardButton("don't changed", callback_data = '105')

otherMenu34 = InlineKeyboardMarkup(row_width = 1)
otherMenu34.insert(btn103)
otherMenu34.insert(btn104)
otherMenu34.insert(btn105)


btn106 = KeyboardButton('shaked', callback_data = '106')
btn107 = KeyboardButton('was shaking', callback_data = '107')
btn108 = KeyboardButton('has been shaking', callback_data = '108')

otherMenu35 = InlineKeyboardMarkup(row_width = 1)
otherMenu35.insert(btn106)
otherMenu35.insert(btn107)
otherMenu35.insert(btn108)

btn109 = KeyboardButton("is rising", callback_data = '109')
btn110 = KeyboardButton("has been rising", callback_data = '110')
btn111 = KeyboardButton("was rising", callback_data = '111')

otherMenu36 = InlineKeyboardMarkup(row_width = 1)
otherMenu36.insert(btn109)
otherMenu36.insert(btn110)
otherMenu36.insert(btn111)

btn112 = KeyboardButton("wasn't really existing", callback_data = '112')
btn113 = KeyboardButton('has been really existing', callback_data = '113')
btn114 = KeyboardButton('is really existing', callback_data = '114')

otherMenu37 = InlineKeyboardMarkup(row_width = 1)
otherMenu37.insert(btn112)
otherMenu37.insert(btn113)
otherMenu37.insert(btn114)

btn115 = KeyboardButton('took', callback_data = '115')
btn116 = KeyboardButton('was taking', callback_data = '116')
btn117 = KeyboardButton('has been taking', callback_data = '117')

otherMenu38 = InlineKeyboardMarkup(row_width = 1)
otherMenu38.insert(btn115)
otherMenu38.insert(btn116)
otherMenu38.insert(btn117)

btn118 = KeyboardButton('is looking', callback_data = '118')
btn119 = KeyboardButton('has been looking', callback_data = '119')
btn120 = KeyboardButton("wasn't looking", callback_data = '120')

otherMenu39 = InlineKeyboardMarkup(row_width = 1)
otherMenu39.insert(btn118)
otherMenu39.insert(btn119)
otherMenu39.insert(btn120)

btn121 = KeyboardButton('painted', callback_data = '121')
btn122 = KeyboardButton('have painted', callback_data = '122')
btn123 = KeyboardButton('have been painting', callback_data = '123')

otherMenu40 = InlineKeyboardMarkup(row_width = 1)
otherMenu40.insert(btn121)
otherMenu40.insert(btn122)
otherMenu40.insert(btn123)

btn124 = KeyboardButton("is watching", callback_data = '124')
btn125 = KeyboardButton("has been watching", callback_data = '125')
btn126 = KeyboardButton("has watching", callback_data = '126')

otherMenu41 = InlineKeyboardMarkup(row_width = 1)
otherMenu41.insert(btn124)
otherMenu41.insert(btn125)
otherMenu41.insert(btn126)

btn127 = KeyboardButton('have been done', callback_data = '127')
btn128 = KeyboardButton('has been doing', callback_data = '128')
btn129 = KeyboardButton('have been doing', callback_data = '129')

otherMenu42 = InlineKeyboardMarkup(row_width = 1)
otherMenu42.insert(btn127)
otherMenu42.insert(btn128)
otherMenu42.insert(btn129)

btn130 = KeyboardButton('have learned', callback_data = '130')
btn131 = KeyboardButton('has learning', callback_data = '131')
btn132 = KeyboardButton('have been learning', callback_data = '132')

otherMenu43 = InlineKeyboardMarkup(row_width = 1)
otherMenu43.insert(btn130)
otherMenu43.insert(btn131)
otherMenu43.insert(btn132)

btn133 = KeyboardButton('has been chasing', callback_data = '133')
btn134 = KeyboardButton('has chased', callback_data = '134')
btn135 = KeyboardButton('have been chasing', callback_data = '135')

otherMenu44 = InlineKeyboardMarkup(row_width = 1)
otherMenu44.insert(btn133)
otherMenu44.insert(btn134)
otherMenu44.insert(btn135)

btn136 = KeyboardButton('painted', callback_data = '136')
btn137 = KeyboardButton('have painted', callback_data = '137')
btn138 = KeyboardButton('have been painting', callback_data = '138')

otherMenu45 = InlineKeyboardMarkup(row_width = 1)
otherMenu45.insert(btn136)
otherMenu45.insert(btn137)
otherMenu45.insert(btn138)

btn139 = KeyboardButton("is watching", callback_data = '139')
btn140 = KeyboardButton("has been watching", callback_data = '140')
btn141 = KeyboardButton("has watching", callback_data = '141')

otherMenu46 = InlineKeyboardMarkup(row_width = 1)
otherMenu46.insert(btn139)
otherMenu46.insert(btn140)
otherMenu46.insert(btn141)

btn142 = KeyboardButton('have been done', callback_data = '142')
btn143 = KeyboardButton('has been doing', callback_data = '143')
btn144 = KeyboardButton('have been doing', callback_data = '144')

otherMenu47 = InlineKeyboardMarkup(row_width = 1)
otherMenu47.insert(btn142)
otherMenu47.insert(btn143)
otherMenu47.insert(btn144)

btn145 = KeyboardButton('have learned', callback_data = '145')
btn146 = KeyboardButton('has learning', callback_data = '146')
btn147 = KeyboardButton('have been learning', callback_data = '147')

otherMenu48 = InlineKeyboardMarkup(row_width = 1)
otherMenu48.insert(btn145)
otherMenu48.insert(btn146)
otherMenu48.insert(btn147)

btn148 = KeyboardButton('has been chasing', callback_data = '148')
btn149 = KeyboardButton('has chased', callback_data = '149')
btn150 = KeyboardButton('have been chasing', callback_data = '150')

otherMenu49 = InlineKeyboardMarkup(row_width = 1)
otherMenu49.insert(btn148)
otherMenu49.insert(btn149)
otherMenu49.insert(btn150)

btn151 = KeyboardButton('painted', callback_data = '151')
btn152 = KeyboardButton('have painted', callback_data = '152')
btn153 = KeyboardButton('have been painting', callback_data = '153')

otherMenu50 = InlineKeyboardMarkup(row_width = 1)
otherMenu50.insert(btn151)
otherMenu50.insert(btn152)
otherMenu50.insert(btn153)

btn154 = KeyboardButton("is watching", callback_data = '154')
btn155 = KeyboardButton("has been watching", callback_data = '155')
btn156 = KeyboardButton("has watching", callback_data = '156')

otherMenu51 = InlineKeyboardMarkup(row_width = 1)
otherMenu51.insert(btn154)
otherMenu51.insert(btn155)
otherMenu51.insert(btn156)

btn157 = KeyboardButton('have been done', callback_data = '157')
btn158 = KeyboardButton('has been doing', callback_data = '158')
btn159 = KeyboardButton('have been doing', callback_data = '159')

otherMenu52 = InlineKeyboardMarkup(row_width = 1)
otherMenu52.insert(btn157)
otherMenu52.insert(btn158)
otherMenu52.insert(btn159)

btn160 = KeyboardButton('have learned', callback_data = '160')
btn161 = KeyboardButton('has learning', callback_data = '161')
btn162 = KeyboardButton('have been learning', callback_data = '162')

otherMenu53 = InlineKeyboardMarkup(row_width = 1)
otherMenu53.insert(btn160)
otherMenu53.insert(btn161)
otherMenu53.insert(btn162)

btn163 = KeyboardButton('has been chasing', callback_data = '163')
btn164 = KeyboardButton('has chased', callback_data = '164')
btn165 = KeyboardButton('have been chasing', callback_data = '165')

otherMenu54 = InlineKeyboardMarkup(row_width = 1)
otherMenu54.insert(btn163)
otherMenu54.insert(btn164)
otherMenu54.insert(btn165)

btn166 = KeyboardButton('Пройти тест Past Simple ✅', callback_data = 'pastsimple')

otherMenu55 = InlineKeyboardMarkup(row_width = 1)
otherMenu55.insert(btn166)

btn167 = KeyboardButton('Пройти тест Past Continuous ✅', callback_data = 'pastcontinuous')

otherMenu56 = InlineKeyboardMarkup(row_width = 1)
otherMenu56.insert(btn167)

btn168 = KeyboardButton('Пройти тест Past Perfect ✅', callback_data = 'pastperfect')

otherMenu57 = InlineKeyboardMarkup(row_width = 1)
otherMenu57.insert(btn168)

btn169 = KeyboardButton('Пройти тест Past Perfect Continuous ✅', callback_data = 'pastperfectcontinuous')

otherMenu58 = InlineKeyboardMarkup(row_width = 1)
otherMenu58.insert(btn169)

btn106 = KeyboardButton('was shaking', callback_data = '106')
btn107 = KeyboardButton('shaked', callback_data = '107')
btn108 = KeyboardButton('has been shaking', callback_data = '108')

otherMenu35 = InlineKeyboardMarkup(row_width = 1)
otherMenu35.insert(btn106)
otherMenu35.insert(btn107)
otherMenu35.insert(btn108)

btn109 = KeyboardButton("has risen", callback_data = '109')
btn110 = KeyboardButton("was rising", callback_data = '110')
btn111 = KeyboardButton("has been rising", callback_data = '111')

otherMenu36 = InlineKeyboardMarkup(row_width = 1)
otherMenu36.insert(btn109)
otherMenu36.insert(btn110)
otherMenu36.insert(btn111)

btn112 = KeyboardButton("wasn't really existing", callback_data = '112')
btn113 = KeyboardButton("hasn't been really existing", callback_data = '113')
btn114 = KeyboardButton("isnt't really existing", callback_data = '114')

otherMenu37 = InlineKeyboardMarkup(row_width = 1)
otherMenu37.insert(btn112)
otherMenu37.insert(btn113)
otherMenu37.insert(btn114)

btn115 = KeyboardButton('has been taking', callback_data = '115')
btn116 = KeyboardButton('has took', callback_data = '116')
btn117 = KeyboardButton('was taking', callback_data = '117')

otherMenu38 = InlineKeyboardMarkup(row_width = 1)
otherMenu38.insert(btn115)
otherMenu38.insert(btn116)
otherMenu38.insert(btn117)

btn118 = KeyboardButton("wasn't looking", callback_data = '118')
btn119 = KeyboardButton("isnt't looking", callback_data = '119')
btn120 = KeyboardButton("hasn't been looking", callback_data = '120')

otherMenu39 = InlineKeyboardMarkup(row_width = 1)
otherMenu39.insert(btn118)
otherMenu39.insert(btn119)
otherMenu39.insert(btn120)
