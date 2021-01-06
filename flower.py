import turtle
screen = turtle.Screen()
screen.bgcolor('lightblue')
nima = turtle.Turtle()
nima.shape('circle')
nima.shapesize(4, 2)
nima.color("hotpink")
# nima.tilt(50)

distance = 6
nima.up()  #Pull the pen up -- no drawing when moving.
# nima.speed('fast')

for _ in range(40):
    nima.stamp() # to stamp the shape
    nima.forward(distance)
    nima.right(30)
    distance += 1

screen.exitonclick()