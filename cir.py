import turtle
def am(a):
	for i in range(1,5):
		a.forward(100)
		a.right(90)
def _draw():
	window=turtle.Screen()
	window.bgcolor("grey")
 	a=turtle.Turtle()
	a.color("green")
	window.title("Demo")
	a.shape("circle")
	a.speed(50)
	for i in range(1,40):
		am(a)
	 	a.right(10)
	window.exitonclick()

_draw()

