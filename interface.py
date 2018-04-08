import Tower
import Library
import LordsRoom
import tavern
import Elaniya
import temple
import Boss

def game(text):
    # Башня
    if text.lower() == "Войти в башню".lower():
        return Tower.description_bashnya()
    elif text.lower() == "Где я могу найти их?".lower():
        return Tower.dialog_1()
    elif text.lower() == "По рукам!".lower():
        return Tower.dialog_2()
    elif text.lower() == "Дверь за спиной мастера Торхилда, ведет в кабинет лорда".lower():
        return LordsRoom.description()
    elif text.lower() == "Дверь справа – в Библиотеку".lower():
        return Library.description()
    # Библиотека
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
    # Кабинет лорда
    if text.lower() == "Кабинет лорда".lower():
        return LordsRoom.description()
    elif text.lower() == "Я расследую пропажу лорда Винздора *показываете ему бумагу от мастера Торхилда*".lower():
        return LordsRoom.dialog_1()
    elif text.lower() == "Осмотреть стол".lower():
        return LordsRoom.result_find_1()
    elif text.lower() == "Осмотреть книжный шкаф".lower():
        return LordsRoom.result_find_3()
    elif text.lower() == "Перейти к изучению шкафа".lower():
        return LordsRoom.result_find_3()
    elif text.lower() == "Осмотреть внимательно".lower():
        return LordsRoom.result_find_2()
    elif text.lower() == "Надеть амулет".lower():
        return LordsRoom.end_room()
    elif text.lower() == "Спрятать амулет в карман и перейти к шкафу".lower():
        return LordsRoom.result_find_3()
    elif text.lower() == "Положить книгу в карман и выйти из кабинета".lower():
        return LordsRoom.end_room()
    elif text.lower() == "В библиотеку".lower():
        return Library.description()
    elif text.lower() == "На площадь".lower():
        return Library.end_room()
    #Таверна
    if text.lower() == "Здесь же расположена таверна Кровавый кабан".lower():
        return tavern.description()
    elif text.lower() == "Подойти к мужчине за столом".lower():
        return tavern.dialog_start()
    elif text.lower() == "Воу-воу! Палехчи, приятель!".lower():
        return tavern.dialog_1()
    elif text.lower() == "Ясно. не переживай, я никому не скажу тоже".lower():
        return tavern.end_room()
    #Дом Элании
    if text.lower() == "Я по поручению мастера Торхилда, расследую дело об исчезновении лорда-протектора Винздора *показываете депешу*".lower():
        return Elaniya.dialog_1()
    elif text.lower() == "А что за праздник-то?".lower():
        return Elaniya.dialog_2()
    elif text.lower() == "Оооок".lower():
        return Elaniya.dialog_3()
    elif text.lower() == "подойти к Элании".lower():
        return Elaniya.dialog_4()
    elif text.lower() == "Я хочу поговорить о пропаже вашего жениха. Скажите, леди, он не рассказывал вам что ни будь странное или пугающее о своих планах?".lower():
        return Elaniya.dialog_5()
    elif text.lower() == "Можете не переживать на этот счет!".lower():
        return Elaniya.dialog_6()
    # Дорога
    if text.lower() == "Теперь я кажется понимаю о чем вы..".lower():
        return temple.description()
    elif text.lower() == "Да, кажется я знаю о каком месте идет речь, по южной дороге есть некий храм, последний раз лорда видели именно у него.".lower():
        return temple.dialog_start()
    #Храм
    if text.lower() == "Осмотреть храм".lower():
        return Boss.dialog_2()
    elif text.lower() == """Осмотреть внимательно""".lower():
        return Boss.dialog_3()
    elif text.lower() == "Солнце в зените, Полумесяц, Восход, Закат".lower():
        return Boss.portal()
    elif text.lower() == "Восход, Закат, Солнце в зените, Полумесяц".lower():
        return Boss.wrogn()
    elif text.lower() == "Полумесяц, Закат, Солнце в зените, Восход".lower():
        return Boss.wrogn()
    elif text.lower() == "Закат, Восход, Полумесяц, Солнце в зените".lower():
        return Boss.wrogn()
    elif text.lower() == "Подойти к порталу".lower():
        return Boss.dialog_4()
    elif text.lower() == "Незаметно подкрасться к входу".lower():
        return Boss.dialog_5()
    elif text.lower() == "Войти в крипту".lower():
        return Boss.dialog_6()
    elif text.lower() == "Бежать".lower():
        return Boss.decide_run()
    elif text.lower() == "Подставить ученика".lower():
        return Boss.decide_apprentice()
    elif text.lower() == "Драться".lower():
        return Boss.decide_fight()
    elif text.lower() == "Вы победили приспешников. Отдышавшись, продолжаете путь".lower():
        return Boss.dialog_7()
    elif text.lower() == "Подбежать к лорду".lower():
        return Boss.dialog_8()
    elif text.lower() == "В бой!".lower():
        return Boss.boss_defeat()
    elif text.lower() == "Вы переводите дыхание и осматриваетесь".lower():
        return Boss.dialog_9()
    elif text.lower() == """Подойти к алтарю""".lower():
        return Boss.dialog_10()
    elif text.lower() == """Помочь лорду встать""".lower():
        return Boss.dialog_11()

