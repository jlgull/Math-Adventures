# Program to draw polygons, with the ability to select the number of sides
# pass side length and number of polygons.
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

def polygon(side_length=120, num_sides=3):
    for i in range(num_sides):
        tur.forward(side_length)
        tur.right(360/num_sides)


# End of function definition

# Enter the required data for the program.
# The names are as sel-explanatory as possible.

num_sides = int(input("Enter the number of Sides for the polygon: "))
side_length = int(input("Enter a value for the length of each side of the Polygon: "))
num_polygons = int(input("Enter the number of Polygons to draw: "))


for x in range(num_polygons):

    # Use polygon function to draw polygons

    polygon(side_length, num_sides)

    tur.right(360 / num_sides / 2)


turtle.exitonclick()
