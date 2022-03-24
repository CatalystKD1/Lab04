import turtle
import time

def go(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
def clear():
  t.clear()
  
def rightD(x):
    t.forward(x)
    t.right(90)
def leftD(y):
    t.forward(y)
    t.left(90)

t = turtle.Turtle()
def draw(x, y, z):
  '''
  go() I had the go function here to make things look nicer.
  However it would look better if I would declare it at the bottom so I can dynamicaly change the values or just not erase it just yet
  '''
  i = 0
  while i < z:
    rightD(x)
    leftD(y)
    i += 1

go(-50, 50)
draw(10, 10, 10)
clear()

go(50, -50)
draw(-10, -10, 10)
clear()

go(0,0)
draw(10,2, 5)
clear()

go(0,0)
draw(5, 10, 10)
clear()

go(-50, 50)
draw(10, 10, 10)
go(50, 50)
draw(-10, 10, 10)

time.sleep(5)
t.hideturtle()
t.clear()