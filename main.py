import turtle
t = turtle.Turtle()
def stairs(x):
  i = 0
  while i < 10:
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.left(90)
    i += 1
stairs(10)