import shelve
from telebot import types
from random import shuffle
from SQLighter import SQLighter
from config import database_name, shelve_name

def count_rows():
    """
    Данный метод считает общее количество строк в базе данных и сохраняет в хранилище.
    Потом из этого количества будем выбирать музыку.
    """
    db = SQLighter(database_name)
 


def generate_markup(right_answer, wrong_answers):
    """
    Создаем кастомную клавиатуру для выбора ответа
    :param right_answer: Правильный ответ
    :param wrong_answers: Набор неправильных ответов
    :return: Объект кастомной клавиатуры
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    # Склеиваем правильный ответ с неправильными
    all_answers = '{},{}'.format(right_answer, wrong_answers)
    # Создаем лист (массив) и записываем в него все элементы
    list_items = []
    for item in all_answers.split(','):
        list_items.append(item)
    # Хорошенько перемешаем все элементы
    shuffle(list_items)
    # Заполняем разметку перемешанными элементами
    for item in list_items:
        markup.add(item)
    return markup
