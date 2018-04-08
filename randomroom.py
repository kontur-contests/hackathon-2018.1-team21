from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def add_statue():
    file_open = open("/home/SamolevarKilusov/mysite/counter.txt", "r")
    count = file_open.read()
    i = int(count)
    i += 1
    file_rewrite = open("/home/SamolevarKilusov/mysite/counter.txt", "w")
    file_rewrite.write(str(i))

def statues():
    file_open = open("/home/SamolevarKilusov/mysite/counter.txt", "r")
    count = file_open.read()
    i = int(count)
    return i

roomname = 'случайная площадь'

def description():
    return"""'Вы сразу же выходите из приемной в башне лорда и попадаете на главную торговую площадь города. Надо сказать, что торговля идет не бойко и несмотря на середину дня, площадь выглядит пустой. Осматриваясь на площади вызамечаете узкую улочку, из которой доносится странный, как будто зовущий, звук"""

def initiate():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Здесь же расположена таверна Кровавый кабан")], [KeyboardButton(text="Поднявщись немного вверх по улице вы попадете в имение Баронессы Элании")],[KeyboardButton(text="Пройти в переулок")]])
    return keyboard

def death():
    n = statues()
    add_statue()
    if n == 0:
	    return "Попав в переулок, вы никого не находите, подумав, что вам это просто показалось, вы собираетесь уходить, как вдруг, из решетки канализации выползает матерый василик и одним взглядом обращает вас в камень, на вашем каменном изваянии застыла гримасса недоумения"
    else:
        return "Попав в переулок, вы обнаруживаете %s интереснеших статуй, каждая из которых стоит в странной позе и с уникальным выражением лица. Вы не понимаете, что происходит, ходите вокруг и в самый последний момент замечаете матерого василиска, но уже поздно, вы стали очередным экспонатом этой коллекции" % n