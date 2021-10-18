from tkinter import *
from random import randrange as rnd, choice, randint
import time

root = Tk()
root.geometry('800x600')
number_of_balls = 3
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
speedx = [5, 4, 6]
speedy = [6, 2, 3]
colors = ['red', 'orange', 'yellow', 'green', 'blue']
balls = []
poolx = []
pooly = []
poolr = []
sc_main = 0
sc = 0
boss = []
speedy_boos = 7
speedx_boss = 8
gde_b00s = False
cheto_budet = 10
count = None
l_count = None
lose_count = 0
end_game = 5

scoreLabel = Label(root, bg='white', fg='black', width=40)
label = Label(root, bg='white', fg='black', width=40)
label['text'] = 'введите свое имя'
label.pack()
e = Entry(root, width=20)
e.pack()

zapis = True


def new_ball():
    ''' Создает шарики по 3 каждые 4 секунды если количесво очков больше
     определленного то переключается на создаение босса'''
    boss.clear()
    balls.clear()
    pooly.clear()
    poolx.clear()
    poolr.clear()
    global cr, cr_b
    global x, y, r
    global ball
    global gde_b00s
    global cheto_budet
    canv.delete(ALL)
    for i in range(number_of_balls):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        poolx.append(x)
        pooly.append(y)
        poolr.append(r)
        balls.append(canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0))
    if lose_count < end_game:
        if sc >= cheto_budet:
            root.after(4000, create_boss)
            gde_b00s = True
        else:
            root.after(4000, new_ball)
            gde_b00s = False


def create_boss():
    ''' Фукция которая создает обьект босса. при количесве очков больше определленого создается босс '''
    global gde_b00s
    boss.clear()
    canv.delete(ALL)
    x = rnd(100, 500)
    y = rnd(100, 400)
    r = 60
    chort(x, y, r)
    if lose_count < end_game:
        if sc >= cheto_budet:
            root.after(4000, create_boss)
            gde_b00s = True
        else:
            root.after(4000, new_ball)
            gde_b00s = False


def chort(x, y, r):
    """  Функция которая рисует босса(черта)"""
    boss.append(canv.create_polygon((2 * x + r) / 2 - 6, y - r / 2, (2 * x + r) / 2 + 6, y - r / 2, (2 * x + r) / 2 + 7,
                                    y - 2 * r))
    boss.append(canv.create_polygon((2 * x - r) / 2 - 7, y - r / 2, (2 * x - r) / 2 + 7, y - r / 2, (2 * x - r) / 2 + 7,
                                    y - 2 * r))
    boss.append(canv.create_oval(x - r, y - r, x + r, y + r, fill="red", width=0))
    boss.append(canv.create_oval((2 * x - r) / 2 - 10, (2 * y - r) / 2 - 10, (2 * x - r) / 2 + 10, (2 * y - r) / 2 + 10,
                                 fill="black", width=0))
    boss.append(canv.create_oval((2 * x + r) / 2 - 10, (2 * y - r) / 2 - 10, (2 * x + r) / 2 + 10, (2 * y - r) / 2 + 10,
                                 fill="black", width=0))


def move_boss():
    """ особый тип движения для босс"""
    global speedy_boos
    global speedx_boss
    for i in range(5):
        canv.move(boss[i], speedx_boss, speedy_boos)
        if 2 * 75 > canv.coords(boss[2])[2] or canv.coords(boss[2])[2] >= 600:
            speedx_boss = - speedx_boss
        if 2 * 75 > canv.coords(boss[2])[3] or canv.coords(boss[2])[3] >= 400:
            speedy_boos = - speedy_boos
    if gde_b00s:
        root.after(10, move_boss)
    else:
        time.sleep(4)
        root.after(10, move)


def move():
    ''' задаеет движение шарикам переключается на движение босса если босс присутсвует на экране '''
    global speedy
    global speedx
    for i in range(number_of_balls):
        canv.move(balls[i], speedx[i], speedy[i])
        if 0 + 2 * r > canv.coords(balls[i])[2] or canv.coords(balls[i])[2] >= 800:
            speedx[i] = - speedx[i]
        if 0 + 2 * r > canv.coords(balls[i])[3] or canv.coords(balls[i])[3] >= 600:
            speedy[i] = - speedy[i]
    if gde_b00s:
        time.sleep(4)
        root.after(10, move_boss)
    else:
        root.after(10, move)


def score():
    ''' выводит количество попаданий и промахов на экран'''
    global count, lose_count, l_count
    canv.delete(count)
    canv.delete(l_count)
    global sc
    count = canv.create_text(30, 30, text=str(sc))
    l_count = canv.create_text(60, 30, text=str(lose_count))
    root.after(400, score)


def click(event):
    ''' считывает нажатия с мышки считает количесво попаданий и промахов, убирает те шары в которые попал'''
    global cheto_budet
    global sc_main, sc, lose_count
    sc_main = 0
    if gde_b00s:
        center_x = (canv.coords(boss[2])[2] + canv.coords(boss[2])[0]) / 2
        center_y = (canv.coords(boss[2])[3] + canv.coords(boss[2])[1]) / 2
        if (abs(int(center_x - event.x)) ^ 2 + abs(int(center_y - event.y)) ^ 2) < 60 ^ 2:
            sc_main += 1
        if sc_main >= 1:
            print('ваще четко')
            sc += 5
            cheto_budet += 20
            print(cheto_budet)
            print(sc)
        else:
            lose_count += 1
            print('ваще не четко')
    else:
        for i in range(number_of_balls):
            center_x = (canv.coords(balls[i])[2] + canv.coords(balls[i])[0]) / 2
            center_y = (canv.coords(balls[i])[3] + canv.coords(balls[i])[1]) / 2
            if (abs(int(center_x - event.x)) ^ 2 + abs(int(center_y - event.y)) ^ 2) < poolr[i] ^ 2:
                sc_main += 1
                canv.delete(balls[i])
                balls[i] = canv.create_oval(center_x, center_y, center_x, center_y, fill='white', width=0)
        if sc_main >= 1:
            print('четко')
            sc += 1
        else:
            print('не четко')
            lose_count += 1


def lose():
    ''' начинает выполнятся с определенного количесвта промахов, останавливает шары на экране, не дает появлятся новым
    выводит на экран счет и записывает его в текстовы дркумент'''
    global speedy, speedx, speedy_boos, speedx_boss, cr, cr_b, zapis
    if lose_count >= end_game:
        speedy = [0, 0, 0]
        speedx = [0, 0, 0]
        speedy_boos = 0
        speedx_boss = 0
        canv.create_text(400, 300, text='Неплохо сыграли! Ваш счет:' + str(sc))
        if zapis:
            name = e.get()
            file = open('results.txt', 'a')
            file.write(name + ' ' + str(sc) + "\n")
            file.close()
            zapis = False

    root.after(400, lose)


new_ball()
score()
move()
canv.bind('<Button-1>', click)
lose()

mainloop()
