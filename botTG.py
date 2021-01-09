import telebot
from telebot import types
 
bot = telebot.TeleBot('1445399636:AAE9MJDJb3OmTQWE7M-xjNwmILNkrz6cKZ0')

@bot.message_handler(commands=['start'])

def send_welcome(message):#Начало работы бота
	bot.reply_to(message, "Привет, я создан для прохождения тестов по истории.")
	markup = types.ReplyKeyboardMarkup()	
	itemONE = types.KeyboardButton('№1' + '\n' + 'X век')#10 век
	itemTWO = types.KeyboardButton('№2' + '\n' + 'XI век')#11 век
	itemTHREE = types.KeyboardButton('№3' + '\n' + 'XII век')#12 век
	itemFOUR = types.KeyboardButton('№4' + '\n' + 'XIII век')#13 век
	itemFIVE = types.KeyboardButton('№5' + '\n' + 'XIV век')#14 век
	itemSIX = types.KeyboardButton('№6' + '\n' + 'XV век')#15 век
	itemSEVEN = types.KeyboardButton('№7' + '\n' + 'XVI век')#16 век
	itemEIGHT = types.KeyboardButton('№8' + '\n' + 'XVII век')#17 век
	itemNINE = types.KeyboardButton('№9' + '\n' + 'XVII век')#17 век
	itemTEN = types.KeyboardButton('№10' + '\n' + 'XVIII век')#18 век
	itemELEVEN = types.KeyboardButton('№11' + '\n' + 'XVIII век')#18 век
	itemTWELVE = types.KeyboardButton('№12' + '\n' + 'XVIII век')#18 век
	itemTHIRTEEN = types.KeyboardButton('№13' + '\n' + 'XIX век')#19 век
	itemFOURTEEN = types.KeyboardButton('№14' + '\n' + 'XIX век')#19 век
	itemFIFTEEN = types.KeyboardButton('№15' + '\n' + 'XIX век')#19 век
	itemSIXTEEN = types.KeyboardButton('№16' + '\n' + 'XX век')#20 век
	itemSEVENTEEN = types.KeyboardButton('№17' + '\n' + 'XX век')#20 век
	itemEIGHTEEN = types.KeyboardButton('№18' + '\n' + 'XX век')#20 век

	markup.row(itemONE, itemTWO, itemTHREE)
	markup.row(itemFOUR, itemFIVE, itemSIX)
	markup.row(itemSEVEN, itemEIGHT, itemNINE)
	markup.row(itemTEN, itemELEVEN, itemTWELVE)
	markup.row(itemTHIRTEEN, itemFOURTEEN, itemFIFTEEN)
	markup.row(itemSIXTEEN, itemSEVENTEEN, itemEIGHTEEN)

	bot.send_message(message.chat.id, "Выбери номер теста:", reply_markup=markup)
	

@bot.message_handler(content_types=['text'])
def select_question1(message):#Выбор теста	
	if message.text==('№1' + '\n' + 'X век'):#10 век
		question1(message)
	elif message.text==('№2'+ '\n' + 'XI век'):#11 век
		question2(message)	
	elif message.text==('№3'+ '\n' + 'XII век'):#12 век
		question3(message)
	elif message.text==('№4'+ '\n' + 'XIII век'):#13 век
		question4(message)
	elif message.text==('№5' + '\n' + 'XIV век'):#14 век
		question5(message)
	elif message.text==('№6' + '\n' + 'XV век'):#15 век
		question6(message)
	elif message.text==('№7' + '\n' + 'XVI век'):#16 век
		question7(message)
	elif message.text==('№8' + '\n' + 'XVII век'):#17 век
		question8(message)
	elif message.text==('№9' + '\n' + 'XVII век'):#17 век
		question9(message)
	elif message.text==('№10' + '\n' + 'XVIII век'):#18 век
		question10(message)
	elif message.text==('№11' + '\n' + 'XVIII век'):#18 век
		question11(message)
	elif message.text==('№12' + '\n' + 'XVIII век'):#18 век
		question12(message)
	elif message.text==('№13' + '\n' + 'XIX век'):#19 век
		question13(message) 
	elif message.text==('№14' + '\n' + 'XIX век'):#19 век
		question14(message)
	elif message.text==('№15' + '\n' + 'XIX век'):#19 век
		question15(message)
	elif message.text==('№16' + '\n' + 'XX век'):#20 век
		question16(message)
	elif message.text==('№17' + '\n' + 'XX век'):#20 век
		question17(message)
	elif message.text==('№18' + '\n' + 'XX век'):#20 век
		question18(message) 


def question1(message):#Вопрос 1, тест 1
	global ONEcount			
	ONEcount=0					
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('922')
	itemTWO=types.KeyboardButton('928')
	itemTHREE=types.KeyboardButton('988')
	itemFOUR=types.KeyboardButton('982')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было крещение Руси?", reply_markup=markup)
	bot.register_next_step_handler(message, answerA1)


