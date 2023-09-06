import io
from turtle import *
from random import triangular, betavariate, seed, random
from math import pi, sin, cos
from time import time
from os import remove
from PIL import Image

startTime = time()

screensizeScalar = 1
defaultHeight = 1080
intSpeed = 0
myIterations = 2000
mySeed = 328
seed(mySeed)
randomAngleScalar = 0.125
marginSizeScalar = 0.025
alpha = 1
beta = 0.55
maxBeforeDist = 10 * screensizeScalar
lineSize = 1
irisMinColor = (0.1, 0.6, 0.1)
irisMaxColor = (0.2, 0.7, 0.2)
irisFillColor = (0.9, 0.82, 0.3)
pupilColor = (0.05, 0.05, 0.05)
fileName = "eye"
fileType = "png"

try:
    remove(fileName + "." + fileType)
except FileNotFoundError:
    print("no file to remove")

realHeight = int(defaultHeight * screensizeScalar * (1 - (2 * marginSizeScalar)))
margin = int(defaultHeight * screensizeScalar * marginSizeScalar)
iterations = int(myIterations * screensizeScalar)
realMaxBeforeDist = int(maxBeforeDist * screensizeScalar)

if (realHeight + 2*margin)**2 >= 178956970:
    exit(print("Image File Will Be Too Large"))
screensize(realHeight, realHeight)
speed(intSpeed)
radians()
pensize(lineSize)

ht()

color(irisFillColor, irisFillColor)
pensize(1)
begin_fill()
penup()
goto(0, -realHeight/2)
pendown()
circle(realHeight/2)
end_fill()

pensize(lineSize)

tracer(iterations*8)

for i in range(iterations):
    if i % 1000 == 0:
        if i == 0:
            print("Initialized in %.6f seconds" % (time()-startTime))
        else:
            print("%d iterations done in %.6f seconds" % (i, time()-startTime))
    color(tuple(triangular(irisMinColor[i], irisMaxColor[i]) for i in range(len(irisMinColor))))
    penup()
    setheading(2*pi*(i/iterations))
    goto(cos(heading())*realHeight/8, sin(heading())*realHeight/8)
    setheading(heading() + random() * randomAngleScalar)
    fd(betavariate(beta, alpha)*maxBeforeDist)
    pendown()
    fd((realHeight/2 - realHeight/8) * betavariate(alpha, beta) - maxBeforeDist)

penup()
color(pupilColor, pupilColor)
goto(0, -realHeight/8)
begin_fill()
setheading(0)
pendown()
circle(realHeight/8)
end_fill()

ht()

print("Completed %d iterations in %f seconds" % (iterations, time()-startTime))
update()
#Completed 2000 iterations in 0.788077 seconds
startExportTime = time()
ps = getscreen().getcanvas().postscript(height=realHeight+2*margin, width=realHeight+2*margin, x=-realHeight/2 - margin, y=-realHeight/2 - margin, pageheight=realHeight+2*margin, pagewidth=realHeight+2*margin)
print(screensize())
tempImage = Image.open(io.BytesIO(ps.encode("utf-8")))
tempImage.save(fileName + "." + fileType, fileType)
print("saved as %s.%s in %.3f seconds" % (fileName, fileType, (time() - startExportTime)))
done()