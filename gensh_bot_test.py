from telebot import types
import telebot

import sqlite3
import json


sample = ['Обычная атака:\n', 'Заряженная атака:\n', 'Элементальный навык:\n', 'Особый навык:\n', 'Взрыв стихий:\n', 'Оружие:\n', 'Подбор артефактов:\n']

keyboard1 = types.InlineKeyboardMarkup()
keyboard2 = types.InlineKeyboardMarkup()
keyboard3 = types.InlineKeyboardMarkup()
keyboard4 = types.InlineKeyboardMarkup()
keyboard5 = types.InlineKeyboardMarkup()
keyboard6 = types.InlineKeyboardMarkup()
keyboard7 = types.InlineKeyboardMarkup()
keyboard8 = types.InlineKeyboardMarkup()

#bot = telebot.TeleBot('5885369608:AAG7G3B4VYN0zd8d35NaqXg7_ERhjy6_Vlc')tst
bot = telebot.TeleBot('5843937954:AAEHbkJuSu_eKputHcFWuiPLxMTYmv4V_qM')

key_desc = types.InlineKeyboardButton(text='Сообщить', callback_data='pred')


key_Al = types.InlineKeyboardButton(text='Аль-Хайтам', callback_data='Аль ')
key_YaoYao = types.InlineKeyboardButton(text='Яо Яо ', callback_data='Яо Яо ')
key_Stranger = types.InlineKeyboardButton(text='Странник ', callback_data='Странник ')
key_Faruzan = types.InlineKeyboardButton(text='Фарузан ', callback_data='Фарузан ')
key_Layla = types.InlineKeyboardButton(text='Лайла ', callback_data='Лайла ')
key_Nahida = types.InlineKeyboardButton(text='Нахида ', callback_data='Нахида ')
key_Nilu = types.InlineKeyboardButton(text='Нилу ', callback_data='Нилу ')
key_Sayno = types.InlineKeyboardButton(text='Сайно ', callback_data='Сайно ')
key_Candice = types.InlineKeyboardButton(text='Кандакия ', callback_data='Кандакия ')
key_to2 = types.InlineKeyboardButton(text='след', callback_data='to2')
keyboard1.add(key_Al, key_YaoYao, key_Stranger, key_Faruzan, key_Layla, key_Nahida, key_Nilu, key_Sayno, key_Candice, key_desc, key_to2)

key_Dori = types.InlineKeyboardButton(text='Дори ', callback_data='Дори ')
key_Tignari = types.InlineKeyboardButton(text='Тигнари ', callback_data='Тигнари ')
key_Kollei = types.InlineKeyboardButton(text='Коллеи ', callback_data='Коллеи ')
key_Trav_dendro = types.InlineKeyboardButton(text='Путешественник Дендро ', callback_data='Путешественник Дендро ')
key_Heizo = types.InlineKeyboardButton(text='Хэйдзо ', callback_data='Хэйдзо ')
key_Sinobu = types.InlineKeyboardButton(text='Синобу ', callback_data='Синобу ')
key_Elan = types.InlineKeyboardButton(text='Е Лань ', callback_data='Е Лань ')
key_ayato = types.InlineKeyboardButton(text='Аято ', callback_data='Аято ')
key_Yae = types.InlineKeyboardButton(text='Яэ Мико ', callback_data='Яэ Мико ')
key_to1 = types.InlineKeyboardButton(text='пред', callback_data='to1')
key_to3 = types.InlineKeyboardButton(text='след', callback_data='to3')
keyboard2.add(key_Dori, key_Tignari, key_Kollei, key_Trav_dendro, key_Heizo, key_Sinobu, key_Elan, key_ayato, key_Yae, key_to1, key_desc, key_to3)

