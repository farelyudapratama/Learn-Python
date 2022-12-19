import turtle
t = turtle.Turtle()

t.color("red")
t.speed(10)

for i in range(36):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(10)

    for j in range(18):
        t.forward(50)
        t.right(20)

turtle.mainloop()
