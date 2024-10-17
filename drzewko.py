import turtle


tt = turtle.Turtle()
tt.speed(0)

tt.penup()
tt.width(2)
tt.pencolor("green")
tt.left(90)
tt.back(200)
tt.pendown()

def tree(t, lenght, angle, step):
    if step > 0:
        t.forward(lenght)
        lenght = 2/3 * lenght
        t.left(angle/2)
        tree(t, lenght, angle, step - 1)
        t.back(lenght)
        t.right(angle)
        tree(t, lenght, angle, step - 1)
        t.back(lenght)
        t.left(angle / 2)
    else:
        t.forward(lenght)


tree(tt, 200, 110, 5)

turtle.done()