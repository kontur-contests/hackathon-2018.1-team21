from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import Library

def game(text):
    if text == "Библиотека":
        return Library.description
    else:
        return "А?"


def keyboard():
    return



