# coding:utf-8
'''
使用Python的turtle模块绘制国旗
'''

import turtle

def draw_rectangle(x,y,width,height):
    #绘制矩形
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.goto(x,y)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def main():
    turtle.penup()
    x,y = -300,-100
    #画国旗主体
    width,height= 540,360
    draw_rectangle(x,y,width,height)
    turtle.pendown()
    # 隐藏箭头
    turtle.ht()
    #显示绘制窗口
    turtle.mainloop()


if __name__ == '__main__':
    main()