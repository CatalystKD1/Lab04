import turtle
import time

t = turtle.Turtle()
t.speed(100)
def square(color):
  t.color(color)
  t.begin_fill()
  for i in range(4):
    t.right(90)
    t.forward(20)
  t.end_fill()
  
def position_turtle(x, y):
  t.hideturtle()
  t.penup()
  t.goto(x, y)
  t.showturtle()
  t.pendown()

def draw_row(x, y, color1, color2):
  for i in range(4):
    x = x + 20
    position_turtle(x, y)
    square(color1)

    x = x + 20
    position_turtle(x, y)
    square(color2)
def end():
  time.sleep(5)
  t.hideturtle()
  t.clear()