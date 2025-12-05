import turtle
import time

def draw_clean_skull(t):
    t.hideturtle()
    t.speed(0)
    t.color("white")
    t.pensize(4)

    # --------------------
    # Skull Head (clean)
    # --------------------
    t.penup()
    t.goto(0, 30)
    t.setheading(0)
    t.pendown()
    t.circle(60)  # smoother round skull

    # --------------------
    # Jaw (rectangle)
    # --------------------
    t.penup()
    t.goto(-45, 30)
    t.setheading(-90)
    t.pendown()
    t.forward(70)
    t.setheading(0)
    t.forward(90)
    t.setheading(90)
    t.forward(70)

    # --------------------
    # Eyes (simple ovals)
    # --------------------
    t.penup()
    t.goto(-25, 60)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(25, 60)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    # --------------------
    # Nose
    # --------------------
    t.penup()
    t.goto(0, 40)
    t.pendown()
    t.begin_fill()
    t.setheading(-90)
    t.forward(15)
    t.left(120)
    t.forward(15)
    t.left(120)
    t.forward(15)
    t.end_fill()

    # --------------------
    # Teeth (clean vertical lines)
    # --------------------
    t.pensize(3)
    for x in [-20, -10, 0, 10, 20]:
        t.penup()
        t.goto(x, 30)
        t.setheading(-90)
        t.pendown()
        t.forward(40)

    # --------------------
    # Crossbones
    # --------------------
    t.pensize(7)
    t.color("white")

    t.penup()
    t.goto(-90, -20)
    t.setheading(30)
    t.pendown()
    t.forward(180)

    t.penup()
    t.goto(90, -20)
    t.setheading(150)
    t.pendown()
    t.forward(180)


