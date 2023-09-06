from turtle import *
from random import *
from sympy import *
from time import *

startTime = time()

screensizeScalar = 0.92
defaultWidth = 1920
defaultHeight = 1080
intSpeed = 0
iterations = 2000
mySeed = 328
seed(mySeed)
randomAngleScalar = 0.1
alpha = 1.0
beta = 0.5
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

for i in range(iterations):
    penup()
    setheading(2*pi*(i/iterations))
    goto(cos(heading())*realHeight/8, sin(heading())*realHeight/8)
    setheading(heading() + random() * randomAngleScalar)
    pendown()
    fd((realHeight/2 - realHeight/8) * betavariate(alpha, beta))


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
#Completed 2000 iterations in 268.220437 seconds
done()