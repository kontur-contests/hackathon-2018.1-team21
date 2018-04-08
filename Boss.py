from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random
roomname = 'Локация босса'

def description():
    return"""Выйдя из имения Леди Элании вы понимаете, что прошло уже больше 3х часов пока вы бродили по городу. 
    Вы устремляетесь к главной площади надеясь еще застать там ученика лорда. Как только вы ступаете на площадь на 
    вас вылетает Ри и начинает свой сумбурный рассказ."""


def dialog_start():
    return"""Учени Ри: Мне удалось перевести несколько страниц, если лорд действительно применял те практики, что 
    описаны в книге, то у нас осталось совсем мало времени, пока от сознания Винздора не заменится полностью демоном 
    с другого плана. Я выяснил какие компоненты нужны для проведения ритуала, нужно особенное место… Тебе удалось 
    что-то узнать?"""

def dialog_answer_buttons_1():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Да, кажется я знаю о каком месте идет речь, по 
	южной дороге есть некий храм, последний раз лорда видели именно у него""")]])
	return keyboard

def dialog_1():
	return """Ри: Отлично! Нам необходимо торопиться! 
	Объединив усилия, вы двигаетесь к Южным воротам. Никто не препятствует вам, и вы выходите на широкую мощёную 
	дорого по которой без труда добираетесь до места.
    Из-за придорожных деревьев на небольшом холме видны серые храмовые развалины, поросшие плющом и другими растениями.
    Вы вдвоем двигаетесь через колючие заросли, подходите ближе к величественному строению."""

def dialog_answer_buttons_2():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Осмотреть храм""")]])
	return keyboard

def dialog_2():
	return """Вы обходите строение со всех сторон, это четыре фигуры ориентированы на стороны света, каждая 
	представляет собой эльфийку держащую в руках различные предметы:
    1.Юг – кисть для рисования
    2.Север – меч
    3.Восток – арфа
    4.Запад – свиток
    Но нет ничего похожего на вход"""

def dialog_answer_buttons_3():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Осмотреть более внимательно""")]])
	return keyboard

def dialog_3():
	return """Вы подходите к каждой статуе, осматриваете внимательно и видите, что перед каждой есть колонна с вращающимся элементом, покрутив его вы видите там символы:
    1.Восход
    2.Закат
    3.Солнце в зените 
    4.Полумесяц
    Необходимо расположить вращающиеся элементы правильно относительно каждой статуи. Как только последняя из колонн 
    принимает правильное положение, в центре строения открывается портал"""

#повороты статуй
#Восток – восход(3 - 1)
#Запад – закат(4 - 2)
#Юг – зенит(1 - 3)
#Север – полумесяц(2 - 4)
def portal():
    return "В центре строения открывается портал"

def wrogn():
    return "Ничего не произошло, вы вращаете колонны дальше"
    #while True:
#        q1 = random.randint(1, 4)
#        w1 = random.randint(1, 4)
#        q2 = random.randint(1, 4)
#        w2 = random.randint(1, 4)
#        q3 = random.randint(1, 4)
#       w3 = random.randint(1, 4)
#        q4 = random.randint(1, 4)
#        w4 = random.randint(1, 4)
#        if q1==3 and w1==1 and q2==4 and w2==2 and q3==1 and w3==3 and q4==2 and w4==4:
#            return "Колонны приняли правильное положение"
#        continue
def statui_asnwer():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Восход, Закат, Солнце в зените, Полумесяц")], [KeyboardButton(text="Солнце в зените, Полумесяц, Восход, Закат")], [KeyboardButton(text="Полумесяц, Закат, Солнце в зените, Восход")], [KeyboardButton(text="Закат, Восход, Полумесяц, Солнце в зените")]])
    return keyboard


def dialog_answer_buttons_4():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Подойти к порталу""")]])
	return keyboard

def dialog_4():
	return """Вам требуется некоторое время, чтобы отыскать портал, в заросших плющом недрах храма. Вы спускаетесь 
	по ступеням вниз. Ри произносит какие-то слова и кристалл в основании его посоха начинает испускать неяркое 
	свечение, в его свете, вам без труда удается преодолеть ступеньки.
    Пройдя так какое-то время, вы видите арку за которой находится слабо освещенное помещение и слышны монотонное 
    бормотание."""

