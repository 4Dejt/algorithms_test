import turtle


t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 200)
t.pendown()

def hilbert_curve(t, step, lenght, angle):
    if step == 0:
        t.left(-angle)
        t.forward(lenght)
        t.left(angle)
        t.forward(lenght)
        t.left(angle)
        t.forward(lenght)
        t.left(-angle)
    else:
        t.left(-angle)
        hilbert_curve(t, step-1, lenght, -angle)
        t.forward(lenght)
        t.left(angle)
        hilbert_curve(t, step - 1, lenght, angle)
        t.forward(lenght)
        hilbert_curve(t, step-1, lenght, angle)
        t.left(angle)
        t.forward(lenght)
        hilbert_curve(t, step-1, lenght, -angle)
        t.left(-angle)


hilbert_curve(t, 3, 30, 90)



turtle.mainloop()