key_Shenhe = types.InlineKeyboardButton(text='Шэнь Хэ ', callback_data='Шэнь Хэ ')
key_Yunzhin = types.InlineKeyboardButton(text='Юнь Цзинь ', callback_data='Юнь Цзинь ')
key_Itto = types.InlineKeyboardButton(text='Итто ', callback_data='Итто ')
key_Goro = types.InlineKeyboardButton(text='Горо ', callback_data='Горо ')
key_Toma = types.InlineKeyboardButton(text='Тома ', callback_data='Тома ')
key_Kokomi = types.InlineKeyboardButton(text='Кокоми ', callback_data='Кокоми ')
key_Shogun = types.InlineKeyboardButton(text='Райдэн ', callback_data='Райдэн ')
key_Eloy = types.InlineKeyboardButton(text='Элой ', callback_data='Элой ')
key_Sara = types.InlineKeyboardButton(text='Сара ', callback_data='Сара ')
key_to2 = types.InlineKeyboardButton(text='пред', callback_data='to2')
key_to4 = types.InlineKeyboardButton(text='след', callback_data='to4')
keyboard3.add(key_Shenhe, key_Yunzhin, key_Itto, key_Goro, key_Toma, key_Kokomi, key_Shogun, key_Eloy, key_Sara, key_to2, key_desc, key_to4)

key_Yeimia = types.InlineKeyboardButton(text='Ёимия ', callback_data='Ёимия ')
key_Sau = types.InlineKeyboardButton(text='Саю ', callback_data='Саю ')
key_Trav_electro = types.InlineKeyboardButton(text='Путешественник Электро ', callback_data='Путешественник Электро ')
key_Ayaka = types.InlineKeyboardButton(text='Аяка ', callback_data='Аяка ')
key_Kadzhuha = types.InlineKeyboardButton(text='Кадзуха ', callback_data='Кадзуха ')
key_Aola = types.InlineKeyboardButton(text='Эола ', callback_data='Эола ')
key_YanFey = types.InlineKeyboardButton(text='Янь Фэй ', callback_data='Янь Фэй ')
key_Rosaria = types.InlineKeyboardButton(text='Розария ', callback_data='Розария ')
key_HuTao = types.InlineKeyboardButton(text='Ху Тао ', callback_data='Ху Тао ')
key_to3 = types.InlineKeyboardButton(text='пред', callback_data='to3')
key_to5 = types.InlineKeyboardButton(text='след', callback_data='to5')
keyboard4.add(key_Yeimia, key_Sau, key_Trav_electro, key_Ayaka, key_Kadzhuha, key_Aola, key_YanFey, key_Rosaria, key_HuTao, key_to3, key_desc, key_to5)

key_Sao = types.InlineKeyboardButton(text='Сяо ', callback_data='Сяо ')
key_GanYui = types.InlineKeyboardButton(text='Гань Юй ', callback_data='Гань Юй ')
key_Albedo = types.InlineKeyboardButton(text='Альбедо ', callback_data='Альбедо ')
key_Ghoungli = types.InlineKeyboardButton(text='Чжун Ли ', callback_data='Чжун Ли ')
key_SinYan = types.InlineKeyboardButton(text='Синь Янь ', callback_data='Синь Янь ')
key_Tartaghilia = types.InlineKeyboardButton(text='Чайльд Тарталья ', callback_data='Чайльд Тарталья ')
key_Diona = types.InlineKeyboardButton(text='Диона ', callback_data='Диона ')
key_Kli = types.InlineKeyboardButton(text='Кли ', callback_data='Кли ')
key_Venti = types.InlineKeyboardButton(text='Венти ', callback_data='Венти ')
key_to4 = types.InlineKeyboardButton(text='пред', callback_data='to4')
key_to6 = types.InlineKeyboardButton(text='след', callback_data='to6')
keyboard5.add(key_Sao, key_GanYui, key_Albedo, key_Ghoungli, key_SinYan, key_Tartaghilia, key_Diona, key_Kli, key_Venti, key_to4, key_desc, key_to6)

