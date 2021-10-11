from vpython import*
g1=graph(width=800, height=500, xtitle='time', ytitle='position')
xDots=gdots(color=color.green, graph=g1)

obj=sphere(pos=vector(0,0,0), radius=0.1, color=color.red, make_trial=True)

k=0
t=0
dt=0.1
x0=0
v0=1.0
a=0.009

while t<7:
    rate(10)
    #v0+=1
    k=0.5*a*t*t
    x=x0+v0*t+k
    obj.pos=vector(x,0,0)
    xDots.plot(t,x)
    t+=dt
