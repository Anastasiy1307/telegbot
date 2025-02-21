import telebot
import random

bot = telebot.TeleBot('7635588138:AAFCpgLfo7ZHIYuVpvZ7tjgvHvp2Hye6E0Y')
#dp = Dispatcher(bot)

@bot.message_handler(commands=['кусь'])
def main(message : telebot.types.Message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "mention":# упоминание чере @
                foruser = message.text[entity.offset:entity.offset + entity.length]
               # await message.reply_text(foruser)
    place_for_kusb = ('пальчик', 'лапку', 'руку', 'коленку', 'локоть', 'плечо', 'жопку', 'голову', 'ушко', 'шею', 'ногу' ,'нос' ,'предплечье','грудь')
    no_kusb = ('Эх, не судьба...','Цель увернулась!','Я уже радовалась кусю, а ты увернулся! ','А зубки-то проскользнули...','Попытка кусь – не пытка, но промах!')
    num_random= random.randint(1,101)

    if num_random <= 35:
        random_place = random.choice(no_kusb)
        user = '@' + message.from_user.username +' '+ random_place
        bot.send_message(message.chat.id, user)
    else:
        random_place = random.choice(place_for_kusb)
        user = '@'+message.from_user.username + ' укусил ' + foruser + ' за '+ random_place
        bot.send_message(message.chat.id, user)

@bot.message_handler(commands=['обнять'])
def main(message : telebot.types.Message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "mention":  # упоминание чере @
                foruser = message.text[entity.offset:entity.offset + entity.length]
    hug = ('@'+message.from_user.username +' заворачивает '+ foruser+ ' в тёплую обнимашку!', '@'+message.from_user.username +' нежно прижимает '+ foruser+' к себе!', '@'+message.from_user.username +' окутывает '+ foruser+' уютными объятиями!',  '@'+message.from_user.username +' тихонько обнял '+ foruser+' и не отпускает!', '@'+message.from_user.username +' делает супер-крепкие объятия для '+ foruser,  '@'+message.from_user.username +' устраивает '+ foruser+' мягкую атаку обнимашками!', '@'+message.from_user.username +' подкрался и обнял '+ foruser)
    random_hug= random.choice(hug)
    bot.send_message(message.chat.id, random_hug)

@bot.message_handler(commands=['совместимость'])
def main(message : telebot.types.Message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "mention":  # упоминание чере @
                foruser = message.text[entity.offset:entity.offset + entity.length]
    num_random_sovm = random.randint(1, 101)
    str_random_sovm = str(num_random_sovm)
    user = '@'+message.from_user.username + ' и '+ foruser+' совместимы на '+ str_random_sovm +'%'
    bot.send_message(message.chat.id, user)


bot.polling(non_stop=True)