key_ChiChi = types.InlineKeyboardButton(text='Ци Ци ', callback_data='Ци Ци ')
key_Mona = types.InlineKeyboardButton(text='Мона ', callback_data='Мона ')
key_Kueqing = types.InlineKeyboardButton(text='Кэ Цин ', callback_data='Кэ Цин ')
key_Diluc = types.InlineKeyboardButton(text='Дилюк ', callback_data='Дилюк ')
key_Jean = types.InlineKeyboardButton(text='Джинн ', callback_data='Джинн ')
key_Amber = types.InlineKeyboardButton(text='Эмбер ', callback_data='Эмбер ')
key_ChunYun = types.InlineKeyboardButton(text='Чун Юнь ', callback_data='Чун Юнь ')
key_Fishl = types.InlineKeyboardButton(text='Фишль ', callback_data='Фишль ')
key_Sunlin = types.InlineKeyboardButton(text='Сян Лин ', callback_data='Сян Лин ')
key_to5 = types.InlineKeyboardButton(text='пред', callback_data='to5')
key_to7 = types.InlineKeyboardButton(text='след', callback_data='to7')
keyboard6.add(key_ChiChi, key_Mona, key_Kueqing, key_Diluc, key_Jean, key_Amber, key_ChunYun, key_Fishl, key_Sunlin, key_to5, key_desc, key_to7)

key_Sinzhu = types.InlineKeyboardButton(text='Син Цю ', callback_data='Син Цю ')
key_Sucrose = types.InlineKeyboardButton(text='Сахароза ', callback_data='Сахароза ')
key_Razor = types.InlineKeyboardButton(text='Рэйзор ', callback_data='Рэйзор ')
key_Noele = types.InlineKeyboardButton(text='Ноэлль ', callback_data='Ноэлль ')
key_Nin = types.InlineKeyboardButton(text='Нин Гуан ', callback_data='Нин Гуан ')
key_Liza = types.InlineKeyboardButton(text='Лиза ', callback_data='Лиза ')
key_Keya = types.InlineKeyboardButton(text='Кэйа ', callback_data='Кэйа ')
key_BayDou = types.InlineKeyboardButton(text='Бэй Доу ', callback_data='Бэй Доу ')
key_Bennet = types.InlineKeyboardButton(text='Беннет ', callback_data='Беннет ')
key_to6 = types.InlineKeyboardButton(text='пред', callback_data='to6')
key_to8 = types.InlineKeyboardButton(text='след', callback_data='to8')
keyboard7.add(key_Sinzhu, key_Sucrose, key_Razor, key_Noele, key_Nin, key_Liza, key_Keya, key_BayDou, key_Bennet, key_to6, key_desc, key_to8)


key_Barabara = types.InlineKeyboardButton(text='Барбара ', callback_data='Барбара ')
key_Trav_geo = types.InlineKeyboardButton(text='Путешественник Гео ', callback_data='Путешественник Гео ')
key_Trav_anemo = types.InlineKeyboardButton(text='Путешественник Анемо ', callback_data='Путешественник Анемо ')
key_test = types.InlineKeyboardButton(text='тест', callback_data='test')
key_to7 = types.InlineKeyboardButton(text='пред', callback_data='to7')
keyboard8.add(key_Barabara, key_Trav_geo, key_Trav_anemo, key_to7, key_desc)


key_list = types.InlineKeyboardButton(text='Просмотреть объявления', callback_data='look')
key_create = types.InlineKeyboardButton(text='создать объявление', callback_data='create')
key_mq = types.InlineKeyboardButton(text='Мои объявления', callback_data='mq')
kb_l = types.InlineKeyboardMarkup()
kb_l.add(key_list, key_create, key_mq)

key_list = [keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8]






