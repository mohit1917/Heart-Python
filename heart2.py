import turtle

t = turtle.Turtle()

t.fillcolor('red')
t.begin_fill()

t.left(45)
t.forward(150)
t.circle(75, 180)
t.right(90)
t.circle(75, 180)
t.forward(150)

t.end_fill()
turtle.done()
