# New file for Chapter 5
# Working in Geometry
#
# Basic setup

def setup():
    size(600, 600)
    

# Draw simple circles (Listing 5-1)

def draw():
    # Draw a circle
    ellipse(200, 100, 20, 20)
    ellipse(200, 300, 20, 20)

# Draw a rectangle (Listing 5-2)

def draw():
    rect(20, 40, 50, 30)

# Draw a rectangle and use translate
#   (Listing 5-3)
def draw():
    translate(50, 80)
    rect(50, 100, 100, 60)

# Draw a rectangle and use translate
#   (Listing 5-4)

def draw():
   translate(width/2, height/2)
   rect(50, 100, 100, 60)

# Draw a rectangle and use rotate
#   (Figure 5-8 left)

def draw():
   rotate(radians(20));
   rect(50, 100, 100, 60)

# Draw a rectangle and use rotate
#   (Figure 5-8 right)

def draw():
    translate(200, 200);
    rotate(radians(20));
    rect(50, 100, 100, 60)
    
# Draw a circle of circles
#   (Listing 5-5)

def draw():
    translate(width/2, height/2)
    for i in range(12):
        ellipse(200, 0, 50, 50)
        rotate(radians(360/12))
    
# Draw a circle of squares
#   (Listing 5-5, modified to use squares)

def draw():
    translate(width/2, height/2)
    for i in range(12):
        rect(200, 0, 50, 50)
        rotate(radians(360/12))
    
