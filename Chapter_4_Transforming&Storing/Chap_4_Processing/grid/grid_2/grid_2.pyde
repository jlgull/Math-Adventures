# Set the range of the x-values
xmin = -10
xmax = 10

# Set the range of the y-values
ymin = -10
ymax = 10

# Calculate the range for both x & y
rangex = xmax - xmin
rangey = ymax - ymin

# Begin the setup of the sketch

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
    
def draw():
    global xscl, yscl
    background(255) # white
    translate(width/2,height/2)
    grid(xscl, yscl) # draw the grid
    graphFunction()


def f(x):
    return 2*x**2 + 7*x - 15

    
def graphFunction():
    x = xmin
    while x <= xmax:
        # Draw a dot at each x value
        # Test with a circle
        stroke(255,0,0)
        line(x*xscl, f(x)*yscl, (x + 0.1)*xscl, f(x + 0.1)*yscl)
        x += 0.1   
    
    
def grid(xscl, yscl):
    # Draw a grid for graphing
    # cyan lines
    strokeWeight(1)
    stroke(0,255,255) # cyan lines
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax + 1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) # Black Axes
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)
    