def dialog_answer_buttons_5():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Незаметно подкрасться к входу""")]])
	return keyboard

def dialog_5():
	return """Перед вами предстает небольшое квадратное помещение, которое очевидно служит гробницей.
    От саркофага вас отделяет небольшой бассейн с темной водой.
    В дальней части перед саркофагом в пляшущем свете свечей вы видите лорда. Он стоит сгорбившись, тяжело опираясь 
    на посох, его осунувшееся лицо ничего не выражает, глаза заволокла белая пелена. Лишь бледные губы находятся в 
    постоянном движении повторяя какие-то незнакомые вам слова."""

def dialog_answer_buttons_6():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Войти в крипту""")]])
	return keyboard

def dialog_6():
	return """Вы входите и только сейчас понимаете, что лорд, не единственный, кто здесь присутствует. От колонны 
	рядом с ним отделяется тень. Это высокий человек, вся его фигура скрыта черным балахоном, вы не ведите его лица, 
	но слышите громкий голос, который он подает из-под капюшона
    Главный Культист: Что?! Кто-то пытается нам помешать?! Не бывать этому! Ритуал скоро будет завершен, а вы станете 
    отличными жертвами! Взять их! *Вытягивает руку в вашем направлении*
    И вы видите, как справа и слева от стен отскакивают такие же тени в темных балахонах, обступая вас. """

def decide_butons():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Драться")], [KeyboardButton(text="Бежать")], [KeyboardButton(text="Подставить ученика")]])
    return keyboard

def decide_run():
    return "А куда вы собственно собрались бежать, вход то за вами закрыли 2 тени, но это промедление стоило вам жизни. Вы мертвы"

def decide_apprentice():
    return "Резко схватив ученика на шкирку вы кинули его на 2 теней стоящих у входа, эта заварушка позволила вам сбежать. Но выполнению задания это не поспособствовало, у вас отняли деньги. И у вас не осталось ничего кроме как пить в кабаке, глядя на то, как ученик греется в лучах славы, ведь в той битве он вышел победителем и спас лорда!"

def decide_fight():
    return "Вы принимаете решение драться и встаете в боевую позу"

def run_buttons():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/Start")]])
    return keyboard

def apprentice_buttons():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/Start")]])
    return keyboard

def draka():
    hpg = 6
    hpp1 = 3
    hpp2 = 3

    while hpg > 0 and hpp1 > 0 and hpp2 > 0:
        n = random.randint(1, 2)
        m = random.randint(1, 2)
        p = random.randint(1, 2)
        if n == 2 and m == 2 and p == 2:
            hpp1 -= 1
            hpp2 -= 1
            if hpp1 <= 0 and hpp2 <= 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                return keyboard
            hpg -= 2
            if hpg <= 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                return keyboard
        elif n == 2 and m == 2 and p==1:
            hpp1 -= 1
            hpp2 -= 1
            if hpp1 <= 0 and hpp2 <= 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                return keyboard
            hpg -= 1
            if hpg <= 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                return keyboard
        elif n == 2 and m == 1 and p == 1:
            hpp1 -= 1
            hpp2 -= 1
            if hpp1 <= 0 and hpp2 <= 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                return keyboard
            hpg -= 0
            if hpg <= 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                return keyboard
        elif n == 2 and m == 1 and p == 2:
                hpp1 -= 1
                hpp2 -= 1
                if hpp1 <= 0 and hpp2 <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                    return keyboard
                hpg -= 1
                if hpg <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                    return keyboard
                continue
        elif n == 1 and m == 2 and p == 2:
                hpp1 -= 0
                hpp2 -= 0
                if hpp1 <= 0 and hpp2 <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                    return keyboard
                hpg -= 2
                if hpg <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                    return keyboard
                continue
        elif n == 1 and m == 2 and p == 1:
                hpp1 -= 0
                hpp2 -= 0
                if hpp1 <= 0 and hpp2 <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                    return keyboard
                hpg -= 1
                if hpg <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                    return keyboard
                continue
        elif n == 1 and m == 1 and p == 2:
                hpp1 -= 0
                hpp2 -= 0
                if hpp1 <= 0 and hpp2 <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                    return keyboard
                hpg -= 2
                if hpg <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                    return keyboard
                continue
        elif n == 1 and m == 1 and p == 1:
                hpp1 -= 0
                hpp2 -= 0
                if hpp1 <= 0 and hpp2 <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы победили приспешников. Отдышавшись, продолжаете путь")]])
                    return keyboard
                hpg -= 0
                if hpg <= 0:
                    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                    return keyboard
                continue



