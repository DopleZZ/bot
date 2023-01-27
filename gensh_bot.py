from telebot import types
import telebot;
import json



bot = telebot.TeleBot('5843937954:AAEHbkJuSu_eKputHcFWuiPLxMTYmv4V_qM')
def send(char, id):
    with open('data__.json','r', encoding='UTF-8') as file:
        try:
            data = json.load(file)
            text = ''
            #for i in data[char]: text += str(i) + ':' +  '\n' + data[char][i] + '\n\n'
            pic = f'возвышение/{char}.webp'
            img = open(pic, 'rb')
            for i in data[char]: text+=i
            bot.send_photo(id, img)
            bot.send_message(id, text)
            print('есть контакт')
        except:
            pass

def report(id, text):
    f = f'пользователь {str(id)} написал: {text}' 
    bot.send_message(396157528, f)




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if '/report' in message.text:
        report(message.from_user.id, message.text)
    else:
        keyboard = types.InlineKeyboardMarkup()
        key_Al = types.InlineKeyboardButton(text='Аль', callback_data='Аль ')
        key_YaoYao = types.InlineKeyboardButton(text='Яо Яо ', callback_data='Яо Яо ')
        key_Stranger = types.InlineKeyboardButton(text='Странник ', callback_data='Странник ')
        key_Faruzan = types.InlineKeyboardButton(text='Фарузан ', callback_data='Фарузан ')
        key_Layla = types.InlineKeyboardButton(text='Лайла ', callback_data='Лайла ')
        key_Nahida = types.InlineKeyboardButton(text='Нахида ', callback_data='Нахида ')
        key_Nilu = types.InlineKeyboardButton(text='Нилу ', callback_data='Нилу ')
        key_Sayno = types.InlineKeyboardButton(text='Сайно ', callback_data='Сайно ')
        key_Candice = types.InlineKeyboardButton(text='Кандакия ', callback_data='Кандакия ')
        key_Dori = types.InlineKeyboardButton(text='Дори ', callback_data='Дори ')
        key_Tignari = types.InlineKeyboardButton(text='Тигнари ', callback_data='Тигнари ')
        key_Kollei = types.InlineKeyboardButton(text='Коллеи ', callback_data='Коллеи ')
        key_Trav_dendro = types.InlineKeyboardButton(text='Путешественник Дендро ', callback_data='Путешественник Дендро ')
        key_Heizo = types.InlineKeyboardButton(text='Хэйдзо ', callback_data='Хэйдзо ')
        key_Sinobu = types.InlineKeyboardButton(text='Синобу ', callback_data='Синобу ')
        key_Elan = types.InlineKeyboardButton(text='Е Лань ', callback_data='Е Лань ')
        key_ayato = types.InlineKeyboardButton(text='Аято ', callback_data='Аято ')
        key_Yae = types.InlineKeyboardButton(text='Яэ Мико ', callback_data='Яэ Мико ')
        key_Shenhe = types.InlineKeyboardButton(text='Шэнь Хэ ', callback_data='Шэнь Хэ ')
        key_Yunzhin = types.InlineKeyboardButton(text='Юнь Цзинь ', callback_data='Юнь Цзинь ')
        key_Itto = types.InlineKeyboardButton(text='Итто ', callback_data='Итто ')
        key_Goro = types.InlineKeyboardButton(text='Горо ', callback_data='Горо ')
        key_Toma = types.InlineKeyboardButton(text='Тома ', callback_data='Тома ')
        key_Kokomi = types.InlineKeyboardButton(text='Кокоми ', callback_data='Кокоми ')
        key_Shogun = types.InlineKeyboardButton(text='Райдэн ', callback_data='Райдэн ')
        key_Eloy = types.InlineKeyboardButton(text='Элой ', callback_data='Элой ')
        key_Sara = types.InlineKeyboardButton(text='Сара ', callback_data='Сара ')
        key_Yeimia = types.InlineKeyboardButton(text='Ёимия ', callback_data='Ёимия ')
        key_Sau = types.InlineKeyboardButton(text='Саю ', callback_data='Саю ')
        key_Trav_electro = types.InlineKeyboardButton(text='Путешественник Электро ', callback_data='Путешественник Электро ')
        key_Ayaka = types.InlineKeyboardButton(text='Аяка ', callback_data='Аяка ')
        key_Kadzhuha = types.InlineKeyboardButton(text='Кадзуха ', callback_data='Кадзуха ')
        key_Aola = types.InlineKeyboardButton(text='Эола ', callback_data='Эола ')
        key_YanFey = types.InlineKeyboardButton(text='Янь Фэй ', callback_data='Янь Фэй ')
        key_Rosaria = types.InlineKeyboardButton(text='Розария ', callback_data='Розария ')
        key_HuTao = types.InlineKeyboardButton(text='Ху Тао ', callback_data='Ху Тао ')
        key_Sao = types.InlineKeyboardButton(text='Сяо ', callback_data='Сяо ')
        key_GanYui = types.InlineKeyboardButton(text='Гань Юй ', callback_data='Гань Юй ')
        key_Albedo = types.InlineKeyboardButton(text='Альбедо ', callback_data='Альбедо ')
        key_Ghoungli = types.InlineKeyboardButton(text='Чжун Ли ', callback_data='Чжун Ли ')
        key_SinYan = types.InlineKeyboardButton(text='Синь Янь ', callback_data='Синь Янь ')
        key_Tartaghilia = types.InlineKeyboardButton(text='Чайльд Тарталья ', callback_data='Чайльд Тарталья ')
        key_Diona = types.InlineKeyboardButton(text='Диона ', callback_data='Диона ')
        key_Kli = types.InlineKeyboardButton(text='Кли ', callback_data='Кли ')
        key_Venti = types.InlineKeyboardButton(text='Венти ', callback_data='Венти ')
        key_ChiChi = types.InlineKeyboardButton(text='Ци Ци ', callback_data='Ци Ци ')
        key_Mona = types.InlineKeyboardButton(text='Мона ', callback_data='Мона ')
        key_Kueqing = types.InlineKeyboardButton(text='Кэ Цин ', callback_data='Кэ Цин ')
        key_Diluc = types.InlineKeyboardButton(text='Дилюк ', callback_data='Дилюк ')
        key_Jean = types.InlineKeyboardButton(text='Джинн ', callback_data='Джинн ')
        key_Amber = types.InlineKeyboardButton(text='Эмбер ', callback_data='Эмбер ')
        key_ChunYun = types.InlineKeyboardButton(text='Чун Юнь ', callback_data='Чун Юнь ')
        key_Fishl = types.InlineKeyboardButton(text='Фишль ', callback_data='Фишль ')
        key_Sunlin = types.InlineKeyboardButton(text='Сян Лин ', callback_data='Сян Лин ')
        key_Sinzhu = types.InlineKeyboardButton(text='Син Цю ', callback_data='Син Цю ')
        key_Sucrose = types.InlineKeyboardButton(text='Сахароза ', callback_data='Сахароза ')
        key_Razor = types.InlineKeyboardButton(text='Рэйзор ', callback_data='Рэйзор ')
        key_Noele = types.InlineKeyboardButton(text='Ноэлль ', callback_data='Ноэлль ')
        key_Nin = types.InlineKeyboardButton(text='Нин Гуан ', callback_data='Нин Гуан ')
        key_Liza = types.InlineKeyboardButton(text='Лиза ', callback_data='Лиза ')
        key_Keya = types.InlineKeyboardButton(text='Кэйа ', callback_data='Кэйа ')
        key_BayDou = types.InlineKeyboardButton(text='Бэй Доу ', callback_data='Бэй Доу ')
        key_Bennet = types.InlineKeyboardButton(text='Беннет ', callback_data='Беннет ')
        key_Barabara = types.InlineKeyboardButton(text='Барбара ', callback_data='Барбара ')
        key_Trav_geo = types.InlineKeyboardButton(text='Путешественник Гео ', callback_data='Путешественник Гео ')
        key_Trav_anemo = types.InlineKeyboardButton(text='Путешественник Анемо ', callback_data='Путешественник Анемо ')
        key_desc = types.InlineKeyboardButton(text='Предложить', callback_data='pred')

        keyboard.add(key_Al,key_YaoYao,key_Stranger,key_Faruzan,key_Layla,key_Nahida,key_Nilu,key_Sayno,key_Candice,key_Dori,key_Tignari,key_Kollei,key_Trav_dendro,key_Heizo,key_Sinobu,key_Elan,key_ayato,key_Yae,key_Shenhe,key_Yunzhin,key_Itto,key_Goro,key_Toma,key_Kokomi,key_Shogun,key_Eloy,key_Sara,key_Yeimia,key_Sau,key_Trav_electro,key_Ayaka,key_Kadzhuha,key_Aola,key_YanFey,key_Rosaria,key_HuTao,key_Sao,key_GanYui,key_Albedo,key_Ghoungli,key_SinYan,key_Tartaghilia,key_Diona,key_Kli,key_Venti,key_ChiChi,key_Mona,key_Kueqing,key_Diluc,key_Jean,key_Amber,key_ChunYun,key_Fishl,key_Sunlin,key_Sinzhu,key_Sucrose,key_Razor,key_Noele,key_Nin,key_Liza,key_Keya,key_BayDou,key_Bennet,key_Barabara,key_Trav_geo,key_Trav_anemo, key_desc)
        bot.send_message(message.from_user.id, text='Выбор персонажа', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'pred':
        bot.send_message(call.message.chat.id, 'Если вы хотите предложить описание перснажа, или оставить отзыв, то напишите этому боту команду /report и ваше предложение/отзыв в одном сообщении')
    else:
        send(call.data, call.message.chat.id)
        
            #bot.send_message(call.message.chat.id, 'ошибка при загрузке персонажа')
            #print(f'при отработке команды {call.data} возникла ошибка при отправке описания')
        #print(f'отработка команды {call.data} успешна')

bot.polling(none_stop=True, interval=0)
