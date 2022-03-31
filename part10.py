import shapes as s
x = -120
y = 100
color1 = "orange"
color2 = "blue"
for i in range(4):
  s.draw_row(x, y, color1, color2)
  y = y - 20
  s.draw_row(x, y, color2, color1)
  y = y - 20
s.end()