class Bildboard():
    def make(self, id, text):

        with open('quest_num.txt', 'r') as file_q:
            quest_id = int(file_q.readline())
            con = sqlite3.connect('bot_data.db')
            with con:
                sql = 'INSERT INTO QUEST_data (id, q_text, user_id, status) values(?, ?, ?, ?)'
                data = [(quest_id, text, id, "open")]
                con.executemany(sql, data)
                bot.send_message(id, text=f'поручение выставлено, его номер:{quest_id}')
                quest_id +=1
            with open('quest_num.txt', 'w') as file:
                file.write(str(quest_id))
                file.flush()
                file.close
            
            
    def look(self, id, username):
        con = sqlite3.connect('bot_data.db')
        with con:
            f = 0
            q_list = con.execute('SELECT * FROM QUEST_data WHERE STATUS != \'closed\'')
            for quest in q_list:
                f = 1
                q_id, text, u_id, stat = quest
                key_accept = types.InlineKeyboardButton(text='Принять✅', callback_data=f'accept_quest:{q_id}:{id}:{username}')
                key_report = types.InlineKeyboardButton(text='Пожаловаться\U0001F198', callback_data=f'accept_report:{q_id}')
                keyboard_quest = types.InlineKeyboardMarkup()
                keyboard_quest.add(key_accept, key_report)
                text = f'Поручение номер {q_id} \n {text}'
                bot.send_message(id, text, reply_markup=keyboard_quest)
            if f == 0:
                bot.send_message(id, 'сейчас нет активных поручений')
                

    def close(self,id, m_id, c_id):
        con = sqlite3.connect('bot_data.db')
        con.execute(f"UPDATE QUEST_data SET status=\"closed\" WHERE id={id}")
        bot.delete_message(c_id, m_id)
        con.commit()


    def user_quests(self,id):
        f = 0
        con = sqlite3.connect('bot_data.db')
        data = con.execute(f'SELECT * FROM QUEST_data WHERE user_id=\'{id}\' AND status != \'closed\'')
        for dt in data:
            f = 1
            q_id, q_text, q_user_id, stat = dt
            key_close = types.InlineKeyboardButton(text='Закрыть', callback_data=f'close:{q_id}')
            kb_close = types.InlineKeyboardMarkup()
            kb_close.add(key_close)
            bot.send_message(id, f'ваше поручение номер {q_id}\n {q_text}', reply_markup=kb_close)
        if f == 0:
            bot.send_message(id, text='у вас нет активных объявлений')
            

    def take(self, id, user_id, username):
        con = sqlite3.connect('bot_data.db')
        dat_resp = con.execute(f'SELECT * FROM quest_data WHERE id={id}')
        for qst in dat_resp:
            q_id, q_text, user_id, sts = qst
            bot.send_message(user_id, text=f'ваше поручение номер {id} \n {q_text}\nпринял пользователь @{username}')










def send(char, id):
    global sample
    con = sqlite3.connect('bot_data.db')
    with con:
        data = con.execute(f'SELECT * FROM CHARS WHERE Name like \'%{char}%\'')
        l = []
        for sql_respond in data:
            for element in sql_respond: l.append(element) 
        ind = 4
        for group in sample:
                bot.send_message(id, text=f'{group} {l[ind]}', parse_mode='MarkdownV2')
                ind+=1

        


bilboard = Bildboard()



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, text='Привет! для работы с ботом обрати внимания на кнопку меню слева от строки ввода сообщения')
    elif '!создать' in message.text:
        bilboard.make(message.from_user.id, message.text.replace('!создать', '', 1))
    elif message.text == '/p':
        bot.send_message(message.from_user.id, text='Выбор персонажа', reply_markup=keyboard1)
    elif message.text == '/b':
        bot.send_message(message.from_user.id, text='Добро пожаловать на доску объявлений\n Здесь вы можете выставить просьбу о помощи или ответить на уже существующие.', reply_markup=kb_l)
    else:
        pass
        

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'pred':
        bot.send_message(call.message.chat.id, 'Обратная связь: @probably_p')
    elif call.data[:-1] == 'to':
        num = int(call.data[-1])
        global key_list
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Выбор персонажа. \nСтраница {num}", reply_markup=key_list[num-1])
    elif 'accept_quest:' in call.data:
        data = call.data.split(':')
        bilboard.take(data[1], data[2], data[3])
    elif 'close' in call.data:
        info = call.data.split(':')
        bilboard.close(info[1],call.message.message_id,call.message.chat.id)
    elif call.data == 'create':
        bot.send_message(call.message.chat.id, text='Для того, чтобы создать объявление, используйте команду  \n** \!создать** \(ваш текст\) \nпример:\n\!создать Нужна помощь с артефактами',parse_mode='MarkdownV2')
    elif call.data == 'look':
        bilboard.look(call.from_user.id, call.from_user.username)
    elif call.data == 'mq':
        bilboard.user_quests(call.message.chat.id)
    elif 'report' in call.data:
        inf = call.data.split(':')
        bot.send_message(call.message.chat.id, f'Ваша жалоба на поручение {inf[1]} отправлена.')
        bot.send_message(396157528, f'Поступила жалоба на поручение номер {inf[1]}')
    else:
        send(call.data, call.message.chat.id)
        

bot.polling(none_stop=True, interval=0)
