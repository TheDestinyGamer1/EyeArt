from turtle import *
from random import *
from sympy import *
from time import *

startTime = time()

screensizeScalar = 0.92
defaultWidth = 1920
defaultHeight = 1080
intSpeed = 0
iterations = 1500
mySeed = 328
seed(mySeed)
randomAngleScalar = 0.1
alpha = 0.55
beta = 0.55
beforeDistScalar = 0.5
maxAfterDist = 5
lineSize = 1
irisLineColor = (1.0, 0.65, 0.0)
irisFillColor = (1.0, 0.15, 0.15)
pupilColor = (0.1, 0.1, 0.1)


realWidth = defaultWidth * screensizeScalar
realHeight = defaultHeight * screensizeScalar

screensize(realWidth, realHeight)
speed(intSpeed)
radians()
pensize(lineSize)

color(irisFillColor, irisFillColor)
pensize(1)
begin_fill()
penup()
goto(0, -realHeight/2)
pendown()
circle(realHeight/2)
end_fill()

color(irisLineColor)
pensize(lineSize)

x, y = symbols("x y", real=true)
innerCircle = x**2 + y**2 - (realHeight/8)**2
outerCircle = x**2 + y**2 - (realHeight/2)**2


for i in range(iterations):
    if i % 100 == 0:
        print("%d iterations completed in %f seconds" % (i, time() - startTime))
    penup()
    setx(betavariate(alpha, beta) * realHeight - realHeight / 2)
    yVals = solve(outerCircle.subs(x, xcor()), y)
    if len(yVals) > 1:
        sety(yVals[randint(0, 1)])
    else:
        sety(yVals[0])
    setheading(atan(ycor()/xcor()) + random() * randomAngleScalar)
    if xcor() >= 0:
        setheading(heading()+pi)
    equ = tan(heading()) * (x - xcor()) - (y - ycor())
    perpEpu = -cot(heading()) * (x - xcor()) - (y - ycor())
    intersections = solve([equ, innerCircle], set=true)
    pendown()

    if len(intersections[1]) < 2:
        setheading(heading() + pi)
    for j in intersections:
        if type(j) == set:
            if len(j) == 2:
                coords = list(j)
                if heading() > pi:
                    if perpEpu.subs([(x, coords[0][0]), (y, coords[0][1])]) > 0:
                        if distance(coords[0][0], coords[0][1]) < distance(coords[1][0], coords[1][1]):
                            beforeDist = randint(0, int(distance(coords[0][0], coords[0][1])/2))
                            afterDist = randint(0, maxAfterDist)
                            dist = distance(coords[0][0], coords[0][1]) - beforeDist - afterDist
                            penup()
                            fd(beforeDist)
                            pendown()
                            fd(dist)
                            penup()
                            fd(afterDist)
                            pendown()
                        else:
                            beforeDist = randint(0, int(distance(coords[1][0], coords[1][1]) / 2))
                            afterDist = randint(0, maxAfterDist)
                            dist = distance(coords[1][0], coords[1][1]) - beforeDist - afterDist
                            penup()
                            fd(beforeDist)
                            pendown()
                            fd(dist)
                            penup()
                            fd(afterDist)
                            pendown()
                else:
                    if perpEpu.subs([(x, coords[0][0]), (y, coords[0][1])]) < 0:
                        if distance(coords[0][0], coords[0][1]) < distance(coords[1][0], coords[1][1]):
                            beforeDist = randint(0, int(distance(coords[0][0], coords[0][1]) / 2))
                            afterDist = randint(0, maxAfterDist)
                            dist = distance(coords[0][0], coords[0][1]) - beforeDist - afterDist
                            penup()
                            fd(beforeDist)
                            pendown()
                            fd(dist)
                            penup()
                            fd(afterDist)
                            pendown()
                        else:
                            beforeDist = randint(0, int(distance(coords[0][0], coords[0][1]) / 2))
                            afterDist = randint(0, maxAfterDist)
                            dist = distance(coords[1][0], coords[1][1]) - beforeDist - afterDist
                            penup()
                            fd(beforeDist)
                            pendown()
                            fd(dist)
                            penup()
                            fd(afterDist)
                            pendown()

color(pupilColor, pupilColor)
begin_fill()
penup()
goto(0, -realHeight/8)
setheading(0)
pendown()
circle(realHeight/8)
end_fill()


penup()
goto(0, 0)

print("Completed %d iterations in %f seconds" % (iterations, time()-startTime))
done()