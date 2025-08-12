import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(500,500)
square=turtle.Turtle()
num_sides=4
side_length=70
angle=360/num_sides
for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)
turtle.done()
