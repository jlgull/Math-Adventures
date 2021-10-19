# Draw a complex circle within a circle
# Using a function to make a square

# Import module section of the code
import turtle

# End of module import section.

# Assign a handle for the Turtle Module
tur = turtle.Turtle()

# Assign the shape and speed of the drawing tool.
tur.shape('turtle')
tur.speed(0)

# Define function to create a square, which accepts a line length


def square(side_length):
    for i in range(4):
        tur.forward(side_length)
        tur.right(90)


# Make 60 squares in a circle
for num in range(1, 6):

    for a in range(60):
        square(num * 50)
        tur.right(6)

turtle.exitonclick()
