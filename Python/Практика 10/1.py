import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre


x = np.linspace(-1,1,1000)


degrees = range(1, 8)


fig, ax = plt.subplots()


for n in degrees:
    Pn = legendre(n)
    ax.plot(x,Pn(x),label=f'n = {n}')


ax.set_title('Полиномы Лежандра')

ax.legend(loc='upper right',bbox_to_anchor=(1.15,1))

plt.show()