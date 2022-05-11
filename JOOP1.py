from scipy.integrate import quadrature
import numpy as np

# v_t is the terminal velocity in meters per second

v_t = 54
def f(t,v_t):
    return ((1-np.exp(-2*9.8*t/v_t))/(1+np.exp(-2*9.8*t/v_t)))

X = []
T = []
x = 4000
dt = 0.001
t = 0
h = 4000
#3 while loops needed: 1 for above 1200, the transition for velocity, and the 1 for above the ground (0). 
while (x>1200):
    t+=dt
    res, err = quadrature(f,0,t, args = v_t)

    x = h-v_t*res
    X.append(float(x))
    T.append(float(t))
#print(x,t)
print(float(t1))
dt = 6.5E-7 #got from estimation this works for about 4 decimals
t1 = t
i = 0
a = -15.467 #from 54/3-7.6/3


while(v_t > 7.6):
    t = t1 + i*dt # A different way to do the above method.
    c = i*dt
    v_t = a*c + 54
    i += 1
    res, err = quadrature(f, t, t+dt, args=v_t)
    x = x - res
    X.append(float(x))
    T.append(float(t))
print(float(t2))
#back to the same code just different terminal velocity.
dt = 0.001
i = 0
v_t = 7.6
t2 = t 
x2 = x


while (x>0):
    t = t2 + i*dt
    i += 1
    res, err = quadrature(f, t2, t, args=v_t)
    x = x2 - res
    X.append(float(x))
    T.append(float(t))

t3 = t
print(float(t3))



import matplotlib.pyplot as plt



# Create the x vs t plot
plt.xlabel("$t$ (s)")
plt.ylabel("$x$ (m)")
plt.plot(T, X)
plt.show()

np.savetxt("Person_falling1.txt", np.column_stack((T,X)))