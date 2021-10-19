# Draw a complex circle
# Using a function to make a square

# Import module section of the code
import turtle

# End of module import section.

# Assign a handle for the Turtle Module
tur = turtle.Turtle()

# Assign the shape and speed of the drawing tool.
tur.shape('turtle')
tur.speed(9)

# Define function to create a square


def square():
    for i in range(4):
        tur.forward(100)
        tur.right(90)


# Make 60 squares in a circle

for a in range(60):
    square()
    tur.right(6)

turtle.exitonclick()
