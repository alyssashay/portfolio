from turtle import *
import math

# Name your Turtle.
john = Turtle(shape="turtle")

#Set Up your screen and starting position.
#octagon
john.penup()
x_pos = 200
y_pos = 0
john.setposition(x_pos, y_pos)
john.pendown()
john.begin_fill()
john.color("black", "thistle")
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)
john.right(45)
john.forward(75)

john.end_fill()

#triangle
john.penup()
x_pos = 100
y_pos = 100
john.setposition(x_pos, y_pos)
john.pendown()
john.begin_fill()
john.color("black", "coral")
john.right(120)
john.forward(100)
john.right(120)
john.forward(100)
john.right(120)
john.forward(100)

john.end_fill()

#square
john.penup()
setup(500,300)
x_pos = 0
y_pos = 0
john.setposition(x_pos, y_pos)
john.pendown()
john.begin_fill()
john.color("black", "powderblue")
john.forward(50)
john.right(90)
john.forward(50)
john.right(90)
john.forward(50)
john.right(90)
john.forward(50)
john.right(90)

john.end_fill()

#rectangle

john.penup()
setup(500,300)
x_pos = -100
y_pos = -100
john.setposition(x_pos, y_pos)
john.pendown()
john.begin_fill()
john.color("black", "mediumaquamarine")
john.forward(90)
john.right(90)
john.forward(30)
john.right(90)
john.forward(90)
john.right(90)
john.forward(30)

john.end_fill()

#10-sided
john.penup()
setup(500,300)
x_pos = -125
y_pos = 50
john.setposition(x_pos, y_pos)
john.pendown()
john.begin_fill()
john.color("black", "palevioletred")
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.right(36)
john.forward(30)
john.end_fill()
### Write your code below:






# Close window on click.
exitonclick()

