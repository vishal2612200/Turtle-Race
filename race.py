from turtle import *
from random import randint

speed(8)
penup()
goto(-160,140)
for step in range(15):
    write(step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

third = Turtle()
third.color('green')
third.shape('turtle')

third.penup()
third.goto(-160,40)
third.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    third.forward(randint(1,5))

