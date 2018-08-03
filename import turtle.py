import turtle
import tkinter as ti

wn = turtle.Screen()
alex = turtle.Turtle()


def drawRect():
    alex.speed(0)
    alex.up()
    alex.fillcolor("green")
    alex.begin_fill()
    alex.setpos(-250, -100)
    alex.down()
    for i in range(2):
        alex.forward(500)
        alex.left(90)
        alex.forward(300)
        alex.left(90)
    alex.end_fill()
drawRect()



def drawCircle():
    alex.speed(0)
    alex.up()
    alex.setpos(10, -50)
    alex.down()
    alex.fillcolor("red")
    alex.begin_fill()
    alex.circle(100)
    alex.end_fill()
drawCircle()
ti.mainloop()