def answerA1(message):#Проверка 1 вопроса на правильность, тест 1
	global ONEcount					
	if message.text=='988':
		bot.send_message(message.chat.id, "Ответ верный")
		ONEcount+=1
		answerA2(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ONEcount+=0
		answerA2(message)		


def answerA2(message):#Вопрос 2, тест 1
	global ONEcount		
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('963-975')
	itemTWO=types.KeyboardButton('964-972')
	itemTHREE=types.KeyboardButton('964-970')
	itemFOUR=types.KeyboardButton('971-986')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Годы правления Святослава Игоревича?", reply_markup=markup)
	bot.register_next_step_handler(message, answerA3)


def answerA3(message):#Проверка 2 вопроса на правильность, тест 1
	global ONEcount
	if message.text=='964-972':
		bot.send_message(message.chat.id, "Ответ верный")
		ONEcount+=1
		answerA4(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ONEcount+=0
		answerA4(message)		

		
def answerA4(message):#Вопрос 3, тест 1
	global ONEcount		
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('950')
	itemTWO=types.KeyboardButton('940')
	itemTHREE=types.KeyboardButton('945')
	itemFOUR=types.KeyboardButton('930')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Убийство Игоря древлянами, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerA5)	


def answerA5(message):#Проверка 3 вопроса на правильность, тест 1
	global ONEcount
	if message.text=='945':
		bot.send_message(message.chat.id, "Ответ верный")
		ONEcount+=1
		answerA6(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ONEcount+=0
		answerA6(message)		
			
	
def answerA6(message):#Вопрос 4, тест 1
	global ONEcount			
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('940')
	itemTWO=types.KeyboardButton('943')
	itemTHREE=types.KeyboardButton('945')
	itemFOUR=types.KeyboardButton('946')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был поход княгини Ольги в Древлянскую землю?", reply_markup=markup)
	bot.register_next_step_handler(message, answerA7)


def answerA7(message):#Проверка 4 вопроса на правильность, тест 1
	global ONEcount
	if message.text=='946':
		bot.send_message(message.chat.id, "Ответ верный")
		ONEcount+=1
		answerA8(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ONEcount+=0
		answerA8(message)		


def answerA8(message):#Вопрос 5, тест 1
	global ONEcount		
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('972')
	itemTWO=types.KeyboardButton('976')
	itemTHREE=types.KeyboardButton('975')
	itemFOUR=types.KeyboardButton('973')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Гибель князя Святослава на днепровских порогах, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerA9)

	
def answerA9(message):#Проверка 5 вопроса на правильность, тест 1
	global ONEcount
	if message.text=='972':
		bot.send_message(message.chat.id, "Ответ верный")
		ONEcount+=1
		answerA10(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ONEcount+=0
		answerA10(message)		
	

def answerA10(message):#Подсчёт результатов, тест 1
	global ONEcount
	if ONEcount==5:		
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceA1(message)		
	elif ONEcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceA1(message)
	elif ONEcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceA1(message)
	elif (ONEcount==2) or (ONEcount==1) or (ONEcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceA1(message)


def choiceA1(message):#Что делать дальше, тест 1
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceA2)
		

def choiceA2(message):#Выбор действия, тест 1
	if message.text=='Пройти тест снова':
		question1(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start.",reply_markup=keyboard)


def question2(message):#Вопрос 1, тест 2
	global TWOcount
	TWOcount=0	
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1071')
	itemTWO=types.KeyboardButton('1072')
	itemTHREE=types.KeyboardButton('1073')
	itemFOUR=types.KeyboardButton('1074')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Составление «Правды Ярославичей», какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerB1)


def answerB1(message):#Проверка 1 вопроса на правильность, тест 2
	global TWOcount	
	if message.text=='1072':
		bot.send_message(message.chat.id, "Ответ верный")
		TWOcount+=1
		answerB2(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		TWOcount+=0
		answerB2(message)		


def answerB2(message):#Вопрос 2, тест 2
	global TWOcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1095')
	itemTWO=types.KeyboardButton('1097')
	itemTHREE=types.KeyboardButton('1093')
	itemFOUR=types.KeyboardButton('1096')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был съезд князей в Любече?", reply_markup=markup)
	bot.register_next_step_handler(message, answerB3)


def answerB3(message):#Проверка 2 вопроса на правильность, тест 2
	global TWOcount
	if message.text=='1097':
		bot.send_message(message.chat.id, "Ответ верный")
		TWOcount+=1
		answerB4(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWOcount+=0
		answerB4(message)


def answerB4(message):#Вопрос 3, тест 2
	global TWOcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1012')
	itemTWO=types.KeyboardButton('1013')
	itemTHREE=types.KeyboardButton('1016')
	itemFOUR=types.KeyboardButton('1015')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году умер князь Владимир «Красное Солнышко»?", reply_markup=markup)
	bot.register_next_step_handler(message, answerB5)

	
def answerB5(message):#Проверка 3 вопроса на правильность, тест 2
	global TWOcount
	if message.text=='1015':
		bot.send_message(message.chat.id, "Ответ верный")
		TWOcount+=1
		answerB6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWOcount+=0
		answerB6(message)


def answerB6(message):#Вопрос 4, тест 2
	global TWOcount			
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1014')
	itemTWO=types.KeyboardButton('1015')
	itemTHREE=types.KeyboardButton('1016')
	itemFOUR=types.KeyboardButton('1017')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "«Правда Ярослава», какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerB7)


def answerB7(message):#Проверка 4 вопроса на правильность, тест 2
	global TWOcount
	if message.text=='1016':
		bot.send_message(message.chat.id, "Ответ верный")
		TWOcount+=1
		answerB8(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWOcount+=0
		answerB8(message)		


def answerB8(message):#Вопрос 5, тест 2
	global TWOcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1035')
	itemTWO=types.KeyboardButton('1036')
	itemTHREE=types.KeyboardButton('1037')
	itemFOUR=types.KeyboardButton('1038')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был разгром печенегов под Киевом?", reply_markup=markup)
	bot.register_next_step_handler(message, answerB9)

	
def answerB9(message):#Проверка 5 вопроса на правильность, тест 2
	global TWOcount
	if message.text=='1036':
		bot.send_message(message.chat.id, "Ответ верный")
		TWOcount+=1
		answerB10(message)		
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWOcount+=0
		answerB10(message)
		

def answerB10(message):#Подсчёт результатов, тест 2
	global TWOcount
	if TWOcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceB1(message)
	elif TWOcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceB1(message)
	elif TWOcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceB1(message)
	elif (TWOcount==2) or (TWOcount==1) or (TWOcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceB1(message)


def choiceB1(message):#Что делать дальше, тест 2
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceB2)
		

def choiceB2(message):#Выбор действия, тест 2
	if message.text=='Пройти тест снова':
		question2(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question3(message):#Вопрос 1, тест 3
	global THREEcount
	THREEcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1145')
	itemTWO=types.KeyboardButton('1147')
	itemTHREE=types.KeyboardButton('1149')
	itemFOUR=types.KeyboardButton('1151')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Первое упоминание Москвы в летописи, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerC1)


def answerC1(message):#Проверка 1 вопроса на правильность, тест 3
	global THREEcount
	if message.text=='1147':
		bot.send_message(message.chat.id, "Ответ верный")
		THREEcount+=1
		answerC2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		THREEcount+=0
		answerC2(message)	


def answerC2(message):#Вопрос 2, тест 3
	global THREEcount
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1110')
	itemTWO=types.KeyboardButton('1112')
	itemTHREE=types.KeyboardButton('1111')
	itemFOUR=types.KeyboardButton('1113')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году Владимир Мономах начал править в Киеве?", reply_markup=markup)
	bot.register_next_step_handler(message, answerC3)


def answerC3(message):#Проверка 2 вопроса на правильность, тест 3
	global THREEcount
	if message.text=='1113':
		bot.send_message(message.chat.id, "Ответ верный")
		THREEcount+=1
		answerC4(message)
		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		THREEcount+=0
		answerC4(message)	


def answerC4(message):#Вопрос 3, тест 3
	global THREEcount
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1181')
	itemTWO=types.KeyboardButton('1183')
	itemTHREE=types.KeyboardButton('1184')
	itemFOUR=types.KeyboardButton('1185')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был поход новгород-северского князя Игоря Святославича на половцев?", reply_markup=markup)
	bot.register_next_step_handler(message, answerC5)


def answerC5(message):#Проверка 3 вопроса на правильность, тест 3
	global THREEcount
	if message.text=='1185':
		bot.send_message(message.chat.id, "Ответ верный")
		THREEcount+=1
		answerC6(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		THREEcount+=0
		answerC6(message)


def answerC6(message):#Вопрос 4, тест 3
	global THREEcount
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1173')
	itemTWO=types.KeyboardButton('1174')
	itemTHREE=types.KeyboardButton('1175')
	itemFOUR=types.KeyboardButton('1176')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году погиб князь Андрей Боголюбский?", reply_markup=markup)
	bot.register_next_step_handler(message, answerC7)


def answerC7(message):#Проверка 4 вопроса на правильность, тест 3
	global THREEcount
	if message.text=='1174':
		bot.send_message(message.chat.id, "Ответ верный")
		THREEcount+=1
		answerC8(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		THREEcount+=0
		answerC8(message)


def answerC8(message):#Вопрос 5, тест 3
	global THREEcount
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1196')
	itemTWO=types.KeyboardButton('1197')
	itemTHREE=types.KeyboardButton('1198')
	itemFOUR=types.KeyboardButton('1199')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году объеденили Волынское и Галицкое княжества?", reply_markup=markup)
	bot.register_next_step_handler(message, answerC9)


def answerC9(message):#Проверка 5 вопроса на правильность, тест 3
	global THREEcount
	if message.text=='1199':
		bot.send_message(message.chat.id, "Ответ верный")
		THREEcount+=1
		answerC10(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		THREEcount+=0
		answerC10(message)


def answerC10(message):#Подсчёт результатов, тест 3
	global THREEcount
	if THREEcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceC1(message)
	elif THREEcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceC1(message)
	elif THREEcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceC1(message)
	elif (THREEcount==2) or (THREEcount==1) or (THREEcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceC1(message)


def choiceC1(message):#Что делать дальше, тест 3
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceC2)
		

def choiceC2(message):#Выбор действия, тест 3
	if message.text=='Пройти тест снова':
		question3(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question4(message):#Вопрос 1, тест 4
	global FOURcount
	FOURcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1237')
	itemTWO=types.KeyboardButton('1240')
	itemTHREE=types.KeyboardButton('1241')
	itemFOUR=types.KeyboardButton('1242')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году была Невская битва?", reply_markup=markup)
	bot.register_next_step_handler(message, answerD1)


def answerD1(message):#Проверка 1 вопроса на правильность, тест 4
	global FOURcount
	if message.text=='1240':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURcount+=1
		answerD2(message)	
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURcount+=0
		answerD2(message)	

	
def answerD2(message):#Вопрос 2, тест 4
	global FOURcount		
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1240')
	itemTWO=types.KeyboardButton('1241')
	itemTHREE=types.KeyboardButton('1242')
	itemFOUR=types.KeyboardButton('1243')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было Ледовое побоище?", reply_markup=markup)
	bot.register_next_step_handler(message, answerD3)


def answerD3(message):#Проверка 2 вопроса на правильность, тест 4
	global FOURcount
	if message.text=='1242':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURcount+=1
		answerD4(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURcount+=0
		answerD4(message)	


def answerD4(message):#Вопрос 3, тест 4
	global FOURcount
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1223')
	itemTWO=types.KeyboardButton('1224')
	itemTHREE=types.KeyboardButton('1222')
	itemFOUR=types.KeyboardButton('1221')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Битва на Калке, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerD5)


def answerD5(message):#Проверка 3 вопроса на правильность, тест 4
	global FOURcount
	if message.text=='1223':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURcount+=1
		answerD6(message)	
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURcount+=0
		answerD6(message)


def answerD6(message):#Вопрос 4, тест 4
	global FOURcount
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1237')
	itemTWO=types.KeyboardButton('1238')
	itemTHREE=types.KeyboardButton('1239')
	itemFOUR=types.KeyboardButton('1241')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Взятие ханом Батыем города Владимира, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerD7)


def answerD7(message):#Проверка 4 вопроса на правильность, тест 4
	global FOURcount
	if message.text=='1238':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURcount+=1
		answerD8(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURcount+=0
		answerD8(message)


def answerD8(message):#Вопрос 5, тест 4
	global FOURcount
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1235')
	itemTWO=types.KeyboardButton('1236')
	itemTHREE=types.KeyboardButton('1238')
	itemFOUR=types.KeyboardButton('1237')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Вторжение Батыя в Рязанскую землю, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerD9)


def answerD9(message):#Проверка 5 вопроса на правильность, тест 4
	global FOURcount
	if message.text=='1237':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURcount+=1
		answerD10(message)		
	else: 
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURcount+=0
		answerD10(message)


def answerD10(message):#Подсчёт результатов, тест 4
	global FOURcount
	if FOURcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceD1(message)
	elif FOURcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceD1(message)
	elif FOURcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceD1(message)
	elif (FOURcount==2) or (FOURcount==1) or (FOURcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceD1(message)
	

def choiceD1(message):#Что делать дальше, тест 4
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceD2)
		

def choiceD2(message):#Выбор действия, тест 4
	if message.text=='Пройти тест снова':
		question4(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question5(message):#Вопрос 1, тест 5
	global FIVEcount
	FIVEcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1378')
	itemTWO=types.KeyboardButton('1380')
	itemTHREE=types.KeyboardButton('1387')
	itemFOUR=types.KeyboardButton('1383')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году была Куликовская битва?", reply_markup=markup)
	bot.register_next_step_handler(message,answerE1)


def answerE1(message):#Проверка 1 вопроса на правильность, тест 5
	global FIVEcount
	if message.text=='1380':
		bot.send_message(message.chat.id, "Ответ верный")
		FIVEcount+=1
		answerE2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIVEcount+=0
		answerE2(message)


def answerE2(message):#Вопрос 2, тест 5
	global FIVEcount
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1360')
	itemTWO=types.KeyboardButton('1374')
	itemTHREE=types.KeyboardButton('1375')
	itemFOUR=types.KeyboardButton('1376')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Поход Дмитрия Донского против Твери, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerE3)


def answerE3(message):#Проверка 2 вопроса на правильность, тест 5
	global FIVEcount
	if message.text=='1375':
		bot.send_message(message.chat.id, "Ответ верный")
		FIVEcount+=1
		answerE4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIVEcount+=0
		answerE4(message)


def answerE4(message):#Вопрос 3, тест 5
	global FIVEcount
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1334')
	itemTWO=types.KeyboardButton('1336')
	itemTHREE=types.KeyboardButton('1339')
	itemFOUR=types.KeyboardButton('1337')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Основание Троицкого монастыря Сергием Радонежским, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerE5)


def answerE5(message):#Проверка 3 вопроса на правильность, тест 5
	global FIVEcount
	if message.text=='1337':
		bot.send_message(message.chat.id, "Ответ верный")
		FIVEcount+=1
		answerE6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIVEcount+=0
		answerE6(message)


def answerE6(message):#Вопрос 4, тест 5
	global FIVEcount
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1382')
	itemTWO=types.KeyboardButton('1381')
	itemTHREE=types.KeyboardButton('1384')
	itemFOUR=types.KeyboardButton('1385')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был набег Тохтамыша на Москву?", reply_markup=markup)
	bot.register_next_step_handler(message, answerE7)


def answerE7(message):#Проверка 4 вопроса на правильность, тест 5
	global FIVEcount
	if message.text=='1382':
		bot.send_message(message.chat.id, "Ответ верный")
		FIVEcount+=1
		answerE8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIVEcount+=0
		answerE8(message)


def answerE8(message):#Вопрос 5, тест 5
	global FIVEcount
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1324')
	itemTWO=types.KeyboardButton('1327')
	itemTHREE=types.KeyboardButton('1330')
	itemFOUR=types.KeyboardButton('1333')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Антиордынское восстание в Твери, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerE9)


def answerE9(message):#Проверка 5 вопроса на правильность, тест 5
	global FIVEcount
	if message.text=='1327':
		bot.send_message(message.chat.id, "Ответ верный")
		FIVEcount+=1
		answerE10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIVEcount+=0
		answerE10(message)


def answerE10(message):#Подсчёт результатов, тест 5
	global FIVEcount
	if FIVEcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceE1(message)
	elif FIVEcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceE1(message)
	elif FIVEcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceE1(message)
	elif (FIVEcount==2) or (FIVEcount==1) or (FIVEcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceE1(message)


def choiceE1(message):#Что делать дальше, тест 5
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceE2)
		

def choiceE2(message):#Выбор действия, тест 5
	if message.text=='Пройти тест снова':
		question5(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question6(message):#Вопрос 1, тест 6
	global SIXcount
	SIXcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1476')
	itemTWO=types.KeyboardButton('1478')
	itemTHREE=types.KeyboardButton('1480')
	itemFOUR=types.KeyboardButton('1482')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было стояние на Угре?", reply_markup=markup)
	bot.register_next_step_handler(message,answerF1)


def answerF1(message):#Проверка 1 вопроса на правильность, тест 6
	global SIXcount
	if message.text=='1480':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXcount+=1
		answerF2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXcount+=0
		answerF2(message)
	

def answerF2(message):#Вопрос 2, тест 6
	global SIXcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Вира')
	itemTWO=types.KeyboardButton('Приказы')
	itemTHREE=types.KeyboardButton('Баскаки')
	itemFOUR=types.KeyboardButton('Стрельцы')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Какой из этих терминов появился в XV веке?", reply_markup=markup)
	bot.register_next_step_handler(message, answerF3)


def answerF3(message):#Проверка 2 вопроса на правильность, тест 6
	global SIXcount
	if message.text=='Приказы':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXcount+=1
		answerF4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXcount+=0
		answerF4(message)


def answerF4(message):#Вопрос 3, тест 6
	global SIXcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1482')
	itemTWO=types.KeyboardButton('1484')
	itemTHREE=types.KeyboardButton('1483')
	itemFOUR=types.KeyboardButton('1485')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Вхождение Твери в состав Московского княжества, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerF5)


def answerF5(message):#Проверка 3 вопроса на правильность, тест 6
	global SIXcount
	if message.text=='1485':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXcount+=1
		answerF6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXcount+=0
		answerF6(message)


def answerF6(message):#Вопрос 4, тест 6
	global SIXcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1448')
	itemTWO=types.KeyboardButton('1449')
	itemTHREE=types.KeyboardButton('1447')
	itemFOUR=types.KeyboardButton('1446')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Автокефалия Русской православной церкви, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerF7)


def answerF7(message):#Проверка 4 вопроса на правильность, тест 6
	global SIXcount
	if message.text=='1448':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXcount+=1
		answerF8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXcount+=0
		answerF8(message)


def answerF8(message):#Вопрос 5, тест 6
	global SIXcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1496')
	itemTWO=types.KeyboardButton('1497')
	itemTHREE=types.KeyboardButton('1498')
	itemFOUR=types.KeyboardButton('1499')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был принят судебник Ивана III?", reply_markup=markup)
	bot.register_next_step_handler(message, answerF9)


def answerF9(message):#Проверка 5 вопроса на правильность, тест 6
	global SIXcount
	if message.text=='1497':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXcount+=1
		answerF10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXcount+=0
		answerF10(message)


def answerF10(message):#Подсчёт результатов, тест 6
	global SIXcount
	if SIXcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceF1(message)
	elif SIXcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceF1(message)
	elif SIXcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceF1(message)
	elif SIXcount==2 or (SIXcount==1) or (SIXcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceF1(message)


def choiceF1(message):#Что делать дальше, тест 6
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceF2)
		

def choiceF2(message):#Выбор действия, тест 6
	if message.text=='Пройти тест снова':
		question6(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question7(message):#Вопрос 1, тест 7
	global SEVENcount
	SEVENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1568')
	itemTWO=types.KeyboardButton('1564')
	itemTHREE=types.KeyboardButton('1544')
	itemFOUR=types.KeyboardButton('1567')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Начало книгопечатания в России, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message,answerG1)


def answerG1(message):#Проверка 1 вопроса на правильность, тест 7
	global SEVENcount
	if message.text=='1564':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENcount+=1
		answerG2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENcount+=0
		answerG2(message)
	

def answerG2(message):#Вопрос 2, тест 7
	global SEVENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1548')
	itemTWO=types.KeyboardButton('1569')
	itemTHREE=types.KeyboardButton('1553')
	itemFOUR=types.KeyboardButton('1550')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году приняли Судебник Ивана IV?", reply_markup=markup)
	bot.register_next_step_handler(message, answerG3)


def answerG3(message):#Проверка 2 вопроса на правильность, тест 7
	global SEVENcount
	if message.text=='1550':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENcount+=1
		answerG4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENcount+=0
		answerG4(message)


def answerG4(message):#Вопрос 3, тест 7
	global SEVENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1558')
	itemTWO=types.KeyboardButton('1555')
	itemTHREE=types.KeyboardButton('1561')
	itemFOUR=types.KeyboardButton('1557')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году началась Ливонская война?", reply_markup=markup)
	bot.register_next_step_handler(message, answerG5)


def answerF5(message):#Проверка 3 вопроса на правильность, тест 7
	global SEVENcount
	if message.text=='1558':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENcount+=1
		answerG6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENcount+=0
		answerG6(message)


def answerG6(message):#Вопрос 4, тест 7
	global SEVENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1539')
	itemTWO=types.KeyboardButton('1546')
	itemTHREE=types.KeyboardButton('1547')
	itemFOUR=types.KeyboardButton('1548')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Венчание Ивана IV на царство, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerG7)


def answerG7(message):#Проверка 4 вопроса на правильность, тест 7
	global SEVENcount
	if message.text=='1547':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENcount+=1
		answerG8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENcount+=0
		answerG8(message)


def answerG8(message):#Вопрос 5, тест 7
	global SEVENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1584')
	itemTWO=types.KeyboardButton('1589')
	itemTHREE=types.KeyboardButton('1581')
	itemFOUR=types.KeyboardButton('1593')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Учреждение патриаршества в Московском государстве, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerG9)


def answerG9(message):#Проверка 5 вопроса на правильность, тест 7
	global SEVENcount
	if message.text=='1589':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENcount+=1
		answerG10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENcount+=0
		answerG10(message)


def answerG10(message):#Подсчёт результатов, тест 7
	global SEVENcount
	if SEVENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceG1(message)
	elif SEVENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceG1(message)
	elif SEVENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceG1(message)
	elif (SEVENcount==2) or (SEVENcount==1) or (SEVENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceG1(message)


def choiceG1(message):#Что делать дальше, тест 7
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceG2)
		

def choiceG2(message):#Выбор действия, тест 7
	if message.text=='Пройти тест снова':
		question7(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question8(message):#Вопрос 1, тест 8
	global EIGHTcount
	EIGHTcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1660')
	itemTWO=types.KeyboardButton('1662')
	itemTHREE=types.KeyboardButton('1663')
	itemFOUR=types.KeyboardButton('1664')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был Медный бунт?", reply_markup=markup)
	bot.register_next_step_handler(message,answerH1)


def answerH1(message):#Проверка 1 вопроса на правильность, тест 8
	global EIGHTcount
	if message.text=='1662':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTcount+=1
		answerH2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTcount+=0
		answerH2(message)
	

def answerH2(message):#Вопрос 2, тест 8
	global EIGHTcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1646')
	itemTWO=types.KeyboardButton('1647')
	itemTHREE=types.KeyboardButton('1648')
	itemFOUR=types.KeyboardButton('1649')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был Соляной бунт?", reply_markup=markup)
	bot.register_next_step_handler(message, answerH3)


def answerH3(message):#Проверка 2 вопроса на правильность, тест 8
	global EIGHTcount
	if message.text=='1648':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTcount+=1
		answerH4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTcount+=0
		answerH4(message)


def answerH4(message):#Вопрос 3, тест 8
	global EIGHTcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1645-1676')
	itemTWO=types.KeyboardButton('1639-1667')
	itemTHREE=types.KeyboardButton('1643-1671')
	itemFOUR=types.KeyboardButton('1649-1686')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Годы правления Алексея Михайловича?", reply_markup=markup)
	bot.register_next_step_handler(message, answerH5)


def answerH5(message):#Проверка 3 вопроса на правильность, тест 8
	global EIGHTcount
	if message.text=='1645-1676':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTcount+=1
		answerH6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTcount+=0
		answerH6(message)


def answerH6(message):#Вопрос 4, тест 8
	global EIGHTcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1651')
	itemTWO=types.KeyboardButton('1652')
	itemTHREE=types.KeyboardButton('1653')
	itemFOUR=types.KeyboardButton('1654')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Переяславская Рада, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerH7)


def answerH7(message):#Проверка 4 вопроса на правильность, тест 8
	global EIGHTcount
	if message.text=='1654':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTcount+=1
		answerH8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTcount+=0
		answerH8(message)


def answerH8(message):#Вопрос 5, тест 8
	global EIGHTcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1667')
	itemTWO=types.KeyboardButton('1670')
	itemTHREE=types.KeyboardButton('1673')
	itemFOUR=types.KeyboardButton('1676')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году началась Крестьянская война Степана Разина?", reply_markup=markup)
	bot.register_next_step_handler(message, answerH9)


def answerH9(message):#Проверка 5 вопроса на правильность, тест 8
	global EIGHTcount
	if message.text=='1670':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTcount+=1
		answerH10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTcount+=0
		answerH10(message)


def answerH10(message):#Подсчёт результатов, тест 8
	global EIGHTcount
	if EIGHTcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceH1(message)
	elif EIGHTcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceH1(message)
	elif EIGHTcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceH1(message)
	elif (EIGHTcount==2) or (EIGHTcount==1) or (EIGHTcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceH1(message)


def choiceH1(message):#Что делать дальше, тест 8
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceH2)
		

def choiceH2(message):#Выбор действия, тест 8
	if message.text=='Пройти тест снова':
		question8(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question9(message):#Вопрос 1, тест 9
	global NINEcount
	NINEcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1669')
	itemTWO=types.KeyboardButton('1668')
	itemTHREE=types.KeyboardButton('1666')
	itemFOUR=types.KeyboardButton('1667')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Новоторговый устав, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message,answerI1)


def answerI1(message):#Проверка 1 вопроса на правильность, тест 9
	global NINEcount
	if message.text=='1667':
		bot.send_message(message.chat.id, "Ответ верный")
		NINEcount+=1
		answerI2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		NINEcount+=0
		answerI2(message)
	

def answerI2(message):#Вопрос 2, тест 9
	global NINEcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1607')
	itemTWO=types.KeyboardButton('1609')
	itemTHREE=types.KeyboardButton('1610')
	itemFOUR=types.KeyboardButton('1611')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Осада поляками Смоленска, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerI3)


def answerI3(message):#Проверка 2 вопроса на правильность, тест 9
	global NINEcount
	if message.text=='1609':
		bot.send_message(message.chat.id, "Ответ верный")
		NINEcount+=1
		answerI4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		NINEcount+=0
		answerI4(message)


def answerI4(message):#Вопрос 3, тест 9
	global NINEcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1611')
	itemTWO=types.KeyboardButton('1613')
	itemTHREE=types.KeyboardButton('1614')
	itemFOUR=types.KeyboardButton('1617')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Начало царствования Романовых, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerI5)


def answerI5(message):#Проверка 3 вопроса на правильность, тест 9
	global NINEcount
	if message.text=='1613':
		bot.send_message(message.chat.id, "Ответ верный")
		NINEcount+=1
		answerI6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		NINEcount+=0
		answerI6(message)


def answerI6(message):#Вопрос 4, тест 9
	global NINEcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1605')
	itemTWO=types.KeyboardButton('1606')
	itemTHREE=types.KeyboardButton('1604')
	itemFOUR=types.KeyboardButton('1603')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году произошло воцарение Лжедмитрия I?", reply_markup=markup)
	bot.register_next_step_handler(message, answerI7)


def answerI7(message):#Проверка 4 вопроса на правильность, тест 9
	global NINEcount
	if message.text=='1605':
		bot.send_message(message.chat.id, "Ответ верный")
		NINEcount+=1
		answerI8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		NINEcount+=0
		answerI8(message)


def answerI8(message):#Вопрос 5, тест 9
	global NINEcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1651')
	itemTWO=types.KeyboardButton('1649')
	itemTHREE=types.KeyboardButton('1647')
	itemFOUR=types.KeyboardButton('1644')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Принятие Соборного уложения Алексея Михайловича, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerI9)


def answerI9(message):#Проверка 5 вопроса на правильность, тест 9
	global NINEcount
	if message.text=='1649':
		bot.send_message(message.chat.id, "Ответ верный")
		NINEcount+=1
		answerI10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		NINEcount+=0
		answerI10(message)


def answerI10(message):#Подсчёт результатов, тест 9
	global NINEcount
	if NINEcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceI1(message)
	elif NINEcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceI1(message)
	elif NINEcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceI1(message)
	elif (NINEcount==2) or (NINEcount==1) or (NINEcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceI1(message)


def choiceI1(message):#Что делать дальше, тест 9
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceI2)
		

def choiceI2(message):#Выбор действия, тест 9
	if message.text=='Пройти тест снова':
		question9(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question10(message):#Вопрос 1, тест 10
	global TENcount
	TENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1720')
	itemTWO=types.KeyboardButton('1721')
	itemTHREE=types.KeyboardButton('1722')
	itemFOUR=types.KeyboardButton('1723')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был заключён Ништадтский мир?", reply_markup=markup)
	bot.register_next_step_handler(message,answerJ1)


def answerJ1(message):#Проверка 1 вопроса на правильность, тест 10
	global TENcount
	if message.text=='1721':
		bot.send_message(message.chat.id, "Ответ верный")
		TENcount+=1
		answerJ2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TENcount+=0
		answerJ2(message)
	

def answerJ2(message):#Вопрос 2, тест 10
	global TENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1766')
	itemTWO=types.KeyboardButton('1777')
	itemTHREE=types.KeyboardButton('1776')
	itemFOUR=types.KeyboardButton('1767')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Созыв Уложенной комиссии, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerJ3)


def answerJ3(message):#Проверка 2 вопроса на правильность, тест 10
	global TENcount
	if message.text=='1767':
		bot.send_message(message.chat.id, "Ответ верный")
		TENcount+=1
		answerJ4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TENcount+=0
		answerJ4(message)


def answerJ4(message):#Вопрос 3, тест 10
	global TENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1772')
	itemTWO=types.KeyboardButton('1775')
	itemTHREE=types.KeyboardButton('1771')
	itemFOUR=types.KeyboardButton('1779')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был первый раздел Польши?", reply_markup=markup)
	bot.register_next_step_handler(message, answerJ5)


def answerJ5(message):#Проверка 3 вопроса на правильность, тест 10
	global TENcount
	if message.text=='1772':
		bot.send_message(message.chat.id, "Ответ верный")
		TENcount+=1
		answerJ6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TENcount+=0
		answerJ6(message)


def answerJ6(message):#Вопрос 4, тест 10
	global TENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1781')
	itemTWO=types.KeyboardButton('1783')
	itemTHREE=types.KeyboardButton('1785')
	itemFOUR=types.KeyboardButton('1787')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Жалованная грамота дворянству, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerJ7)


