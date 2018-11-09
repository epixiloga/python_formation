import turtle

walle = turtle.Turtle()

x=int(input("combien de cote?  "))
y=360/x

walle.color("purple")
for i in range(x) :
    walle.forward(100)
    walle.left(y)







turtle.done()