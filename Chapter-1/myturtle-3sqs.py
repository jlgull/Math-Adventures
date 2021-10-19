# Program to show the use of a default value in a function.

# Import section of the code.

import turtle

# End of import section.

# Assign handle for turtle module

tur = turtle.Turtle()

# End of assignment section.

# Assign shape and speed to turtle

tur.shape('turtle')
tur.speed(0)


# Define a function to draw a square.

def square(side_length=100):
    for i in range(4):
        tur.forward(side_length)
        tur.right(90)


# End of function definition

# Use the following code to draw 4 sets of 3 squares

for x in range(10):

    # Use square function to draw 3 squares

    square(50)

    square(30)

    square()

    tur.right(36)


turtle.exitonclick()
