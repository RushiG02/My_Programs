import turtle
from random import randint
from colorsys import hsv_to_rgb

t=turtle.Turtle()

'''
t=turtle.Turtle()
t.speed(100)

for i in range(74):
    t.forward(150)
    t.right(130)
    
    t.forward(5)
    t.right(15)
    t.forward(10)
    t.left(2)
'''

width=5
(w,h)=turtle.screensize()
t.speed('fastest')
turtle.colormode(1.0)
turtle.bgcolor('black')
hue=0.0

for i in range(2000):
    t.setheading(randint(0,359))
    t.color(hsv_to_rgb(hue,1.0,1.0))
    hue+=0.001
    t.forward(30)
    (x,y)=t.pos()
    if abs(x)>w or abs(y)>h:
        t.backward(100)
        

turtle.done()