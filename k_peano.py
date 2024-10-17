import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300, -300)
t.pendown()

def peano_curve(t, lenght, step, angle):
    if step == 0:
        for i in range(2):
            t.forward(lenght)
            t.left(angle)
            t.forward(lenght / 2)
            t.left(angle)
            angle *= -1
        t.forward(lenght)
    else:
        peano_curve(t, lenght, step - 1, angle)
        t.forward(lenght / 2)
        peano_curve(t, lenght, step-1, -angle)
        t.forward(lenght / 2)
        peano_curve(t, lenght, step - 1, angle)
        t.left(angle)
        t.forward(lenght / 2)
        t.left(angle)
        peano_curve(t, lenght, step - 1, -angle)
        t.forward(lenght / 2)
        peano_curve(t, lenght, step - 1, angle)
        t.forward(lenght / 2)
        peano_curve(t, lenght, step - 1, -angle)
        t.left(-angle)
        t.forward(lenght / 2)
        t.left(-angle)
        peano_curve(t, lenght, step - 1, angle)
        t.forward(lenght / 2)
        peano_curve(t, lenght, step - 1, -angle)
        t.forward(lenght / 2)
        peano_curve(t, lenght, step - 1, angle)



peano_curve(t, 50, 2, 90)





turtle.mainloop()