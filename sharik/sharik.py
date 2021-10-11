from tkinter import *
from random import randrange as rnd, choice, randint
import time

root = Tk()
root.geometry('800x600')
number_of_balls = 3
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
speedx = [3, 3, 3]
speedy = [3, 2, 3]
colors = ['red', 'orange', 'yellow', 'green', 'blue']
balls = []
poolx = []
pooly = []
poolr = []
sc_main = 0
sc = 0
boss = []
speedy_boos = 5
speedx_boss = 6
gde_b00s = False
cheto_budet = 10
count = None

def new_ball():
    boss.clear()
    balls.clear()
    pooly.clear()
    poolx.clear()
    poolr.clear()
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
    if sc >= cheto_budet:
        root.after(1000, create_boss)
        gde_b00s = True
    else:
        root.after(4000, new_ball)
        gde_b00s = False


def create_boss():
    global gde_b00s
    boss.clear()
    canv.delete(ALL)
    x = rnd(100, 500)
    y = rnd(100, 400)
    r = 60
    chort(x, y, r)
    if sc >= cheto_budet:
        root.after(100, create_boss)
        gde_b00s = True
    else:
        root.after(4000, new_ball)
        gde_b00s = False


def chort(x, y, r):
    boss.append(canv.create_polygon((2 * x + r) / 2 - 6, y - r / 2, (2 * x + r) / 2 + 6, y - r / 2, (2 * x + r) / 2 + 7, y - 2 * r))
    boss.append(canv.create_polygon((2 * x - r) / 2 - 7, y - r / 2, (2 * x - r) / 2 + 7, y - r / 2, (2 * x - r) / 2 + 7, y - 2 * r))
    boss.append(canv.create_oval(x - r, y - r, x + r, y + r, fill="red", width=0))
    boss.append(canv.create_oval((2*x - r)/2 - 10, (2*y-r)/2 - 10, (2*x - r)/2 + 10, (2*y-r)/2 + 10, fill="black", width=0))
    boss.append(canv.create_oval((2 * x + r) / 2 - 10, (2 * y - r) / 2 - 10, (2 * x + r) / 2 + 10, (2 * y - r) / 2 + 10,
                     fill="black", width=0))


def move_boss():
    global speedy_boos
    global speedx_boss
    for i in range(5):
        canv.move(boss[i], speedx_boss, speedy_boos)
        if 2*75 > canv.coords(boss[1])[2] or canv.coords(boss[1])[2] >= 600:
            speedx_boss = - speedx_boss
        if 2*75 > canv.coords(boss[1])[3] or canv.coords(boss[1])[3] >= 400:
            speedy_boos = - speedy_boos
    if sc >= cheto_budet:
        root.after(100, move_boss)
    else:
        root.after(10, move)


def move():
    global speedy
    global speedx
    for i in range(number_of_balls):
        canv.move(balls[i], speedx[i], speedy[i])
        if 0 + 2*r > canv.coords(balls[i])[2] or canv.coords(balls[i])[2] >= 800:
            speedx[i] = - speedx[i]
        if 0 + 2*r > canv.coords(balls[i])[3] or canv.coords(balls[i])[3] >= 600:
            speedy[i] = - speedy[i]
    if sc >= cheto_budet:
        root.after(100, move_boss)
    else:
        root.after(10, move)


def score():
    global count
    canv.delete(count)
    global sc
    count = canv.create_text(30, 30, text=str(sc))
    root.after(400, score)


def click(event):
    global cheto_budet
    global sc_main, sc
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




new_ball()
score()
move()
canv.bind('<Button-1>', click)

mainloop()