def answerJ7(message):#Проверка 4 вопроса на правильность, тест 10
	global TENcount
	if message.text=='1785':
		bot.send_message(message.chat.id, "Ответ верный")
		TENcount+=1
		answerJ8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TENcount+=0
		answerJ8(message)


def answerJ8(message):#Вопрос 5, тест 10
	global TENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1714')
	itemTWO=types.KeyboardButton('1713')
	itemTHREE=types.KeyboardButton('1716')
	itemFOUR=types.KeyboardButton('1707')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был подписан указ о единонаследии?", reply_markup=markup)
	bot.register_next_step_handler(message, answerJ9)


def answerJ9(message):#Проверка 5 вопроса на правильность, тест 10
	global TENcount
	if message.text=='1714':
		bot.send_message(message.chat.id, "Ответ верный")
		TENcount+=1
		answerJ10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TENcount+=0
		answerJ10(message)


def answerJ10(message):#Подсчёт результатов, тест 10
	global TENcount
	if TENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceJ1(message)
	elif TENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceJ1(message)
	elif TENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceJ1(message)
	elif (TENcount==2) or (TENcount==1) or (TENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceJ1(message)
	

def choiceJ1(message):#Что делать дальше, тест 10
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceJ2)
		

def choiceJ2(message):#Выбор действия, тест 10
	if message.text=='Пройти тест снова':
		question10(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question11(message):#Вопрос 1, тест 11
	global ELEVENcount
	ELEVENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1701')
	itemTWO=types.KeyboardButton('1709')
	itemTHREE=types.KeyboardButton('1711')
	itemFOUR=types.KeyboardButton('1717')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было Полтавское сражение?", reply_markup=markup)
	bot.register_next_step_handler(message,answerK1)


def answerK1(message):#Проверка 1 вопроса на правильность, тест 11
	global ELEVENcount
	if message.text=='1709':
		bot.send_message(message.chat.id, "Ответ верный")
		ELEVENcount+=1
		answerK2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ELEVENcount+=0
		answerK2(message)
	

def answerK2(message):#Вопрос 2, тест 11
	global ELEVENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1785')
	itemTWO=types.KeyboardButton('1788')
	itemTHREE=types.KeyboardButton('1789')
	itemFOUR=types.KeyboardButton('1793')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Взятие крепости Очаков, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerK3)


