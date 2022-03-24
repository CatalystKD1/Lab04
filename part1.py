import turtle
import time

t = turtle.Turtle()
i = 0
while i < 7:
  t.forward(10)
  t.left(50)
  t.forward(10)
  t.right(100)
  i += 1
  
t.home()
time.sleep(5)
t.clear()