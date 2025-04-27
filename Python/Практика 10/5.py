import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x =np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X,Y =np.meshgrid(x,y)

Z =(X**2+Y**2)/2  

fig= plt.figure(figsize=(12,6))
ax1=fig.add_subplot(121,projection='3d')
ax1.plot_surface(X,Y,Z)

ax1.set_title('MSE')

ax2 =fig.add_subplot(122,projection='3d')

ax2.plot_surface(X,Y,np.log(Z+1))  
ax2.set_title('MSE (логарифмический масштаб)')
plt.show()