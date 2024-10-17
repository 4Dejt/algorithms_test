import turtle


rafal = turtle.Turtle()
rafal.speed(0)
rafal.color('darkred')

rafal.penup()
rafal.goto(-250,-250)
rafal.pendown()

def sierpinski_carpet(t, lenght, step):
    if step > 0:
        for i in range(4):
            sierpinski_carpet(t, lenght/3, step-1)
            t.forward(lenght / 3)
            sierpinski_carpet(t, lenght / 3, step - 1)
            t.forward(2 * lenght / 3)
            t.left(90)
    else:
        t.begin_fill()
        for i in range(4):
            t.forward(lenght)
            t.left(90)
        t.end_fill()


sierpinski_carpet(rafal, 500, 3)

turtle.done()