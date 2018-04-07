from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

roomname = 'Второй финал'

def description():
    return """Лорд: Нам необходимо вернуться в город скорее! Отправим сюда людей, чтобы могли очистить это место и 
    вернуть моего бедного ученика домой, чтобы придать его земле как подобает. А я должен восстановиться и быстрее 
    вернуться к своим обязанностям."""

def dialog_answer_buttons_1():
	keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="""Помочь лорду идти до города.""")]])
	return keyboard

def dialog_1():
	return """Как только вы переступаете порог Южных ворот, народ, видя вас и лорда, которого вы несете фактически на 
	руках, начинает перешептываться, слух о возвращении защитника города распространяется быстро и у башни вас уже 
	встречает восторженная толпа. Люди кричат, хлопают и на их глазах видны слезы радости. На шум выходит мастер 
	Торхилд, он втаскивает вас с лордом в башню.
    Мастер Торхилд: Не верю своим глазам!  Вы справились! Как я рад! А как счастлив народ Размирана вы уже и сами 
    убедились! Вы заслуживаете много больше чем эти деньги, но прошу примите хотя бы эту скромную награду
    Он протягивает вам кошель с 100 ЗМ и крепко жмет вам руку"""