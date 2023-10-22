from PyQt5.QtCore import Qt #библиотека для кодинга
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel) #загрузка модулей из библиотеки пайкьюти5
from random import shuffle, randint #рандомайзер расположений вариантов ответа

class Question(): #создание класса чтобы не заморачиватся с кодингом вопросов
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3): #добавление переменных с инит
        self.question = question #
        self.right_answer = right_answer #
        self.wrong1 = wrong1 #
        self.wrong2 = wrong2 #
        self.wrong3 = wrong3 #

question_list = [] #
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский')) #вопрос 1 с 4 вариантами
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий')) #вопрос 2 с 4 вариантами
question_list.append(Question('Национальная хижина якутов?', 'Ураса', 'Юрта', 'Иглу', 'Хата')) #вопрос 3 с 4 вариантами

app = QApplication([]) #создание приложения
btn_ok = QPushButton("Ответить") #создаем кнопку ответа
lb_Question = QLabel("Самый сложный вопрос в мире!") #текст

RadioGroupBox = QGroupBox("Варианты ответов:") #текст
rbtn_1 = QRadioButton('Вариант 1') #вариант 1
rbtn_2 = QRadioButton('Вариант 2') #вариант 2
rbtn_3 = QRadioButton('Вариант 3') #вариант 3
rbtn_4 = QRadioButton('Вариант 4') #вариант 4

RadioGroup = QButtonGroup() #добавляем/создаём/включаем модуль
RadioGroup.addButton(rbtn_1) #создаем кнопку 1
RadioGroup.addButton(rbtn_2) #создаем кнопку 2
RadioGroup.addButton(rbtn_3) #создаем кнопку 3
RadioGroup.addButton(rbtn_4) #создаем кнопку 4

layout_ans1 = QVBoxLayout() #отображение по вертикали 1
layout_ans2 = QVBoxLayout() #отображение по вертикали 2
layout_ans3 = QVBoxLayout() #отображение по вертикали 3
layout_ans2.addWidget(rbtn_1) #добавляем лайаут для кнопки 1
layout_ans2.addWidget(rbtn_2) #добавляем лайаут для кнопки 2
layout_ans3.addWidget(rbtn_3) #добавляем лайаут для кнопки 3
layout_ans3.addWidget(rbtn_4) #добавляем лайаут для кнопки 4

layout_ans1.addLayout(layout_ans2) #добавляем лайаут анс 1 на лайаут анс 2
layout_ans1.addLayout(layout_ans3) #добавляем лайаут анс 1 на лайаут анс 2

RadioGroupBox.setLayout(layout_ans1) #сетаем лайаут анс1

AnsGroupBox = QGroupBox("Результат теста")#текст
lb_Result = QLabel('прав ты или нет?')#текст
lb_Correct = QLabel('ответ будет тут!')#текст

layout_res = QVBoxLayout()#отображение вертикали
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))#отобразить слева сверху
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)#отоброжение по горизонтали
AnsGroupBox.setLayout(layout_res)#сет лайаут для результатов

layout_line1 = QHBoxLayout()#отоброжение по горизонтали
layout_line2 = QHBoxLayout()#отоброжение по горизонатали
layout_line3 = QHBoxLayout()#отоброжение по горизонтали

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))#отобразить по центру сверху
layout_line2.addWidget(RadioGroupBox)#добавляем виджет к линии 2
layout_line2.addWidget(AnsGroupBox)#добавляем виджет к линии 2
AnsGroupBox.hide#скрываем

layout_line3.addStretch(1)#растягиваем на 1
layout_line3.addWidget(btn_ok, stretch=2)#растягиваем на 2 + кнопка ок
layout_line3.addStretch(1)#растягиваем на 1

layout_card = QVBoxLayout()#отображение по вертикали

layout_card.addLayout(layout_line1, stretch=2)#добавляем лайаут карте линию 1 + растягиваем на 2
layout_card.addLayout(layout_line2, stretch=8)#добавляем лайаут карте линию 2 + растягиваем на 8
layout_card.addStretch(1)#добавляем растяжение 1
layout_card.addLayout(layout_line3, stretch=1)#добавляем лайаут карте линию 3 + растягиваем на 1
layout_card.addStretch(1)#добавляем растяжение 1
layout_card.addSpacing(5)#добавляем растяжение 1

def show_result():#создаем функцию показывающюю результат
    RadioGroupBox.hide()#скрываем вопрос и т.д
    AnsGroupBox.show()#показываем ответы
    btn_ok.setText('Следующий вопрос')#кнопка с текстом

def show_question():#создаем функцию показывающюю вопрос
    RadioGroupBox.show()#показать вопрос
    AnsGroupBox.hide()#скрываем остальное
    btn_ok.setText('Ответить')#кнопка с текстом
    RadioGroup.setExclusive(False)#сетаем эксклюзив на нет
    rbtn_1.setChecked(False)#чек кнопок
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)#сетаем эксклюзив

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]#лист ответов

def ask(q: Question):#создаем функцию вопроса
    shuffle(answers)#мешаем ответы
    answers[0].setText(q.right_answer)#правильный ответ
    answers[1].setText(q.wrong1) #неправильный ответ
    answers[2].setText(q.wrong2) #неправильный ответ
    answers[3].setText(q.wrong3) #неправильный ответ
    lb_Question.setText(q.question) #текст
    lb_Correct.setText(q.right_answer) #текст
    show_question() #показать вопрос

def show_correct(res): #создаем функцию показывающюю правильный ответ
    lb_Result.setText(res) #текст
    show_result() #показать результат

def check_answer():#чекаем ответы
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неправильно!')
            print('Рейтинг: ', (window.score/window.total*100), '%') #

def next_question():#следующий вопрос
    ''' задает случайный вопрос из списка ''' #
    window.total += 1 #
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)  # нам не нужно старое значение, 
                                                        # поэтому можно использовать локальную переменную! 
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = question_list[cur_question] # взяли вопрос
    ask(q) # спросили

def click_ok(): #если нажали кнопку ок
    if btn_ok.text() == 'Ответить': #
        check_answer() #
    else:
        next_question() #

window = QWidget() #создаем окно
window.setLayout(layout_card) #лайаут окна
window.setWindowTitle('Memo Card') #название окна
btn_ok.clicked.connect(click_ok) #чек клика
window.score = 0 #очки
window.total = 0 #вообщем
next_question() #следующий вопрос
window.resize(400, 300) #окно 400 на 300
window.show() #показать окно
app.exec() #показать приложение