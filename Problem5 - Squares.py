# Nousheen Siddiqui
# Edited on 02/25/21
# Use the following chunk of code as a base to produce the image shown below.


import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
drawSquare(alex, 50)
sizelist=[50,40,30,20,10]
for i in sizelist:
    drawSquare(alex,i)
    alex.penup()
    alex.left(45)
    alex.forward(i/5)
    alex.right(45)
    alex.pendown()
wn.exitonclick()

