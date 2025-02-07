import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,400)
turtle.title("Welxome to turtle window")

object=turtle.Turtle()

for i in range(4):
    object.forward(100)
    object.left(90)

turtle.done()