import telebot
from telebot import types
from covid import Covid
import virus
import datetime
covid = Covid()
bot = telebot.TeleBot('Ваш api-ключ')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('Во всём мире')
	btn2 = types.KeyboardButton('Украина')
	btn3 = types.KeyboardButton('Россия')
	btn4 = types.KeyboardButton('Беларусь')
	markup.add(btn1, btn2, btn3, btn4)

	send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные по коронавирусу напишите " \
		f"название страны, например: США, Украина, Россия и так далее\n"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "во всём мире":
		location = covid.get_status_by_country_name("US")
		time = str(location['last_update'])
		active = covid.get_total_active_cases()
		confirmed = covid.get_total_confirmed_cases()
		recovered = covid.get_total_recovered()
		deaths = covid.get_total_deaths()
		final_message = f"<u>Данные по миру:</u>\n<b>Последнее обновление от: {datetime.datetime.fromtimestamp(int(time[:len(time)-3]))} </b>\n<b>Подтвержденных случаев: </b>{confirmed:,}\n<b>Всего заболевших (по миру): </b>{active:,}\n<b>Выздоровевших: </b>{recovered:,}\n<b>Смертей: </b>{deaths:,}"
	else :
		en_country_name = virus.translate_country_name(get_message_bot)
		if en_country_name != 'error':
			location = covid.get_status_by_country_name(en_country_name)
			time = str(location['last_update'])
			final_message = f"<u>Данные по стране: {location['country']}</u>\n<b>Последнее обновление от: {datetime.datetime.fromtimestamp(int(time[:len(time)-3]))} </b>\n<b>Подтвержденных случаев: </b>{location['confirmed']:,}\n<b>Всего заболевших (по стране): </b>{location['active']:,}\n<b>Выздоровевших: </b>{location['recovered']:,}\n<b>Смертей: </b>{location['deaths']:,}"
		else:
			final_message = "Такой страны нет в базе/Введено неправильное название страны/Некорректный запрос"
	bot.send_message(message.chat.id, final_message, parse_mode='html')

# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)