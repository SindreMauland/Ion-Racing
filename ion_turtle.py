#from tkinter import PhotoImage
import time
import turtle
screen = turtle.Screen()
screen.setup(width=1346, height=485)
screen.setworldcoordinates(-1346, -485, 1346, 485)
screen.bgcolor("black")
# screen.bgpic("ion/dashboard/ION-Racing_editedgif.gif")
screen.register_shape("ION-Racing_editedgif.gif")
turtle.shape("ION-Racing_editedgif.gif")
screen.colormode(255)
screenTk = screen.getcanvas().winfo_toplevel()
#screenTk.attributes("-fullscreen", True)
# screen.mainloop()
print('hei')
turtle_hex_1 = turtle.Turtle()
#turtle.register_shape("last_ned.gif")
#turtle_hex_1.shape("last_ned.gif")
turtle_hex_1.hideturtle()
turtle_hex_1.color(17, 158, 217)
turtle_hex_1.penup()
turtle_hex_2 = turtle.Turtle()
turtle_hex_2.hideturtle()
turtle_hex_2.color(17, 158, 217)
turtle_hex_2.penup()
turtle_hex_3 = turtle.Turtle()
turtle_hex_3.hideturtle()
turtle_hex_3.color(17, 158, 217)
turtle_hex_3.penup()
turtle_hex_4 = turtle.Turtle()
turtle_hex_4.hideturtle()
turtle_hex_4.color(17, 158, 217)
turtle_hex_4.penup()
turtle_hex_5 = turtle.Turtle()
turtle_hex_5.hideturtle()
turtle_hex_5.color(17, 158, 217)
turtle_hex_5.penup()
turtle_hex_6 = turtle.Turtle()
turtle_hex_6.hideturtle()
turtle_hex_6.color(17, 158, 217)
turtle_hex_6.penup()
print('hei')
#turtle_hex_1.right(0)
turtle_hex_1.speed(0)
turtle_hex_2.speed(0)
turtle_hex_3.speed(0)
turtle_hex_4.speed(0)
turtle_hex_5.speed(0)
turtle_hex_6.speed(0)

turtle_hex_2.right(60)
turtle_hex_3.right(120)
turtle_hex_4.right(180)
turtle_hex_5.right(240)
turtle_hex_6.right(300)

turtle_hex_1.setx(-1090)
turtle_hex_1.sety(271)
turtle_hex_1.pendown()
turtle_hex_1.begin_fill()

turtle_hex_2.setx(-954)
turtle_hex_2.sety(261)
turtle_hex_2.pendown()
turtle_hex_2.begin_fill()

turtle_hex_3.setx(-892)
turtle_hex_3.sety(139)
turtle_hex_3.pendown()
turtle_hex_3.begin_fill()

turtle_hex_4.setx(-968)
turtle_hex_4.sety(25)
turtle_hex_4.pendown()
turtle_hex_4.begin_fill()

turtle_hex_5.setx(-1104)
turtle_hex_5.sety(35)
turtle_hex_5.pendown()
turtle_hex_5.begin_fill()

turtle_hex_6.setx(-1164)
turtle_hex_6.sety(157)
turtle_hex_6.pendown()
turtle_hex_6.begin_fill()
print('hei')

#turtle_hex_1.speed(4)
#turtle_hex_2.speed(4)
#turtle_hex_3.speed(4)
#turtle_hex_4.speed(3)
#turtle_hex_5.speed(3)
#turtle_hex_6.speed(3)
turtle_hex_1.speed(7)
turtle_hex_2.speed(7)
turtle_hex_3.speed(7)
turtle_hex_4.speed(7)
turtle_hex_5.speed(7)
turtle_hex_6.speed(7)

print('hei')
for i in range(0, 6):
    turtle_hex_1.forward(122)
    turtle_hex_1.left(60)
    turtle_hex_2.forward(122)
    turtle_hex_2.left(60)
    turtle_hex_3.forward(122)
    turtle_hex_3.left(60)
    turtle_hex_4.forward(122)
    turtle_hex_4.left(60)
    turtle_hex_5.forward(122)
    turtle_hex_5.left(60)
    turtle_hex_6.forward(122)
    turtle_hex_6.left(60)

    # turtle_hex_1.left(60)
    # turtle_hex_2.left(60)
    # turtle_hex_3.left(60)
    # turtle_hex_4.left(60)
    # turtle_hex_5.left(60)
    # turtle_hex_6.left(60)


turtle_hex_1.end_fill()
time.sleep(0.3)
turtle_hex_2.end_fill()
time.sleep(0.3)
turtle_hex_3.end_fill()
time.sleep(0.3)
turtle_hex_4.end_fill()
time.sleep(0.3)
turtle_hex_5.end_fill()
time.sleep(0.3)
turtle_hex_6.end_fill()


turtle.done()
