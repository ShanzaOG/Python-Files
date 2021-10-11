from pylab import *
from scipy.integrate import odeint


N = 1000    # number of steps to take

y = np.zeros([4])      # we have FOUR parameters

L_o = 2.0       # unstretched spring length
L = 1.0         # inital stretch of spring
v_o = 0.0       # initial velocity
theta_o = 0.2  # radians
omega_o = 0.2   # initial angular velocity

y[0] = L
y[1] = v_o
y[2] = theta_o
y[3] = omega_o

time = np.linspace(0, 25, N)

k = 3.5         # spring constant, in N/m
m = 0.2         # mass, in kg
gravity = 9.8   # g, in m/s^2

def spring_pendulum(y, time):
    """
    This defines the set of differential equations we are solving.
    """
    g0 = y[1]
    g1 = (L_o+y[0])*y[3]**2 - k/m*y[0] + gravity*np.cos(y[2])
    g2 = y[3]
    g3 = -(gravity*np.sin(y[2]) + 2.*y[1]*y[3])/(L_o+y[0])
    
    return np.array([g0, g1, g2, g3])

# calculations
answer = odeint(spring_pendulum, y, time)

# graph the results
xdata = (L_o + answer[:,0])*np.sin(answer[:,2])
ydata = -(L_o + answer[:,0])*np.cos(answer[:,2])

plot(xdata, ydata)
xlabel("Horizontal position")
ylabel("Vertical position")
savefig('pendulum_fig2.jpg')
show()
