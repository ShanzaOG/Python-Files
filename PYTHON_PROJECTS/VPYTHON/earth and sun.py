from vpython import*
sun=sphere(pos=vector(0,0,0), radius=1, color=color.yellow)
earth=sphere(pos=vector(2,1,0), radius=0.3, color=color.blue)

t=0
dt=0.5
theta=0
y0=2
v0=0
omega=2*pi/365


while True:
    rate(100)
    x=10*cos(theta)
    y=10*sin(theta)
    earth.pos=vector(x,y,0)
    theta=omega*t
    t+=dt
    
