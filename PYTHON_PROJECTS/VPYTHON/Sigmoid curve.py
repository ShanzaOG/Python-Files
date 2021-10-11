"""
import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(-20,20,100)
z=1/(1+np.exp(-x))
plt.plot(x,z)

plt.show()"""


from vpython import*
import math
g1=graph(width=800, height=500, xtitle='time', ytitle='velocity')
xDots=gdots(color=color.green, graph=g1)

obj=sphere(pos=vector(0,0,0), radius=0.1, color=color.red, make_trial=False)

k=0
t=0
dt=0.01
x0=0
v0=1.0
a=0.009

while t<5:
    rate(20)
    v0+=0.1
    k=0.1*a*t*t
    x=x0+v0*t+k
    z=1/(1+exp(-x))
    obj.pos=vector(z,0,0)
    xDots.plot(t,z)
    t+=dt
 
        
