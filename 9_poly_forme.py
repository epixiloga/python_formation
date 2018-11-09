import turtle

walle = turtle.Turtle()

x= int(input("combien de poly? "))
y=int(input("taille "))
a=int(input("combien de cote?  "))
b=360/a


    
for i in range(x):

    for j in range(a) :
        walle.forward(y)
        walle.left(b)
    
    
    y=y+30
        








turtle.done()