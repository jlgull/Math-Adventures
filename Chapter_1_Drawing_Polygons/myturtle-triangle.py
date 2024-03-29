# Program to draw triangles, with the ability to pass side length
# Program to show the use of a default value in a function.

# Import section of the code.

import turtle

# End of import section.

# Assign handle for turtle module

tur = turtle.Turtle()

# End of assignment section.

# Assign shape and speed to turtle

tur.shape('turtle')
tur.speed(1)


# Define a function to draw a square.

def triangle(side_length=120):
    for i in range(3):
        tur.forward(side_length)
        tur.right(120)


# End of function definition

# Use the following code to draw 4 sets of 3 triangles

numtriangles = int(input("Enter the number of Triangles you want to see: "))

for x in range(numtriangles):

    # Use square function to draw 3 squares

    triangle(40)

    triangle(80)

    triangle()

    tur.right(360 / numtriangles)


turtle.exitonclick()
