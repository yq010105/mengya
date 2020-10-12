import turtle as t
import time
import datetime as dt
# import threading
# import configparser
from PIL import ImageGrab

def drawuse():
    # background
    # cf = configparser.ConfigParser()
    # cf.read('config.ini')
    # w ,h ,x, y= cf.getint('clock','w'),cf.getint('clock','h'),cf.getint('clock','x'),cf.getint('clock','y')
    w , h , x , y = 500,500,0,50
    game = t.Screen()
    game.bgcolor('#A4D3EE')
    game.setup(w,h,x,y)
    game.tracer(0)

    pen = t.Turtle()
    pen.ht()
    pen.speed(0)
    pen.up()
    pen.pensize(3)
    
    def draw():
        i = 0
        while True:
            pen.clear()
            # 圆
            pen.pensize(3)
            pen.up()
            pen.color('black')
            pen.goto(0,-200)
            pen.down()
            pen.seth(0)
            pen.circle(200)

            # 刻度
            pen.up()
            pen.goto(0,0)
            pen.seth(225)

            for _ in range(13):
                pen.fd(180)
                pen.down()
                pen.fd(20)
                pen.up()
                pen.goto(0,0)
                pen.right(22.5)

            # 指针
            pen.up()
            pen.goto(0,0)
            pen.down()
            pen.seth(225 - i)
            pen.color('red')
            pen.pensize(6)
            pen.fd(120)
            i += 1
            if i >= 271:
                i = 0
            game.update()
            time.sleep(1)

    def drawgd(thr):
        pen.clear()
        # 圆
        pen.up()
        pen.color('black')
        pen.goto(0,-200)
        pen.down()
        pen.seth(0)
        pen.circle(200)

        # 刻度
        pen.up()
        pen.goto(0,0)
        pen.seth(225)

        for _ in range(13):
            pen.fd(180)
            pen.down()
            pen.fd(20)
            pen.up()
            pen.goto(0,0)
            pen.right(22.5)

        # 指针
        pen.up()
        pen.goto(0,0)
        pen.down()
        pen.seth(225 - thr)
        pen.color('red')
        pen.pensize(6)
        pen.fd(120)
        game.update()
        time.sleep(1)

    # 模式一--动态
    draw()

    # # 模式二--固定
    # thr = int(input("输入指针度数:--角度--"))
    # drawgd(thr)

    game.mainloop()

def dclock():
    img = ImageGrab.grab((17,110,630,710))
    img.save('dclock.jpg','JPEG')

if __name__ == '__main__':
    drawuse()
    dclock()