def answerK3(message):#Проверка 2 вопроса на правильность, тест 11
	global ELEVENcount
	if message.text=='1788':
		bot.send_message(message.chat.id, "Ответ верный")
		ELEVENcount+=1
		answerK4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ELEVENcount+=0
		answerK4(message)


def answerK4(message):#Вопрос 3, тест 11
	global ELEVENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1717')
	itemTWO=types.KeyboardButton('1714')
	itemTHREE=types.KeyboardButton('1712')
	itemFOUR=types.KeyboardButton('1711')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был заключён Прутский договор с Турцией?", reply_markup=markup)
	bot.register_next_step_handler(message, answerK5)


def answerK5(message):#Проверка 3 вопроса на правильность, тест 11
	global ELEVENcount
	if message.text=='1711':
		bot.send_message(message.chat.id, "Ответ верный")
		ELEVENcount+=1
		answerK6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ELEVENcount+=0
		answerK6(message)


def answerK6(message):#Вопрос 4, тест 11
	global ELEVENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1721')
	itemTWO=types.KeyboardButton('1722')
	itemTHREE=types.KeyboardButton('1723')
	itemFOUR=types.KeyboardButton('1724')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Учреждение Синода, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerK7)


def answerK7(message):#Проверка 4 вопроса на правильность, тест 11
	global ELEVENcount
	if message.text=='1721':
		bot.send_message(message.chat.id, "Ответ верный")
		ELEVENcount+=1
		answerK8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ELEVENcount+=0
		answerK8(message)


