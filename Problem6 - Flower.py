# Nousheen Siddiqui
# Edited on 02/25/2021
# Use the polygon program from the last module and convert it to a function.


import turtle
wn = turtle.Screen()
flower = turtle.Turtle()
flower.shape("classic")
flower.color("pink")
flower.pensize(2)


def drawshape(sides_poly, length_poly, angle):
    for i in range(sides_poly):
        flower.forward(length_poly)
        flower.right(angle)
for i in range(10):
    flower.right(35)
    drawshape(6,50,60)
    #for a in range(6):
        #flower.forward(50)
        #flower.right(60)

