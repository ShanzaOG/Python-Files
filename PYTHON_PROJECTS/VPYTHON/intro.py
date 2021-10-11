Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from vpython import*
>>> box()
<vpython.vpython.box object at 0x0000013D603CE5E0>
>>> x=sphere(radius=1.2)
>>> y= sphere()
>>> x= sphere(radius=5, color=color.green)
>>> clear()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> exit()
>>> x= box()
>>> 
================================ RESTART: Shell ================================
>>> from vpython import*
>>> cylinder(axis=vector(0,1.5,0))
<vpython.vpython.cylinder object at 0x000001712E463640>
>>> cylinder(axis=vector(0,-5,5))
<vpython.vpython.cylinder object at 0x000001712E4B6AC0>
>>> cylinder(axis=vector(0,5,-5))
<vpython.vpython.cylinder object at 0x000001712DB819D0>
>>> cylinder(axis=vector(-5,0,5))
<vpython.vpython.cylinder object at 0x000001712DB4B3D0>
>>> 
================================ RESTART: Shell ================================
>>> x=box(-5,5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=box(-5,5)
NameError: name 'box' is not defined
>>> from vpython import*
x=b
>>> x=box(-5,5)
Exception ignored in: <function standardAttributes.__del__ at 0x00000201DE4E9940>
Traceback (most recent call last):
  File "C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\site-packages\vpython\vpython.py", line 1092, in __del__
    super(standardAttributes, self).__del__()
  File "C:\Users\hp\AppData\Local\Programs\Python\Python38\lib\site-packages\vpython\vpython.py", line 317, in __del__
    cmd = {"cmd": "delete", "idx": self.idx}
AttributeError: 'box' object has no attribute 'idx'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x=box(-5,5)
TypeError: __init__() takes 1 positional argument but 3 were given
>>> x=box()
>>> 
================================ RESTART: Shell ================================
>>> 