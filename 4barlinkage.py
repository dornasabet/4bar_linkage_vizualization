from vpython import *
import math
sphere1 = sphere(pos=vector(0, 0, 0), radius=1, color=color.red)
sphere2 = sphere(pos=vector(3, 4, 0), radius=1, color=color.white)
sphere3 = sphere(pos=vector(5, 12, 0),redius=1,color=color.white)
sphere4 = sphere(pos=vector(10, 0, 0),redius=3,color=color.red)


shaft12 = arrow(pos=sphere1.pos, axis=sphere2.pos - sphere1.pos, color=color.white,shaftwidth =0.5, headwidth=1, headlength=0.5)
shaft23 = arrow(pos=sphere2.pos, axis=sphere3.pos - sphere2.pos, color=color.white,shaftwidth =0.5, headwidth=1, headlength=0.5)
shaft34 = arrow(pos=sphere3.pos, axis=sphere4.pos - sphere3.pos, color=color.white, shaftwidth =0.5,headwidth=1, headlength=0.5)
shaft41 = arrow(pos=sphere4.pos, axis=sphere1.pos - sphere4.pos, color=color.white,shaftwidth =0.5, headwidth=1, headlength=0.5)
angle=0

a = ((5-3)**2+(12-4)**2)
g = 10
b = 0.3
scene.range=50
while True:
    rate(g)

    k = keysdown() # a list of keys that are down

    if 'down' in k: b -= 0.1
    if 'up' in k: b += 0.1

    e = (5 ** 2 + 10 ** 2 - 2 * 5 * 10 * math.cos(angle))
    E= (math.sqrt(5 ** 2 + 10 ** 2 - 2 * 10* 5 * math.cos(angle)))

    alfa = math.asin(math.sin(angle) * 5 / E)
    beta = acos(-(a -e - 13*13) / (2 * E * 13))
    x1= (math.cos(angle) * 5)
    y1= (math.sin(angle) * 5)
    x2= (10-13*math.cos(alfa+beta))
    y2= (13*math.sin(alfa+beta))
    angle += b

    sphere2.pos = vector(x1, y1, 0)
    shaft12.axis = sphere2.pos - sphere1.pos
    sphere3.pos = vector(x2, y2, 0)
    shaft23.pos=sphere2.pos
    shaft34.pos=sphere3.pos
    shaft23.axis=sphere3.pos - sphere2.pos
    shaft34.axis=sphere4.pos - sphere3.pos
