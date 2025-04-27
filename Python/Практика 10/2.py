import numpy as np
import matplotlib.pyplot as plt

t =np.linspace(0,2*np.pi,1000)
ratios = [(3,2),(3,4),(5,4),(5,6)]

plt.figure(figsize = (12,8))

for i,(a,b) in enumerate(ratios,1):
    x=np.sin(a*t)
    y=np.sin(b*t)
    
    plt.subplot(2,2,i)
    plt.plot(x,y)
    plt.title(f'Соотношение {a}:{b}')


plt.tight_layout()
plt.show()