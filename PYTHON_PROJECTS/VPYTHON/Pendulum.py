from vpython import*
g=9.8
bob=sphere(pos=vector(5,2,0),radius=1.5,color=color.green)
pivot = vector(0,20,0)
roof = box(pos=pivot,size=vector(10,0.5,10),color=color.blue)
arm=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)
t=0
dt=0.01
l=mag(bob.pos-pivot)
cos=(l-bob.pos.y)/l
theta=acos(cos)
vel=0.0
while(t<100):
	rate(100)
	acc=-g/1*sin(theta)
	theta+=vel*dt
	vel+=acc*dt
	bob.pos=vector(l*sin(theta),l*(l-cos(theta)),0)
	arm.axis=bob.pos-arm.pos
	t+=dt
