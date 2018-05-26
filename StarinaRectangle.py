import turtle
import math

# Set the background color
screen = turtle.Screen()
screen.bgcolor("White")

# Create our turtle
george = turtle.Turtle()
george.color("black")
george.shape("turtle")
george.speed(1000000000000000)

# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  

# Draw and fill the red rectangle 
george.penup() 
george.goto(-250, -250)
george.pendown()
drawRectangle(george,500, 400, "red")

# # Draw and fill the star

star = turtle.Turtle()
star.penup()
star.goto(-120, 0)
star.pendown()
star.pencolor("yellow")
star.fillcolor("yellow" )
star.begin_fill()

for i in range(5):
    star.forward(250)
    star.right(144)
star.end_fill()
turtle.done()
