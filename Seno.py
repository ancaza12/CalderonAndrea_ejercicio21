import numpy as np
import matplotlib.pylab as plt
x= np.linspace(-2*np.pi, 2*np.pi,20)
y= np.cos(x)
print (y)

plt.figure()
plt.plot(x,y)
plt.savefig('Grafcos.png')
