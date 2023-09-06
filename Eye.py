from turtle import *
from random import *
from sympy import *

screensizeScalar = 0.92
defaultWidth = 1920
defaultHeight = 1080
intSpeed = 0
iterations = 1000
mySeed = 328
seed(mySeed)

realWidth = defaultWidth * screensizeScalar
realHeight = defaultHeight * screensizeScalar

screensize(realWidth, realHeight)
speed(intSpeed)
radians()


#penup()
#goto(0, -realHeight/8)
#pendown()
#circle(realHeight/8)
#penup()
#goto(0, -realHeight/2)
#pendown()
#circle(realHeight/2)


x, y = symbols("x y", real=true)
innerCircle = x**2 + y**2 - (realHeight/8)**2
outerCircle = x**2 + y**2 - (realHeight/2)**2


for i in range(iterations):
    penup()
    goto(random() * realHeight - realHeight / 2, random() * realHeight - realHeight / 2)
    setheading(random()*2*pi)
    while heading() == 0 or heading() == pi/2 or heading() == pi or heading() == 3*pi/2 or heading() == 2*pi:
        setheading(random()*2*pi)
    while innerCircle.subs([(x, xcor()), (y, ycor())]) < 0 or outerCircle.subs([(x, xcor()), (y, ycor())]) > 0:
        goto(random()*realHeight - realHeight/2, random()*realWidth - realWidth/2)
    equ = tan(heading()) * (x - xcor()) - (y - ycor())
    perpEpu = -cot(heading()) * (x - xcor()) - (y - ycor())
    intersections = solve([equ, outerCircle], set=true)
    intersections2 = solve([equ, innerCircle], set=true)
    pendown()

    if len(intersections2[1]) > 0:
        for j in intersections2:
            if type(j) == set:
                if len(j) == 2:
                    coords = list(j)
                    if heading() > pi:
                        if perpEpu.subs([(x, coords[0][0]), (y, coords[0][1])]) > 0:
                            if distance(coords[0][0], coords[0][1]) < distance(coords[1][0], coords[1][1]):
                                fd(distance(coords[0][0], coords[0][1]))
                            else:
                                fd(distance(coords[1][0], coords[1][1]))
                    else:
                        if perpEpu.subs([(x, coords[0][0]), (y, coords[0][1])]) < 0:
                            if distance(coords[0][0], coords[0][1]) < distance(coords[1][0], coords[1][1]):
                                fd(distance(coords[0][0], coords[0][1]))
                            else:
                                fd(distance(coords[1][0], coords[1][1]))

    else:
        for j in intersections:
            if type(j) == set:
                if len(j) == 2:
                    coords = list(j)
                    if heading() > pi:
                        if perpEpu.subs([(x, coords[0][0]), (y, coords[0][1])]) > 0:
                            fd(distance(coords[0][0], coords[0][1]))
                        else:
                            fd(distance(coords[1][0], coords[1][1]))
                    else:
                        if perpEpu.subs([(x, coords[0][0]), (y, coords[0][1])]) < 0:
                            fd(distance(coords[0][0], coords[0][1]))
                        else:
                            fd(distance(coords[1][0], coords[1][1]))


done()