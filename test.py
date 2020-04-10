import turtle
def _draw():
	window=turtle.Screen()
	window.bgcolor("grey")
 	a=turtle.Turtle()
	i=0
	j=0
	x=['grey','black','blue','green','red','white','yellow','white']
	while(i<7):
	 a.circle(20+j)
	 j=j+40
	 i=i+1
	# a.fill(x[i])
	 a.color(x[i])
_draw()

input()