def answerK8(message):#Вопрос 5, тест 11
	global ELEVENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1788')
	itemTWO=types.KeyboardButton('1773')
	itemTHREE=types.KeyboardButton('1790')
	itemFOUR=types.KeyboardButton('1793')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Взятие русскими войсками турецкой крепости Измаил, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerK9)


def answerK9(message):#Проверка 5 вопроса на правильность, тест 11
	global ELEVENcount
	if message.text=='1790':
		bot.send_message(message.chat.id, "Ответ верный")
		ELEVENcount+=1
		answerK10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		ELEVENcount+=0
		answerK10(message)


def answerK10(message):#Подсчёт результатов, тест 11
	global ELEVENcount
	if ELEVENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceK1(message)
	elif ELEVENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceK1(message)
	elif ELEVENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceK1(message)
	elif (ELEVENcount==2) or (ELEVENcount==1) or (ELEVENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceK1(message)


def choiceK1(message):#Что делать дальше, тест 11
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceK2)
		

def choiceK2(message):#Выбор действия, тест 11
	if message.text=='Пройти тест снова':
		question11(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question12(message):#Вопрос 1, тест 12
	global TWELVEcount
	TWELVEcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1762')
	itemTWO=types.KeyboardButton('1763')
	itemTHREE=types.KeyboardButton('1764')
	itemFOUR=types.KeyboardButton('1765')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Создание Вольного экономического общества, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message,answerL1)


def answerL1(message):#Проверка 1 вопроса на правильность, тест 12
	global TWELVEcount
	if message.text=='1765':
		bot.send_message(message.chat.id, "Ответ верный")
		TWELVEcount+=1
		answerL2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWELVEcount+=0
		answerL2(message)
	

def answerL2(message):#Вопрос 2, тест 12
	global TWELVEcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1790')
	itemTWO=types.KeyboardButton('1795')
	itemTHREE=types.KeyboardButton('1797')
	itemFOUR=types.KeyboardButton('1799')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был третий раздел Речи Посполитой?", reply_markup=markup)
	bot.register_next_step_handler(message, answerL3)