def dialog_7():
	return """В это время Ри пытается приблизиться к своему учителю, но между ним и главным кулитстом завязывается 
	бой, они посылают друг в друга искрящиеся заряды, выкрикивая различные заклинания. 
    Когда последний поражённый приспешник падает перед вами, главный культист обращает внимание на вас.
    Главный культист: Слабаки, все приходится делать самому!
    Он прыгает в бассейн и темные воды скрывают его полностью."""

def dialog_answer_buttons_8():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Подбежать к лорду""")]])
	return keyboard

def dialog_8():
	return """Воспользовавшись затишьем вы вместе с Ри бежите к алтарю, у которого стоит Винздор. Ученик успевает 
	добежать до лорда и берет его за плечи. Но когда вы доходите до бассейна, фонтан воды окатывает вас и из его недр 
	появляется странное существо, с множеством щупалец и красных разъяренных глаз, оно издает душераздирающий рев и 
	выбрасывает в вашу сторону щупальце."""

def boss_defeat():
    return """В пылу какзалось бы бесперспективного сражения, вы замечете, как Ри подбегает к бассейну, он шепчет какое-то заклинание, его ладони 
                    сближаются, между ними проскакивают искры, воздух в комнате ставится разряженным. Он ступает в воду, 
                    его голос звучит громче, он резко ударяет ладонями по воде и всю воду в бассейне пронзают всполохи 
                    молний. Чудовище ревет, испускает последний вздох и падает замертво."""

def bitva_boss():
    hpg = 3
    # Здоровье врага
    hpe = 3
    while hpg > 0 and hpe > 0:
        n = random.randint(1, 2)
        m = random.randint(1, 2)
        if n == 2 and m == 2:
            hpe -= 1
            if hpe == 1:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="В бой!")]])
                return keyboard
            hpg -= 1
            if hpg == 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                return keyboard
            continue
        elif n == 2 and m == 1:
            hpe -= 1
            if hpe == 1:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="В бой!")]])
                return keyboard
            continue
        elif n == 1 and m == 2:
            hpg -= 1
            if hpg == 0:
                keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Start")]])
                return keyboard
            continue
        elif n == 1 and m == 1:
            continue
    input()
    pass

def rest():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Вы переводите дыхание и осматриваетесь")]])
    return keyboard

def dialog_9():
	return """ Когда все стихает вы видите в воде два бездыханных тела. Одно из них принадлежит ученику. 
	Но ваши мысли прерывает слабый стон, раздающийся со стороны алтаря"""

def dialog_answer_buttons_10():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Подойти к алтарю""")]])
	return keyboard

def dialog_10():
	return """Вы подниметесь по ступеням ведущим к саркофагу и видите лорда Винздора. Пелена с его глаз спала, он 
	очень слаб, но жив и пытается подняться"""

def dialog_answer_buttons_11():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Помочь лорду встать""")]])
	return keyboard

def dialog_11():
	return """Вы подхватываете лорда и понимаете, что его тело почти ничего не весит
    Лорд-протектор: Сколько.. сколько зла может причинить жажда властвовать над темными силами.. Я видел, как мой 
    ученик пожертвовал собой.. надеюсь больше никто не пострадал?"""

def end_room_buttons():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Рассказать лорду о том, что он пытался принести в 
	                                        жертву свою невесту, чуть не убил своего слугу.""")],
											 [KeyboardButton(text="""Ничего не говорить и попытаться увести лорда в 
											 город""")]])
	return keyboard







