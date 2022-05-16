import turtle
import time

turtle.bgcolor('black')
turtle.title("Turtles' Race")

window = turtle.Screen()

t1 = turtle.Turtle()
t1.shape("turtle")
t1.pensize(8)
t1.penup()
t1.goto(-200, 100)
t1.pendown()
t1.color('green')

t2 = turtle.Turtle()
t2.shape("turtle")
t2.pensize(7)
t2.penup()
t2.goto(-200, -100)
t2.pendown()
t2.color("pink")

meta = turtle.Turtle()
meta.color("white")
meta.pensize(4)
meta.penup()
meta.goto(240, 220)
meta.write("Finish Line", font=("Arial", 15, "bold"))

meta.penup()
meta.goto(300, 200)
meta.pendown()
meta.goto(300, -200)
meta.hideturtle()

odl = turtle.Turtle()
odl.color("light grey")
odl.penup()
odl.goto(-200, 200)
odl.hideturtle()

for x in range(3):
    odl.write(3-x, font=("Arial", 40, 'bold'))
    time.sleep(1)
    odl.clear()
odl.write("Start !!!", font=("Arial", 30, 'bold'))

def prosto1():
    t1.forward(20)  

def prosto2():
    t2.forward(20)

def bye():
    turtle.bye()



#def sprawdz1():
    
#    if t2.position(300, 100):
#        odl.clear()
#        odl.write("PLAYER 1 has won!!!", font=("Arial", 30, 'bold'))
#    pass
#def sprawdz2():
#    if t2.position(300, -100):
#        odl.clear()
#        odl.write("PLAYER 2 has won!!!", font="Arial", 30, 'bold')
#    pass

window.onkey(prosto1,"d")
window.onkey(prosto2,"Right")
window.onkey(bye,"Escape")


turtle.listen()
turtle.mainloop()


