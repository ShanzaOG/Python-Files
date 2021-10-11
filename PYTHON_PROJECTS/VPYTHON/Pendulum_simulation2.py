from vpython import*
#display(width=360, height=640,centre=vector(0,12,0),backgroung=color.black)
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.blue)
g=9.8
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.green)
string=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)
t=0
dt=0.01
l=mag(bob.pos-pivot)
cs=(l-bob.pos.y)/l
theta=acos(cs)
vel=0.0
while (t<1000):
    rate(100)
    acc=g/l*sin(theta)
    theta+=vel*dt
    vel+=acc*dt
    bob.pos=vector(l*sin(theta),l*(l-cos(theta)),0)
    string.axis=bob.pos-string.pos
    t+=dt
 
