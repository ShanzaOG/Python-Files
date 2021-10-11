from vpython import *
import time
Breadboard = box(length=6, height=.2, width=2,opacity=.5)
Xarrow=arrow(axis=vector(1,0,0),length=2, shaftwidth=.1,color=color.red)    
Yarrow=arrow(axis=vector(0,1,0),length=2, shaftwidth=.1,color=color.green)
Zarrow=arrow(axis=vector(0,0,1),length=2, shaftwidth=.1,color=color.blue)
arduino=box(length=1.75,width=.6,height=.1,pos=vector(-2,.15,0),color=color.yellow)
MPU = box(length=.75,width=.65,height=.1,pos=vector(0,.15,0),color=color.orange)
