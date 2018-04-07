from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import Library

def game(text):
    if text.lower() == "Библиотека".lower():
        return Library.description()
    else:
        return "Ну е мае"


def keyboard(text):
    if text.lower() == "Библиотека".lower():
       keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="%s" % Library.initiate())]])
       return keyboard



