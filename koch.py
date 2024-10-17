import turtle

def koch_curve(t, n, length, d, angle):
    if n == 0:
        t.forward(length)
    else:
        n -= 1
        length = length / d
        koch_curve(t, n, length, d, angle)
        t.left(angle)
        koch_curve(t, n, length, d, angle)
        t.right(angle * 2)
        koch_curve(t, n, length, d, angle)
        t.left(angle)
        koch_curve(t, n, length, d, angle)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

for i in range(3):
    koch_curve(t, 2, 400, 3, 60)
    t.right(120)

turtle.mainloop()