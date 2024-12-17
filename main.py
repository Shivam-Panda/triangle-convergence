from vpython import *
import math

a = 10
v0=10


b1 = sphere(pos=vector(0,0,0), radius=0.05, color=color.yellow, make_trail=True)
b2 = sphere(pos=vector(a,0,0), radius=0.05, color=color.green, make_trail=True)
b3 = sphere(pos=vector(a/2,a * sqrt(3) / 2,0), radius=0.05, color=color.blue, make_trail=True)

v1 = vertex(pos=b1.pos)
v2 = vertex(pos=b2.pos)
v3 = vertex(pos=b3.pos)

triangle(vs=[v1,v2,v3])

t = 0
dt = 0.001

while t <= 1:
  rate(100)

  b1.v = v0*(vector(b2.pos.x - b1.pos.x, b2.pos.y - b1.pos.y, 0).norm())
  b2.v = v0*(vector(b3.pos.x - b2.pos.x, b3.pos.y - b2.pos.y, 0).norm())
  b3.v = v0*(vector(b1.pos.x - b3.pos.x, b1.pos.y - b3.pos.y, 0).norm())

  b1.pos = b1.pos + b1.v*dt
  b2.pos = b2.pos + b2.v*dt
  b3.pos = b3.pos + b3.v*dt

  print(t)

  t = t + dt