def answerL3(message):#Проверка 2 вопроса на правильность, тест 12
	global TWELVEcount
	if message.text=='1795':
		bot.send_message(message.chat.id, "Ответ верный")
		TWELVEcount+=1
		answerL4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWELVEcount+=0
		answerL4(message)


def answerL4(message):#Вопрос 3, тест 12
	global TWELVEcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1750')
	itemTWO=types.KeyboardButton('1753')
	itemTHREE=types.KeyboardButton('1755')
	itemFOUR=types.KeyboardButton('1757')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Основание Московского университета, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerL5)


def answerL5(message):#Проверка 3 вопроса на правильность, тест 12
	global TWELVEcount
	if message.text=='1755':
		bot.send_message(message.chat.id, "Ответ верный")
		TWELVEcount+=1
		answerL6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWELVEcount+=0
		answerL6(message)


def answerL6(message):#Вопрос 4, тест 12
	global TWELVEcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1797')
	itemTWO=types.KeyboardButton('1798')
	itemTHREE=types.KeyboardButton('1799')
	itemFOUR=types.KeyboardButton('1800')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году были Итальянский и Швейцарский походы А. В. Суворова?", reply_markup=markup)
	bot.register_next_step_handler(message, answerL7)


def answerL7(message):#Проверка 4 вопроса на правильность, тест 12
	global TWELVEcount
	if message.text=='1799':
		bot.send_message(message.chat.id, "Ответ верный")
		TWELVEcount+=1
		answerL8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWELVEcount+=0
		answerL8(message)


def answerL8(message):#Вопрос 5, тест 12
	global TWELVEcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1725')
	itemTWO=types.KeyboardButton('1727')
	itemTHREE=types.KeyboardButton('1723')
	itemFOUR=types.KeyboardButton('1721')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Учреждение Академии наук, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerL9)


def answerL9(message):#Проверка 5 вопроса на правильность, тест 12
	global TWELVEcount
	if message.text=='1725':
		bot.send_message(message.chat.id, "Ответ верный")
		TWELVEcount+=1
		answerL10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		TWELVEcount+=0
		answerL10(message)


def answerL10(message):#Подсчёт результатов, тест 12
	global TWELVEcount
	if TWELVEcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceL1(message)
	elif TWELVEcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceL1(message)
	elif TWELVEcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceL1(message)
	elif (TWELVEcount==2) or (TWELVEcount==1) or (TWELVEcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceL1(message)


def choiceL1(message):#Что делать дальше, тест 12
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceL2)
		

def choiceL2(message):#Выбор действия, тест 12
	if message.text=='Пройти тест снова':
		question12(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question13(message):#Вопрос 1, тест 13
	global THIRTEENcount
	THIRTEENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1823')
	itemTWO=types.KeyboardButton('1825')
	itemTHREE=types.KeyboardButton('1826')
	itemFOUR=types.KeyboardButton('1829')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было восстание декабристов?", reply_markup=markup)
	bot.register_next_step_handler(message,answerM1)


def answerM1(message):#Проверка 1 вопроса на правильность, тест 13
	global THIRTEENcount
	if message.text=='1825':
		bot.send_message(message.chat.id, "Ответ верный")
		THIRTEENcount+=1
		answerM2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		THIRTEENcount+=0
		answerM2(message)
	

def answerM2(message):#Вопрос 2, тест 13
	global THIRTEENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1811')
	itemTWO=types.KeyboardButton('1812')
	itemTHREE=types.KeyboardButton('1813')
	itemFOUR=types.KeyboardButton('1814')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году была Бородинская битва?", reply_markup=markup)
	bot.register_next_step_handler(message, answerM3)


def answerM3(message):#Проверка 2 вопроса на правильность, тест 13
	global THIRTEENcount
	if message.text=='1812':
		bot.send_message(message.chat.id, "Ответ верный")
		THIRTEENcount+=1
		answerM4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		THIRTEENcount+=0
		answerM4(message)


def answerM4(message):#Вопрос 3, тест 13
	global THIRTEENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1850')
	itemTWO=types.KeyboardButton('1854')
	itemTHREE=types.KeyboardButton('1855')
	itemFOUR=types.KeyboardButton('1856')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был заключён Парижский мир?", reply_markup=markup)
	bot.register_next_step_handler(message, answerM5)


def answerM5(message):#Проверка 3 вопроса на правильность, тест 13
	global THIRTEENcount
	if message.text=='1856':
		bot.send_message(message.chat.id, "Ответ верный")
		THIRTEENcount+=1
		answerM6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		THIRTEENcount+=0
		answerM6(message)


def answerM6(message):#Вопрос 4, тест 13
	global THIRTEENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1819')
	itemTWO=types.KeyboardButton('1813')
	itemTHREE=types.KeyboardButton('1817')
	itemFOUR=types.KeyboardButton('1815')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году была «битва народов»?", reply_markup=markup)
	bot.register_next_step_handler(message, answerM7)


def answerM7(message):#Проверка 4 вопроса на правильность, тест 13
	global THIRTEENcount
	if message.text=='1813':
		bot.send_message(message.chat.id, "Ответ верный")
		THIRTEENcount+=1
		answerM8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		THIRTEENcount+=0
		answerM8(message)


def answerM8(message):#Вопрос 5, тест 13
	global THIRTEENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1821-1853')
	itemTWO=types.KeyboardButton('1827-1859')
	itemTHREE=types.KeyboardButton('1829-1854')
	itemFOUR=types.KeyboardButton('1825-1855')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Годы правления Николая I?", reply_markup=markup)
	bot.register_next_step_handler(message, answerM9)


def answerM9(message):#Проверка 5 вопроса на правильность, тест 13
	global THIRTEENcount
	if message.text=='1825-1855':
		bot.send_message(message.chat.id, "Ответ верный")
		THIRTEENcount+=1
		answerM10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		THIRTEENcount+=0
		answerM10(message)


def answerM10(message):#Подсчёт результатов, тест 13
	global THIRTEENcount
	if THIRTEENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceM1(message)
	elif THIRTEENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceM1(message)
	elif THIRTEENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceM1(message)
	elif (THIRTEENcount==2) or (THIRTEENcount==1) or (THIRTEENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceM1(message)


def choiceM1(message):#Что делать дальше, тест 13
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceM2)
		

def choiceM2(message):#Выбор действия, тест 13
	if message.text=='Пройти тест снова':
		question13(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question14(message):#Вопрос 1, тест 14
	global FOURTEENcount
	FOURTEENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1889')
	itemTWO=types.KeyboardButton('1884')
	itemTHREE=types.KeyboardButton('1887')
	itemFOUR=types.KeyboardButton('1881')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Циркуляр о кухаркиных детях, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message,answerN1)


def answerN1(message):#Проверка 1 вопроса на правильность, тест 14
	global FOURTEENcount
	if message.text=='1887':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURTEENcount+=1
		answerN2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURTEENcount+=0
		answerN2(message)
	

def answerN2(message):#Вопрос 2, тест 14
	global FOURTEENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1837')
	itemTWO=types.KeyboardButton('1833')
	itemTHREE=types.KeyboardButton('1839')
	itemFOUR=types.KeyboardButton('1831')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Строительство первой железной дороги, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerN3)


def answerN3(message):#Проверка 2 вопроса на правильность, тест 14
	global FOURTEENcount
	if message.text=='1837':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURTEENcount+=1
		answerN4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURTEENcount+=0
		answerN4(message)


def answerN4(message):#Вопрос 3, тест 14
	global FOURTEENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1859')
	itemTWO=types.KeyboardButton('1851')
	itemTHREE=types.KeyboardButton('1853')
	itemFOUR=types.KeyboardButton('1856')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Окончание Крымской войны, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerN5)


def answerN5(message):#Проверка 3 вопроса на правильность, тест 14
	global FOURTEENcount
	if message.text=='1856':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURTEENcount+=1
		answerN6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURTEENcount+=0
		answerN6(message)


def answerN6(message):#Вопрос 4, тест 14
	global FOURTEENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1857')
	itemTWO=types.KeyboardButton('1855')
	itemTHREE=types.KeyboardButton('1851')
	itemFOUR=types.KeyboardButton('1853')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Синопский бой, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerN7)


def answerN7(message):#Проверка 4 вопроса на правильность, тест 14
	global FOURTEENcount
	if message.text=='1853':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURTEENcount+=1
		answerN8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURTEENcount+=0
		answerN8(message)


