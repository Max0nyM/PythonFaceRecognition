import telebot
import config
import os
import time
import random
import utils
from SQLighter import SQLighter
from telebot import types
import requests
import shutil
from face_detect import detectFace
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['game'])
def game(message):
    db_worker = SQLighter(config.database_name)
    row = db_worker.select_single(random.randint(1,2))
    markup = utils.generate_markup(row[1], row[1])
    bot.send_message(message.chat.id, 'Верно!', reply_markup=markup)
    db_worker.close()

@bot.message_handler(content_types=['photo'])
def check_answer(message):
    print(message.caption)
    file_info = bot.get_file(message.photo[3].file_id)
    person_name = message.caption
    print('https://api.telegram.org/file/bot{0}/{1}'.format(config.token, file_info.file_path))
    if message.caption != '':
        detectFace('https://api.telegram.org/file/bot{0}/{1}'.format(config.token, file_info.file_path),person_name,message.photo[3].file_id)
    else:
        person_name = recognizeFace('https://api.telegram.org/file/bot{0}/{1}'.format(config.token, file_info.file_path))
    path = 'dataSet/face/'+person_name
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    for image_path in image_paths:
        photo = open(image_path, 'rb')
        bot.send_photo(message.chat.id,photo)
   
if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)