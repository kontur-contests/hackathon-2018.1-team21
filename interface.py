from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import Library

def game(text):
    if text == "Библиотека":
        return Library.description()
    else:
        return "Ну е мае"


def keyboard(text):
    if text == "Библиотека":
       keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="%s" % Library.initiate())]])
       return keyboard



