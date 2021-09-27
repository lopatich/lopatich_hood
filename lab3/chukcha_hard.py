from graph import *
import math

windowSize(794, 1123)
canvasSize(794, 1123)
penColor(230, 230, 230)
brushColor(230, 230, 230)
rectangle(0, 0, 794, 200)

def ellips1(x0, y0, a, b, ang):
    x = -a
    h = 0.4
    t = math.radians(ang)
    points1 = []
    points2=[]
    while x < a:
        y = b * math.sqrt(1 - (x ** 2 / a ** 2))
        xe1 = x0 - (x*math.cos(t)-y*math.sin(t))
        xe2 = x0 + (x*math.cos(t)-y*math.sin(t))
        ye1 = y0 + (x * math.sin(t) + y * math.cos(t))
        ye2 = y0 - (x * math.sin(t) + y * math.cos(t))
        points1.append((xe1, ye1))
        points2.append((xe2,ye2))
        x += h
    polygon(points1)
    polygon(points2)

def ellips(x0,y0, a, b):
    x = -a
    h = 0.2
    points = []
    while x <= a:
        y = b * math.sqrt(1 - (x ** 2 / a ** 2))
        xe = x0 + x
        ye1 = y0 - y
        ye2 = y0 + y
        points.append((xe, ye1))
        points.append((xe, ye2))
        x += h
    polygon(points)

def domik (x0, y0, mashtab):
    x = -190
    h = 0.2
    penColor('black')
    brushColor(230, 230, 230)
    points = []
    while x <= 190:
        y = math.sqrt(190**2 - x**2)
        xe = x0 + mashtab*x
        ye = y0 - mashtab*y
        points.append((xe, ye))
        x += h
    polygon(points)
    for i in range(4):
        penColor("black")
        line(x0-math.sqrt(190**2-(190/4*i)**2)*mashtab, y0-190/4*i*mashtab,
             x0+math.sqrt(190**2-(190/4*i)**2)*mashtab, y0-190/4*i*mashtab)
        for g in range(5-i):
            line(x0-math.sqrt(190**2-(190/4*i)**2)*mashtab + (g+1)*(x0+math.sqrt(190**2-(190/4*i)**2))/(7-i)*mashtab, y0-190/4*i*mashtab,
                 x0-math.sqrt(190**2-(190/4*i)**2)*mashtab + (g+1)*(x0+math.sqrt(190**2-(190/4*i)**2))/(7-i)*mashtab, y0-190/4*(i+1)*mashtab)

