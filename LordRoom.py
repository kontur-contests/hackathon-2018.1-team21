from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

roomname = 'Кабинет лорда'

# description = ('Пройдя в зал библиотеки и оглядевшись на первый взгляд вы никого здесь не замечаете, но ваш взгляд отделяет от стены, сидящую в дальнем углу фигуру в сером балахоне, которая скрюченно сидит над каким-то фолиантом.')

person = (
    'Охранник: Кто идет, чаво нать?')


def description():
    return 'Вы поднимаетесь по узкой винтовой лестнице и упираетесь в охранника преграждающего вам путь к двери в комнату. Крупный мужчина в форме городской стражи и с алебардой в руках.'
def initiate():
    return 'Я расследую пропажу лорда Винздора *показываете ему бумагу от мастера Торхилда*'


def dialog(answer):
    if answer == 'Я расследую пропажу лорда Винздора *показываете ему бумагу от мастера Торхилда*':
        return 'Охранник: А, ну так бы сразу. Интересной чавой-та ты там сможешь отыскать, чего не нашли наши. Он отходит в сторону и вы, пройдя через довольно низкий дверной проем, вам даже пришлось пригнуться, чтобы не удариться головой, оказываетесь в небольшом помещении. Обстановка довольно простая, здесь совсем нет лишней мебели, перед вами стоит массивный стол и справа от вас шкаф с книгами.


def ok():
    reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='По рукам')]])

    where = 'По рукам'

    if where == 'По рукам':
        print(
            '*Увесистый кошель падает на стол.* Глава гильдии мастер Торхилд – Чтож, мне необходимо приступить к обязанностям возложенным на меня в отсутствие лорда. Да помогут Вам Боги! Вы оглядываете приемную и замечаете две двери, помимо той которая привела вас сюда.')