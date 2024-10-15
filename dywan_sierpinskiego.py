import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-100, -100)
t.pendown()
t.color('tomato')

def draw(t, length, step):
    if step == 0:
        t.begin_fill()
        for i in range(4):
            t.forward(length)
            t.left(90)
        t.end_fill()
    else:
        for _ in range(4):
            draw(t, length / 3, step - 1)
            t.forward(length / 3)
            draw(t, length / 3, step - 1)
            t.forward(length / 3)
            draw(t, length / 3, step - 1)
            t.forward(length / 3)
            t.left(90)



draw(t, 150, 3)
turtle.done()