def chukcha(x0, y0, mashtab, right):
    penColor(227, 222, 219)
    brushColor(227,222,219)
    ellips(x0, y0-150*mashtab, 67*mashtab, 40*mashtab)

    penColor(145, 124, 111)
    brushColor(145, 124, 111)
    ellips(x0 + 53*mashtab, y0 + 28*mashtab, 25*mashtab, 8*mashtab)
    ellips(x0 - 45*mashtab, y0 + 28*mashtab, 25*mashtab, 10*mashtab)
    ellips(x0 - 34*mashtab, y0 + 1*mashtab, 18*mashtab, 24*mashtab)
    ellips(x0 + 35*mashtab, y0 + 3*mashtab, 18*mashtab, 24*mashtab)



    x = -77.5
    h = 0.2
    penColor(145, 124, 111)
    brushColor(145, 124, 111)
    points = []
    while x <= 77.5:
        y = 150*math.sqrt(1-(x**2/77.5**2))
        xe = x0 + mashtab * x
        ye = y0 - mashtab * y
        points.append((xe, ye))
        x += h
    polygon(points)
    penSize(30*mashtab)
    penColor(108, 93, 83)
    line(x0, y0-150*mashtab, x0, y0)
    line(x0 - 77*mashtab, y0, x0 + 78*mashtab, y0)

    penSize(1)
    penColor(172, 157, 147)
    brushColor(172, 157, 147)
    ellips(x0, y0-150*mashtab,51*mashtab, 32*mashtab)
    penColor(227, 219, 219)
    brushColor(227, 219, 219)
    ellips(x0, y0 - 150*mashtab, 33*mashtab, 21*mashtab)
    penColor('black')
    line(x0-13*mashtab, y0-155*mashtab, x0-30*mashtab, y0-162*mashtab)
    line(x0+4*mashtab, y0 - 155*mashtab, x0+22*mashtab, y0 - 158*mashtab)
    def smile(x05, y05, mashtab5):
        k = 0.2
        x5 = -14
        points5 = []
        while x5 <= 14:
            y5 = x5 ** 2 /50
            xe5 = x05 + mashtab5 * x5
            ye5 = y05 + mashtab5 * y5
            points5.append((xe5, ye5))
            x5 += k
        penColor('black')
        polyline(points5)

    smile(x0+1*mashtab, y0 - 143*mashtab, mashtab)

    if right:
        penColor(145, 124, 111)
        brushColor(145, 124, 111)
        ellips(x0-70*mashtab, y0-96*mashtab, 38*mashtab, 12*mashtab)
        ellips1(x0 + 72*mashtab, y0-74*mashtab, 38*mashtab, 12*mashtab, 135)
        penColor('black')
        line(x0 - 77*mashtab, y0 + 20*mashtab, x0 - 112*mashtab, y0 - 190*mashtab)

    else:
        penColor(145, 124, 111)
        brushColor(145, 124, 111)
        ellips(x0 + 68*mashtab, y0-96*mashtab, 38*mashtab, 12*mashtab)
        ellips1(x0-69*mashtab, y0 - 78*mashtab, 38*mashtab, 12*mashtab, 45)
        penColor('black')
        line(x0 + 88*mashtab, y0 + 20*mashtab, x0 + 83*mashtab, y0 - 190*mashtab)

def kotick(x0, y0, mastab):

    brushColor(204, 204, 204)
    penColor(204, 204, 204)
    ellips(x0, y0, 70, 16)
    ellips1(x0 + 62, y0 + 33, 55, 6, 160)
    ellips1(x0 + 87, y0 +21, 55, 6, 160)
    ellips1(x0 + 114, y0 - 37, 60, 8, 30)
    ellips1(x0-59, y0 + 28, 55, 8, 30)
    ellips1(x0 - 84, y0 + 9, 55, 8, 15)

    penColor(147, 172, 167)
    penSize(1)
    brushColor(147, 172, 167)
    ellips1(x0 - 72, y0 - 17, 30, 8, 160)
    polygon([(x0-52, y0 -9), (x0 - 31, y0-9), (x0 - 31, y0 -1)])

    penColor("white")
    penSize(2)
    line(x0 - 61, y0 - 13, x0 - 61, y0 - 8)
    line(x0 - 72, y0-12, x0 -72, y0-18)

    brushColor(204, 204, 204)
    penColor(204, 204, 204)

    ellips(x0-52, y0 - 28, 26, 18)
    ellips1(x0 - 66, y0 - 17, 8, 2, 135)
    polygon([(x0-42, y0-53), (x0-42, y0-41), (x0-30, y0-41)])
    polygon([(x0-64, y0-55), (x0-64, y0 - 43), (x0-52, y0-43)])
    brushColor("white")
    penColor('white')
    ellips(x0-50, y0 - 28, 5, 3)
    ellips(x0-66, y0 -33, 5, 3)
    penColor('black')
    brushColor('black')
    circle(x0-48, y0-28, 3)
    circle(x0-64, y0-33, 3)
    circle(x0-66, y0 - 22, 2)
    penColor("white")


domik(89, 235,0.4)
domik(256, 339, 1)
domik(146, 398,0.5)
domik(306, 459,0.5)

chukcha(518, 333, 0.3, False)
chukcha(726, 267, 0.4, True)
chukcha(636, 257, 0.4, False)
chukcha(632.5, 506, 1, False)
chukcha(532, 340, 0.6, True)

kotick(344,553, 1)
kotick(181,724,1)
kotick(560, 744,1 )


run()