# import turtle
# wn = turtle.Screen()
# clr= str(input("Please enter which color of the screen you want: "))
# wn.bgcolor(clr)
# aks = turtle.Turtle()
# t_clr = str(input("Which color of turtle you want: "))
# aks.color(t_clr)
# aks.pensize(15)
# aks.forward(200)
# aks.left(90)
# aks.forward(50)
# aks.left(90)
# aks.forward(200)
# aks.left(90)
# aks.forward(50)
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# alex = turtle.Turtle()
# alex.forward(150)
# alex.left(90)
# alex.forward(75)

#************
# import turtle
# wn = turtle.Screen()             # Set up the window and its attributes
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()           # create tess and set his pen width
# tess.pensize(5)

# alex = turtle.Turtle()           # create alex
# alex.color("hotpink")            # set his color

# tess.forward(80)                 # Let tess draw an equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)                   # complete the triangle

# tess.right(180)                  # turn tess around
# tess.forward(80)                 # move her away from the origin so we can see alex

# alex.forward(50)                 # make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

# wn.exitonclick()

#*******
# import turtle
# window = turtle.Screen()
# window.bgcolor("lightgreen")

# ak= turtle.Turtle()
# ak.color("black")


# distance= 50
# # angle=90
# for i in range(10):
#     ak.forward(distance)
#     ak.right(90)
#     distance= distance+10
#     # angle= angle-3
# window.exitonclick()

#*****
# import turtle
# window = turtle.Screen()
# window.bgcolor("lightgreen")
# ak= turtle.Turtle()
# ak.color("blue")
# ak.shape("turtle")
# distance=5
# ak.up()
# for i in range(30): #Starts with 5, and go by 2
#     ak.stamp()  #Leaves an expression on the canvas
#     ak.forward(distance)
#     ak.right(20)
#     distance= distance+4
# window.exitonclick()

#*********
# import turtle
# import math
# wn = turtle.Screen()
# bob = turtle.Turtle()
# bob.right(90)
# bob.forward(50)
# bob.left(90)
# bob.forward(50)
# bob.left(90)
# bob.forward(50)
# bob.left(90)
# bob.forward(50)
# dist= math.sqrt(50*50/2)
# bob.right(135)
# bob.forward(dist)
# bob.right(90)
# bob.forward(dist)
# wn.exitonclick()

# ****Fibonacci series turtle
# import turtle
# n= int(input(': '))
# def fib(n):
#     a, b= 0,1
#     for _ in range(n):
#         for _ in range(4):
#             turtle.forward(a)
#             turtle.left(90)
            
#         x,y = turtle.pos()
#         turtle.penup()
#         turtle.goto(x+a,y)
#         turtle.pendown()
#         a,b = b, a+b
# screen= turtle.Screen()
# t=turtle.Turtle()
# t.speed(0)
# fib(n)
# screen.exitonclick() 

import turtle
wn = turtle.Screen()
wn.bgcolor("black")
bob = turtle.Turtle()
bob.color("white")
bob.speed(100)
for i in range(700):
    bob.forward(1.5*i)
    bob.right(90.5)
wn.exitonclick()