def keyboard(text):
    # Башня
    if text.lower() == "Войти в башню".lower():
       keyboard_show = Tower.initiate_bashnya()
       return keyboard_show
    elif text.lower() == "Где я могу найти их?".lower():
       keyboard_show = Tower.dialog_answer_buttons_3()
       return keyboard_show
    elif text.lower() == "По рукам!".lower():
       keyboard_show = Tower.end_room_buttons()
       return keyboard_show
    elif text.lower() == "Дверь за спиной мастера Торхилда, ведет в кабинет лорда".lower():
       keyboard_show = LordsRoom.dialog_answer_buttons_1()
       return keyboard_show
    elif text.lower() == "Дверь справа – в Библиотеку".lower():
       keyboard_show = Library.initiate()
       return keyboard_show
    # Библиотека
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
    # Кабинки Лорда
    if text.lower() == "Кабинет лорда".lower():
       keyboard_show = LordsRoom.dialog_answer_buttons_1()
       return keyboard_show
    elif text.lower() == "Я расследую пропажу лорда Винздора *показываете ему бумагу от мастера Торхилда*".lower():
       keyboard_show = LordsRoom.find_1()
       return keyboard_show
    elif text.lower() == "Осмотреть стол".lower():
       keyboard_show = LordsRoom.find_2()
       return keyboard_show
    elif text.lower() == "Осмотреть книжный шкаф".lower():
       keyboard_show = LordsRoom.find_4()
       return keyboard_show
    elif text.lower() == "Осмотреть внимательно".lower():
       keyboard_show = LordsRoom.find_3()
       return keyboard_show
    elif text.lower() == "Перейти к изучению шкафа".lower():
       keyboard_show = LordsRoom.find_4()
       return keyboard_show
    elif text.lower() == "Надеть амулет".lower():
       keyboard_show = LordsRoom.end_room_buttons()
       return keyboard_show
    elif text.lower() == "Спрятать амулет в карман и перейти к шкафу".lower():
       keyboard_show = LordsRoom.find_4()
       return keyboard_show
    elif text.lower() == "Положить книгу в карман и выйти из кабинета".lower():
       keyboard_show = LordsRoom.end_room_buttons()
       return keyboard_show
    elif text.lower() == "В библиотеку".lower():
       keyboard_show = Library.initiate()
       return keyboard_show
    elif text.lower() == "На площадь".lower():
       keyboard_show = Library.end_room_buttons()
       return keyboard_show
    # Таверна
    if text.lower() == "Здесь же расположена таверна Кровавый кабан".lower():
       keyboard_show = tavern.initiate()
       return keyboard_show
    elif text.lower() == "Вернуться на площадь".lower():
       keyboard_show = Library.end_room_buttons()
       return keyboard_show
    elif text.lower() == "Подойти к мужчине за столом".lower():
       keyboard_show = tavern.dialog_answer_buttons_1()
       return keyboard_show
    elif text.lower() == "Воу-воу! Палехчи, приятель!".lower():
       keyboard_show = tavern.dialog_answer_buttons_2()
       return keyboard_show
    elif text.lower() == "Ясно. не переживай, я никому не скажу тоже".lower():
       keyboard_show = Elaniya.dialog_answer_buttons_1()
       return keyboard_show
    #Дом Элании
    if text.lower() == "Я по поручению мастера Торхилда, расследую дело об исчезновении лорда-протектора Винздора *показываете депешу*".lower():
        keyboard_show = Elaniya.dialog_answer_buttons_2()
        return keyboard_show
    elif text.lower() == "А что за праздник-то?".lower():
        keyboard_show = Elaniya.dialog_answer_buttons_3()
        return keyboard_show
    elif text.lower() == "Оооок".lower():
        keyboard_show = Elaniya.dialog_answer_buttons_4()
        return keyboard_show
    elif text.lower() == "подойти к Элании".lower():
        keyboard_show = Elaniya.dialog_answer_buttons_5()
        return keyboard_show
    elif text.lower() == "Я хочу поговорить о пропаже вашего жениха. Скажите, леди, он не рассказывал вам что ни будь странное или пугающее о своих планах?".lower():
        keyboard_show = Elaniya.dialog_answer_buttons_6()
        return keyboard_show
    elif text.lower() == "Можете не переживать на этот счет!".lower():
        keyboard_show = Elaniya.end_room_buttons()
        return keyboard_show
    #Дорога
    if text.lower() == "Теперь я кажется понимаю о чем вы..".lower():
        keyboard_show = temple.initiate()
        return keyboard_show
    elif text.lower() == "Да, кажется я знаю о каком месте идет речь, по южной дороге есть некий храм, последний раз лорда видели именно у него.".lower():
        keyboard_show = temple.dialog_answer_buttons_1()
        return keyboard_show
    #Храм
    if text.lower() == "Осмотреть храм".lower():
        keyboard_show = Boss.dialog_answer_buttons_3()
        return keyboard_show
    elif text.lower() == """Осмотреть внимательно""".lower():
        keyboard_show = Boss.statui_asnwer()
        return keyboard_show
    elif text.lower() == "Солнце в зените, Полумесяц, Восход, Закат".lower():
        keyboard_show = Boss.dialog_answer_buttons_4()
        return keyboard_show
    elif text.lower() == "Восход, Закат, Солнце в зените, Полумесяц".lower():
        keyboard_show = Boss.statui_asnwer()
        return keyboard_show
    elif text.lower() == "Полумесяц, Закат, Солнце в зените, Восход".lower():
        keyboard_show = Boss.statui_asnwer()
        return keyboard_show
    elif text.lower() == "Закат, Восход, Полумесяц, Солнце в зените".lower():
        keyboard_show = Boss.statui_asnwer()
        return keyboard_show
    elif text.lower() == "Подойти к порталу".lower():
        keyboard_show = Boss.dialog_answer_buttons_5()
        return keyboard_show
    elif text.lower() == "Незаметно подкрасться к входу".lower():
        keyboard_show = Boss.dialog_answer_buttons_6()
        return keyboard_show
    elif text.lower() == "Войти в крипту".lower():
        keyboard_show = Boss.decide_butons()
        return keyboard_show
    elif text.lower() == "Бежать".lower():
        keyboard_show = Boss.run_buttons()
        return keyboard_show
    elif text.lower() == "Подставить ученика".lower():
        keyboard_show = Boss.apprentice_buttons()
        return keyboard_show
    elif text.lower() == "Драться".lower():
        keyboard_show = Boss.draka()
        return keyboard_show
    elif text.lower() == "Вы победили приспешников. Отдышавшись, продолжаете путь".lower():
        keyboard_show = Boss.dialog_answer_buttons_8()
        return keyboard_show
    elif text.lower() == "Подбежать к лорду".lower():
        keyboard_show = Boss.bitva_boss()
        return keyboard_show
    elif text.lower() == "В бой!".lower():
        keyboard_show = Boss.rest()
        return keyboard_show
    elif text.lower() == "Вы переводите дыхание и осматриваетесь".lower():
        keyboard_show = Boss.dialog_answer_buttons_10()
        return keyboard_show
    elif text.lower() == """Подойти к алтарю""".lower():
        keyboard_show = Boss.dialog_answer_buttons_11()
        return keyboard_show
    elif text.lower() == """Помочь лорду встать""".lower():
        keyboard_show = Boss.end_room_buttons()
        return keyboard_show
