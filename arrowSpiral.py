import turtle
screen = turtle.Screen()
screen.bgcolor('black')
nima = turtle.Turtle()
nima.pensize(2)
nima.pencolor('yellow')
nima.shape('classic')

distance = 8
nima.up()  #Pull the pen up -- no drawing when moving.
nima.speed('normal')
for _ in range(100):
    nima.stamp() # to stamp the shape
    nima.forward(distance)
    nima.right(30)
    distance += 2

screen.exitonclick()