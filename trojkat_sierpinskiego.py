import turtle

t = turtle.Turtle()
t.speed(0)
t.color('lime')

points = [(-300, -300), (0, 250), (300, -300)]

def draw(t, points, step):
    if step == 0:
        t.begin_fill()
        t.penup()
        t.goto(*points[0])
        t.pendown()
        t.goto(*points[1])
        t.goto(*points[2])
        t.goto(*points[0])
        t.end_fill()
    else:
        draw(t, [points[0], get_middle(points[0], points[1]), get_middle(points[2], points[0])], step - 1)
        draw(t, [get_middle(points[0], points[1]), points[1], get_middle(points[1], points[2])], step - 1)
        draw(t, [get_middle(points[0], points[2]), get_middle(points[1], points[2]), points[2]], step - 1)


def get_middle(p,q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)

draw(t, points, 5)

turtle.done()