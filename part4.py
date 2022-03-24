import turtle
t = turtle.Turtle()
def go():
  t.clear()
  t.penup()
  t.goto(-50, 50)
  t.pendown()

def steps_10(x, y):
  go()
  i = 0
  while i < 10:
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    i += 1
steps_10(10, 10)

def steps_2(x, y):
  go()
  i = 0
  while i < 10:
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    i += 1
steps_10(10, 2)

def steps_5(x, y):
  go()
  i = 0
  while i < 10:
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    i += 1
steps_5(10, 5)

def steps_15(x, y):
  go()
  i = 0
  while i < 10:
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    i += 1
steps_15(10, 15)