def answerN8(message):#Вопрос 5, тест 14
	global FOURTEENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1873-1877')
	itemTWO=types.KeyboardButton('1877-1878')
	itemTHREE=types.KeyboardButton('1879-1873')
	itemFOUR=types.KeyboardButton('1875-1879')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Оборона Шипки, какие годы?", reply_markup=markup)
	bot.register_next_step_handler(message, answerN9)


def answerN9(message):#Проверка 5 вопроса на правильность, тест 14
	global FOURTEENcount
	if message.text=='1877-1878':
		bot.send_message(message.chat.id, "Ответ верный")
		FOURTEENcount+=1
		answerN10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FOURTEENcount+=0
		answerN10(message)


def answerN10(message):#Подсчёт результатов, тест 14
	global FOURTEENcount
	if FOURTEENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceN1(message)
	elif FOURTEENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceN1(message)
	elif FOURTEENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceN1(message)
	elif (FOURTEENcount==2) or (FOURTEENcount==1) or (FOURTEENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceN1(message)


def choiceN1(message):#Что делать дальше, тест 14
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceN2)
		

def choiceN2(message):#Выбор действия, тест 14
	if message.text=='Пройти тест снова':
		question14(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question15(message):#Вопрос 1, тест 15
	global FIFTEENcount
	FIFTEENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1815')
	itemTWO=types.KeyboardButton('1813')
	itemTHREE=types.KeyboardButton('1809')
	itemFOUR=types.KeyboardButton('1810')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было учреждение Государственного совета?", reply_markup=markup)
	bot.register_next_step_handler(message,answerO1)


def answerO1(message):#Проверка 1 вопроса на правильность, тест 15
	global FIFTEENcount
	if message.text=='1810':
		bot.send_message(message.chat.id, "Ответ верный")
		FIFTEENcount+=1
		answerO2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIFTEENcount+=0
		answerO2(message)
	

def answerO2(message):#Вопрос 2, тест 15
	global FIFTEENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1802')
	itemTWO=types.KeyboardButton('1803')
	itemTHREE=types.KeyboardButton('1804')
	itemFOUR=types.KeyboardButton('1805')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году было учреждение первых министерств?", reply_markup=markup)
	bot.register_next_step_handler(message, answerO3)


def answerO3(message):#Проверка 2 вопроса на правильность, тест 15
	global FIFTEENcount
	if message.text=='1802':
		bot.send_message(message.chat.id, "Ответ верный")
		FIFTEENcount+=1
		answerO4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIFTEENcount+=0
		answerO4(message)


def answerO4(message):#Вопрос 3, тест 15
	global FIFTEENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1835-1849')
	itemTWO=types.KeyboardButton('1833-1847')
	itemTHREE=types.KeyboardButton('1839-1843')
	itemFOUR=types.KeyboardButton('1836-1840')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Денежная реформа Е. Ф. Канкрина, какие годы?", reply_markup=markup)
	bot.register_next_step_handler(message, answerO5)


def answerO5(message):#Проверка 3 вопроса на правильность, тест 15
	global FIFTEENcount
	if message.text=='1839-1843':
		bot.send_message(message.chat.id, "Ответ верный")
		FIFTEENcount+=1
		answerO6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIFTEENcount+=0
		answerO6(message)


def answerO6(message):#Вопрос 4, тест 15
	global FIFTEENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1885')
	itemTWO=types.KeyboardButton('1879')
	itemTHREE=types.KeyboardButton('1881')
	itemFOUR=types.KeyboardButton('1880')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Убийство Александра II, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerO7)


def answerO7(message):#Проверка 4 вопроса на правильность, тест 15
	global FIFTEENcount
	if message.text=='1881':
		bot.send_message(message.chat.id, "Ответ верный")
		FIFTEENcount+=1
		answerO8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIFTEENcount+=0
		answerO8(message)


def answerO8(message):#Вопрос 5, тест 15
	global FIFTEENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1842')
	itemTWO=types.KeyboardButton('1845')
	itemTHREE=types.KeyboardButton('1844')
	itemFOUR=types.KeyboardButton('1843')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году была первая сельскохозяйственная выставка в России?", reply_markup=markup)
	bot.register_next_step_handler(message, answerO9)


def answerO9(message):#Проверка 5 вопроса на правильность, тест 15
	global FIFTEENcount
	if message.text=='1843':
		bot.send_message(message.chat.id, "Ответ верный")
		FIFTEENcount+=1
		answerO10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		FIFTEENcount+=0
		answerO10(message)


def answerO10(message):#Подсчёт результатов, тест 15
	global FIFTEENcount
	if FIFTEENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceO1(message)
	elif FIFTEENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceO1(message)
	elif FIFTEENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceO1(message)
	elif (FIFTEENcount==2) or (FIFTEENcount==1) or (FIFTEENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceO1(message)


def choiceO1(message):#Что делать дальше, тест 15
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceO2)
		

def choiceO2(message):#Выбор действия, тест 15
	if message.text=='Пройти тест снова':
		question15(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question16(message):#Вопрос 1, тест 16
	global SIXTEENcount
	SIXTEENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1958')
	itemTWO=types.KeyboardButton('1963')
	itemTHREE=types.KeyboardButton('1962')
	itemFOUR=types.KeyboardButton('1965')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был Карибский кризис?", reply_markup=markup)
	bot.register_next_step_handler(message,answerP1)


def answerP1(message):#Проверка 1 вопроса на правильность, тест 16
	global SIXTEENcount
	if message.text=='1962':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXTEENcount+=1
		answerP2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXTEENcount+=0
		answerP2(message)
	

def answerP2(message):#Вопрос 2, тест 16
	global SIXTEENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1942')
	itemTWO=types.KeyboardButton('1941')
	itemTHREE=types.KeyboardButton('1939')
	itemFOUR=types.KeyboardButton('1945')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Год начала Великой Отечественной войны?", reply_markup=markup)
	bot.register_next_step_handler(message, answerP3)


def answerP3(message):#Проверка 2 вопроса на правильность, тест 16
	global SIXTEENcount
	if message.text=='1941':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXTEENcount+=1
		answerP4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXTEENcount+=0
		answerP4(message)


def answerP4(message):#Вопрос 3, тест 16
	global SIXTEENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1941')
	itemTWO=types.KeyboardButton('1942')
	itemTHREE=types.KeyboardButton('1943')
	itemFOUR=types.KeyboardButton('1944')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году была Курская битва?", reply_markup=markup)
	bot.register_next_step_handler(message, answerP5)


def answerP5(message):#Проверка 3 вопроса на правильность, тест 16
	global SIXTEENcount
	if message.text=='1943':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXTEENcount+=1
		answerP6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXTEENcount+=0
		answerP6(message)


def answerP6(message):#Вопрос 4, тест 16
	global SIXTEENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1960')
	itemTWO=types.KeyboardButton('1964')
	itemTHREE=types.KeyboardButton('1968')
	itemFOUR=types.KeyboardButton('1970')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Подавление Пражской весны, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerP7)


def answerP7(message):#Проверка 4 вопроса на правильность, тест 16
	global SIXTEENcount
	if message.text=='1968':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXTEENcount+=1
		answerP8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXTEENcount+=0
		answerP8(message)


def answerP8(message):#Вопрос 5, тест 16
	global SIXTEENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1983-1989')
	itemTWO=types.KeyboardButton('1984-1990')
	itemTHREE=types.KeyboardButton('1985-1991')
	itemFOUR=types.KeyboardButton('1986-1992')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Годы перестройки?", reply_markup=markup)
	bot.register_next_step_handler(message, answerP9)


def answerP9(message):#Проверка 5 вопроса на правильность, тест 16
	global SIXTEENcount
	if message.text=='1985-1991':
		bot.send_message(message.chat.id, "Ответ верный")
		SIXTEENcount+=1
		answerP10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SIXTEENcount+=0
		answerP10(message)


def answerP10(message):#Подсчёт результатов, тест 16
	global SIXTEENcount
	if SIXTEENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceP1(message)
	elif SIXTEENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceP1(message)
	elif SIXTEENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceP1(message)
	elif (SIXTEENcount==2) or (SIXTEENcount==1) or (SIXTEENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceP1(message)


def choiceP1(message):#Что делать дальше, тест 16
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceP2)
		

