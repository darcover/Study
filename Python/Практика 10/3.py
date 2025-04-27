from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

fig=plt.figure()
ax=fig.add_subplot(111)
line,=ax.plot([],[],lw=2)

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

t=np.linspace(0,2*np.pi,400)

def init():

    line.set_data([],[])
    return line,

def update(frame):

    a = frame/100
    b = 1
    x =np.sin(a*t+0)
    y=np.sin(b*t)
    line.set_data(x,y)
    return line,

ani=FuncAnimation(fig,update,frames=range(0,101), init_func=init, blit=True)

plt.show()


