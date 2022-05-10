from scipy.integrate import quadrature
import numpy as np


def f(t):
    return ((1-np.exp(-2*9.8*t/54))/(1+np.exp(-2*9.8*t/54)))

X = []
T = []
x = 1400
dt = 0.001
t = 29.70
h = 1400
while (x>0):
    t+=dt
    res, err = quadrature(f,0,t)

    x = h-54*res

    T.append(float(t))
    X.append(float(x))
print(x,t)

import matplotlib.pyplot as plt



# Create the x vs t plot
plt.xlabel("$t$ (m)")
plt.ylabel("$x$ (m)")
plt.plot(T, X)
plt.show()

np.savetxt("Person_falling.txt", np.column_stack((T,X)))