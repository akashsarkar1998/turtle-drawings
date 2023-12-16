# turtle-drawings
Made some structures with turtle library.
#### ```Fibonacci series```
```python
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
ak= turtle.Turtle()
ak.color("blue")
ak.shape("turtle")
distance=5
ak.up()
for i in range(30): #Starts with 5, and go by 2
    ak.stamp()  #Leaves an expression on the canvas
    ak.forward(distance)
    ak.right(20)
    distance= distance+4
window.exitonclick()
```
```python
import turtle
n= int(input(': '))
def fib(n):
    a, b= 0,1
    for _ in range(n):
        for _ in range(4):
            turtle.forward(a)
            turtle.left(90)
            
        x,y = turtle.pos()
        turtle.penup()
        turtle.goto(x+a,y)
        turtle.pendown()
        a,b = b, a+b
screen= turtle.Screen()
t=turtle.Turtle()
t.speed(0)
fib(n)
screen.exitonclick()
```

### ```I don't know what is this, But it is something!!```
```python
mport turtle
wn = turtle.Screen()
wn.bgcolor("black")
bob = turtle.Turtle()
bob.color("white")
bob.speed(100)
for i in range(700):
    bob.forward(1.5*i)
    bob.right(90.5)
wn.exitonclick()
```
