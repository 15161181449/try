import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def logistic(x,t):
    r = 0.3
    max_x = 500
    return np.array(r*x*(1-(x/max_x))+0*t)
time = np.arange(0,30,1)
x = odeint(logistic,100,time)
plt.xlabel('time')
plt.ylabel('number(W)')
plt.title('car number')
plt.plot(x)
plt.legend()
plt.show()