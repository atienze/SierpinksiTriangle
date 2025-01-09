# Author: Elijah Atienza
# Date: 2/24/23
# Description: Sierpinski triangle drawing - A4

import turtle

def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255

    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t

def random_corner(canv_width, canv_height):
    """ This function will take the canvas width and length and find a random
        corner to choose returned in a tuple. """
    import random
    # use randrange to determine a random number 0 - 2 to determine what corner will be used 
    count = random.randrange(3)
    if count == 0:
        point = (0,0)
    if count == 1:
        point = (canv_width, 0)
    if count == 2:
        point = (canv_width / 2, canv_height)
    return point

def all_corners(canv_width, canv_height):
    """ This function will take the canvas width and length and calculate all
        corners of the triangle then give them back in a 3 valued tuple.
    """
    corner1 = (canv_width / 2, canv_height)
    corner2 = (0,0)
    corner3 = (canv_width, 0)
    corners = corner1, corner2, corner3
    return corners

def choose_color(midpoint, corners, canvas_width, canvas_height):
    """ This function takes the midpoint from the main function and all corners
        then calcualates the specific rgb values depending on the canvas_width
        and canvas_height
    """
    #declare variables 
    corner1,corner2,corner3 = corners
    max_dist = int(distance((0,0),corner1))
    side_dist = int(distance((0,0),corner3))
    
    #using the max distance that r can be from any point convert to red
    r = int((((max_dist - distance(midpoint,corner1)) / max_dist) * 255))
    #create an exception to make the gradiant correct across different triangles
    if canvas_width >= canvas_height:
        #create an exception to make sure rgb values will not be negative
        if distance(midpoint,corner2) <= side_dist:
            g = int((((side_dist - distance(midpoint,corner2)) / side_dist) * 255))
        else:
            g = int((((max_dist - distance(midpoint,corner2)) / max_dist) * 255))
        if distance(midpoint,corner3) <= side_dist:
            b = int((((side_dist - distance(midpoint,corner3)) / side_dist) * 255))
        else:
            b = int((((max_dist - distance(midpoint,corner3)) / max_dist) * 255))
    else:
        g = int((((max_dist - distance(midpoint,corner2)) / max_dist) * 255))
        b = int((((max_dist - distance(midpoint,corner3)) / max_dist) * 255))
    
    color = (r, g, b)
    return color
    
def distance(midpoint, corner):
    """ calculate the distance from the midpoint to the corner of choice"""
    x1,y1 = midpoint
    x2,y2 = corner
    distance = int((((x2-x1)**2) + ((y2-y1)**2))**0.5)
    return distance

def color_pixel(t, midpoint, color):
    """ Use the turtle from main, midpoint, and color given from choose
        color function to draw the color with the turtle.
    """
    x,y = midpoint
    t.goto(x,y)
    t.dot(1, color)
    
def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my


if __name__ == "__main__":
    import sys
    import turtle

    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])

    # Start by calling the turtle_setup function.
    t = turtle_setup(canv_width, canv_height)

    # Then implement the pseudocode below,
    # using the above turtle to color pixels:

    # Chaos game - pseudocode from the assignment handout:
    # p = a random corner of the triangle
    p = random_corner(canv_width, canv_height)
    # loop 10000 times:
    for i in range(10000):
        #     c = a random corner of the triangle
        c = random_corner(canv_width, canv_height)
        #     m = the midpoint between p and c
        m = midpoint(p, c)
        #     choose a color for m
        corners = all_corners(canv_width, canv_height)
        color = choose_color(m, corners, canv_width, canv_height)
        #     color the pixel at m
        color_pixel(t, m, color)
        p = m
        #turtle.update() tracking through looping variable
        if i % 1000 == 0 :
            turtle.update()
    turtle.update()
  