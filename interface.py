from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import Library

def game(text):
    if text.lower() == "Библиотека".lower():
        return Library.description()
    elif text.lower() == "Подойти к человеку".lower():
        return Library.dialog_start()
    elif text.lower() == "Я расследую исчезновение лорда. А ты случайно не Ри?".lower():
        return Library.dialog_1()
    elif text.lower() == "Эти байки для стражи можешь и оставить, а мне расскажи-ка лучше про это *кладете перед ним книгу в черной обложке*".lower():
        return Library.dialog_2()
    elif text.lower() == "Тише-тише, я даже не понимаю, что здесь написано.".lower():
        return Library.dialog_end()
    elif text.lower() == "Хм.. ну ладно".lower():
        return Library.end_room()


def keyboard(text):
    if text.lower() == "Библиотека".lower():
       keyboard_show = Library.initiate()
       return keyboard_show
    elif text.lower() == "Подойти к человеку".lower():
        keyboard_show = Library.dialog_answer_buttons_1()
        return keyboard_show
    elif text.lower() == "Я расследую исчезновение лорда. А ты случайно не Ри?".lower():
        keyboard_show = Library.dialog_answer_buttons_2()
        return keyboard_show
    elif text.lower() == "Эти байки для стражи можешь и оставить, а мне расскажи-ка лучше про это *кладете перед ним книгу в черной обложке*".lower():
        keyboard_show = Library.dialog_answer_buttons_3()
        return keyboard_show
    elif text.lower() == "Тише-тише, я даже не понимаю, что здесь написано.".lower():
        keyboard_show = Library.dialog_end_buttons()
        return keyboard_show
    elif text.lower() == "Хм.. ну ладно".lower():
        keyboard_show = Library.end_room_buttons()
        return keyboard_show