def choiceP2(message):#Выбор действия, тест 16
	if message.text=='Пройти тест снова':
		question16(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question17(message):#Вопрос 1, тест 17
	global SEVENTEENcount
	SEVENTEENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1918')
	itemTWO=types.KeyboardButton('1919')
	itemTHREE=types.KeyboardButton('1917')
	itemFOUR=types.KeyboardButton('1916')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был заключён Брестский мир?", reply_markup=markup)
	bot.register_next_step_handler(message,answerQ1)


def answerQ1(message):#Проверка 1 вопроса на правильность, тест 17
	global SEVENTEENcount
	if message.text=='1918':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENTEENcount+=1
		answerQ2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENTEENcount+=0
		answerQ2(message)
	

def answerQ2(message):#Вопрос 2, тест 17
	global SEVENTEENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1977')
	itemTWO=types.KeyboardButton('1975')
	itemTHREE=types.KeyboardButton('1980')
	itemFOUR=types.KeyboardButton('1979')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Ввод советских войск в Афганистан, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerQ3)


def answerQ3(message):#Проверка 2 вопроса на правильность, тест 17
	global SEVENTEENcount
	if message.text=='1979':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENTEENcount+=1
		answerQ4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENTEENcount+=0
		answerQ4(message)


def answerQ4(message):#Вопрос 3, тест 17
	global SEVENTEENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1941')
	itemTWO=types.KeyboardButton('1943')
	itemTHREE=types.KeyboardButton('1945')
	itemFOUR=types.KeyboardButton('1947')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Ялтинская конференция, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerQ5)


def answerQ5(message):#Проверка 3 вопроса на правильность, тест 17
	global SEVENTEENcount
	if message.text=='1945':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENTEENcount+=1
		answerQ6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENTEENcount+=0
		answerQ6(message)


def answerQ6(message):#Вопрос 4, тест 17
	global SEVENTEENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1940')
	itemTWO=types.KeyboardButton('1941')
	itemTHREE=types.KeyboardButton('1939')
	itemFOUR=types.KeyboardButton('1938')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Начало Второй мировой войны, какой год?", reply_markup=markup)
	bot.register_next_step_handler(message, answerQ7)


def answerQ7(message):#Проверка 4 вопроса на правильность, тест 17
	global SEVENTEENcount
	if message.text=='1939':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENTEENcount+=1
		answerQ8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENTEENcount+=0
		answerQ8(message)


def answerQ8(message):#Вопрос 5, тест 17
	global SEVENTEENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1969')
	itemTWO=types.KeyboardButton('1966')
	itemTHREE=types.KeyboardButton('1967')
	itemFOUR=types.KeyboardButton('1968')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был Чехословацкий кризис?", reply_markup=markup)
	bot.register_next_step_handler(message, answerQ9)


def answerQ9(message):#Проверка 5 вопроса на правильность, тест 17
	global SEVENTEENcount
	if message.text=='1968':
		bot.send_message(message.chat.id, "Ответ верный")
		SEVENTEENcount+=1
		answerQ10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		SEVENTEENcount+=0
		answerQ10(message)


def answerQ10(message):#Подсчёт результатов, тест 17
	global SEVENTEENcount
	if SEVENTEENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceQ1(message)
	elif SEVENTEENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceQ1(message)
	elif SEVENTEENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceQ1(message)
	elif (SEVENTEENcount==2) or (SEVENTEENcount==1) or (SEVENTEENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceQ1(message)


def choiceQ1(message):#Что делать дальше, тест 17
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceQ2)
		

def choiceQ2(message):#Выбор действия, тест 17
	if message.text=='Пройти тест снова':
		question17(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)


def question18(message):#Вопрос 1, тест 18
	global EIGHTEENcount
	EIGHTEENcount=0
	bot.send_message(message.chat.id, "Тогда начинаем")
	bot.send_message(message.chat.id, "Вопрос первый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1953')
	itemTWO=types.KeyboardButton('1956')
	itemTHREE=types.KeyboardButton('1959')
	itemFOUR=types.KeyboardButton('1965')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "В каком году был Венгерский кризис?", reply_markup=markup)
	bot.register_next_step_handler(message,answerR1)


def answerR1(message):#Проверка 1 вопроса на правильность, тест 18
	global EIGHTEENcount
	if message.text=='1956':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTEENcount+=1
		answerR2(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTEENcount+=0
		answerR2(message)
	

def answerR2(message):#Вопрос 2, тест 18
	global EIGHTEENcount			
	bot.send_message(message.chat.id, "Вопрос второй")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1950-1953')
	itemTWO=types.KeyboardButton('1951-1954')
	itemTHREE=types.KeyboardButton('1952-1955')
	itemFOUR=types.KeyboardButton('1953-1956')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Годы Корейской войны?", reply_markup=markup)
	bot.register_next_step_handler(message, answerR3)


def answerR3(message):#Проверка 2 вопроса на правильность, тест 18
	global EIGHTEENcount
	if message.text=='1950-1953':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTEENcount+=1
		answerR4(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTEENcount+=0
		answerR4(message)


def answerR4(message):#Вопрос 3, тест 18
	global EIGHTEENcount			
	bot.send_message(message.chat.id, "Вопрос третий")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1901')
	itemTWO=types.KeyboardButton('1904')
	itemTHREE=types.KeyboardButton('1905')
	itemFOUR=types.KeyboardButton('1909')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Год Цусимского сражения?", reply_markup=markup)
	bot.register_next_step_handler(message, answerR5)


def answerR5(message):#Проверка 3 вопроса на правильность, тест 18
	global EIGHTEENcount
	if message.text=='1905':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTEENcount+=1
		answerR6(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTEENcount+=0
		answerR6(message)


def answerR6(message):#Вопрос 4, тест 18
	global EIGHTEENcount		
	bot.send_message(message.chat.id, "Вопрос четвёртый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1920')
	itemTWO=types.KeyboardButton('1922')
	itemTHREE=types.KeyboardButton('1924')
	itemFOUR=types.KeyboardButton('1926')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Год завершения Гражданской войны на Дальнем Востоке?", reply_markup=markup)
	bot.register_next_step_handler(message, answerR7)


def answerR7(message):#Проверка 4 вопроса на правильность, тест 18
	global EIGHTEENcount
	if message.text=='1922':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTEENcount+=1
		answerR8(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTEENcount+=0
		answerR8(message)


def answerR8(message):#Вопрос 5, тест 18
	global EIGHTEENcount			
	bot.send_message(message.chat.id, "Вопрос пятый")
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('1901')
	itemTWO=types.KeyboardButton('1904')
	itemTHREE=types.KeyboardButton('1903')
	itemFOUR=types.KeyboardButton('1900')
	markup.row(itemONE, itemTWO)
	markup.row(itemTHREE, itemFOUR)
	bot.send_message(message.chat.id, "Год Ляоянского сражения?", reply_markup=markup)
	bot.register_next_step_handler(message, answerR9)


def answerR9(message):#Проверка 5 вопроса на правильность, тест 18
	global EIGHTEENcount
	if message.text=='1904':
		bot.send_message(message.chat.id, "Ответ верный")
		EIGHTEENcount+=1
		answerR10(message)
	else:
		bot.send_message(message.chat.id, "Ответ не верный")
		EIGHTEENcount+=0
		answerR10(message)


def answerR10(message):#Подсчёт результатов, тест 18
	global EIGHTEENcount
	if EIGHTEENcount==5:
		bot.send_message(message.chat.id, "Твоя оценка 5")
		choiceR1(message)
	elif EIGHTEENcount==4:
		bot.send_message(message.chat.id, "Твоя оценка 4")
		choiceR1(message)
	elif EIGHTEENcount==3:
		bot.send_message(message.chat.id, "Твоя оценка 3")
		choiceR1(message)
	elif (EIGHTEENcount==2) or (EIGHTEENcount==1) or (EIGHTEENcount==0):
		bot.send_message(message.chat.id, "Твоя оценка 2")
		choiceR1(message)


def choiceR1(message):#Что делать дальше, тест 18
	markup= types.ReplyKeyboardMarkup()
	itemONE=types.KeyboardButton('Пройти тест снова')
	itemTWO=types.KeyboardButton('Выбрать другой тест')
	itemTHREE=types.KeyboardButton('Закончить тестирование')
	markup.row(itemONE, itemTWO, itemTHREE)
	bot.send_message(message.chat.id,"Выбери, что делать дальше.", reply_markup=markup)
	bot.register_next_step_handler(message, choiceR2)
		

def choiceR2(message):#Выбор действия, тест 18
	if message.text=='Пройти тест снова':
		question18(message)
	elif message.text=='Выбрать другой тест':
		send_welcome(message)
	elif message.text=='Закончить тестирование':
		keyboard = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Тестирование закончено." + "\n" + "Если захочешь снова пройти тест, напиши /start",reply_markup=keyboard)

 
bot.polling()