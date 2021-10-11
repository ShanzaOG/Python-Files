Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from vpython import*
>>> g=9.8
>>> bob=sphere(pos=vector(0,0,0),radius(1.5),color=color.green)
SyntaxError: positional argument follows keyword argument
>>>  bob=sphere(pos=vector(0,0,0),radius=1.5,color=color.green)
 
SyntaxError: unexpected indent
>>> bob=sphere(pos=vector(0,0,0),radius=1.5,color=color.green)
>>> bob=sphere(pos=vector(5,0,0),radius=0.5,color=color.green)
>>> 
================================ RESTART: Shell ================================
>>> bob=sphere(pos=vector(5,2,0),radius=1.5,color=color.green)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    bob=sphere(pos=vector(5,2,0),radius=1.5,color=color.green)
NameError: name 'sphere' is not defined
>>> from vpython import*
>>> bob=sphere(pos=vector(5,2,0),radius=1.5,color=color.green)
>>> 
================================ RESTART: Shell ================================
>>> from vpython import*
>>> bob=sphere(pos=vector(5,2,0),radius=1.5,color=color.green)
>>> pivot = vector(0,20,0)
>>> roof = box(pos=pivot,size=vector(10,0.5,10),color=color.blue)
>>> arm=cylinder(pos=pivot,axis=bob,pos-pivot,radius=0.1,color=color.red)
SyntaxError: positional argument follows keyword argument
>>> arm=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)
>>> t=0
>>> dt=0.01
>>> l=mag(bob.pos-pivot)
>>> cos=(l-bob.pos.y)/l
>>> theta=acos(cs)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    theta=acos(cs)
NameError: name 'cs' is not defined
>>> theta=acos(cos)
>>> 