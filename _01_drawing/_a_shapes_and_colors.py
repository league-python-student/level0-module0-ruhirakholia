import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    ruhi = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    ruhi.shape('turtle')
    # Set your turtle's speed using .speed(2)
    ruhi.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    ruhi.color('green')
    ruhi.pencolor('blue')
    # Move your turtle forward using .forward(100)
    for i in range(4):
        ruhi.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        ruhi.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.

    # TEST    Did your turtle draw a square?
        
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    ruhi.goto(1,1)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    ruhi.begin_fill()
    ruhi.circle(radius=150, steps=30)
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle

    # and .end_fill() below
    ruhi.end_fill()
    # Draw 3 more shapes with different fill colors!
    ruhi.circle(radius=20, steps=3)
    ruhi.circle(radius=130, steps=8)
    ruhi.circle(radius=50, steps=6)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
