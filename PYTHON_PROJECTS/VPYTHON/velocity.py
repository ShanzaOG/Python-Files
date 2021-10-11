import numpy as np
import matplotlib.pyplot as plt

# Initialise time
t_1 = np.arange(1,20,1)/100
t_2 = np.arange(21,40,1)/100

# Compute v(t)
v_1 = np.where(t_1<0.2, 20, 0)
v_2 = np.where(t_2<0.2, 20, 0)

# Compute f(t)
f_1 = np.where(t_1<=0.2, 20*t_1, 4)
f_2 = np.where(t_2<=0.2, 20*t_2, 4)
#plot values into two graphs.
plt.subplot(2, 1, 1)
plt.plot(t_1, v_1)
plt.plot(t_2, v_2)
plt.title(' Problem 9')
plt.ylabel('Velocity')

plt.subplot(2, 1, 2)
plt.plot(t_1, f_1)
plt.plot(t_2, f_2)
plt.xlabel('time (t)')
plt.ylabel('Velocity');
