import turtle
import time

tree=turtle.Turtle()
time.sleep(5)
tree.penup()
tree.goto(0,-100)
tree.pendown()
tree.screen.bgcolor("black")
tree.pensize(2)
tree.color("green")
tree.left(90)
tree.backward(100)
tree.speed(0)
tree.shape("turtle")

def trees(i):
    if i<10:
        return 
    else:
        tree.forward(i)
        tree.color("orange")
        tree.circle(2)
        tree.color("green")
        tree.circle(1)
        tree.color("brown")
        tree.left(30)
        trees(3*i/4)
        tree.right(60)
        trees(3*i/4)
        tree.left(30)
        tree.backward(i)

trees(100)
turtle.done()