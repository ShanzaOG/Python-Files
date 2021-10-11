from vpython import*
from time import*
import numpy as np
import math
scene.range=5
toRad=2*np.pi/360
toDeg=1/toRad
scene.forward=vector(-1,-1,-1)

scene.width=600
scene.height=600


Breadboard = box(length=6, height=.2, width=2,opacity=.5)
arduino=box(length=1.75,width=.6,height=.1,pos=vector(-2,.15,0),color=color.yellow)
MPU = box(length=.75,width=.65,height=.1,pos=vector(0,.15,0),color=color.orange)

Xarrow=arrow(axis=vector(1,0,0),length=2, shaftwidth=.1,color=color.red)    
Yarrow=arrow(axis=vector(0,1,0),length=2, shaftwidth=.1,color=color.green)
Zarrow=arrow(axis=vector(0,0,1),length=2, shaftwidth=.1,color=color.blue)

frontarrow=arrow(axis=vector(1,0,0),length=4, shaftwidth=.1,color=color.purple)
Uparrow=arrow(axis=vector(0,1,0),length=1, shaftwidth=.1,color=color.magenta)    
Sidearrow=arrow(axis=vector(0,0,1),length=2, shaftwidth=.1,color=color.orange)
myObj=compound([Breadboard,arduino,MPU])

while True:
	pitch=45*toRad
	for yaw in np.arange(0,2*np.pi,.01):
		rate(50)
		k=vector(cos(yaw)*cos(pitch),sin(pitch),sin(yaw)*cos(pitch))
		y=vector(0,1,0)
		s=cross(k,y)
		v=cross(s,k)

		frontarrow.axis=k
		Sidearrow.axis=s
		Uparrow.axis=v
		myObj.axis=k
		myObj.up=v

		Sidearrow.length=2
		frontarrow.length=4
		Uparrow.length=1
		
