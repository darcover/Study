import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig,(ax1,ax2,ax3)=plt.subplots(3,1,figsize=(8,12))

x=np.linspace(0,10,1000)

def update(val):
    amp1=slider_amp1.val
    freq1=slider_freq1.val
    amp2=slider_amp2.val
    freq2=slider_freq2.val
    wave1=amp1*np.sin(freq1*x)
    wave2=amp2*np.sin(freq2*x)
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax1.plot(x,wave1)
    ax2.plot(x,wave2)
    ax3.plot(x,wave1+wave2)
    ax1.set_title('Волна 1')
    ax2.set_title('Волна 2')
    ax3.set_title('Сумма волн')
    plt.draw()

slider_ax1 = plt.axes([0.2,0.01,0.65,0.03])
slider_amp1= Slider(slider_ax1,'Амплитуда 1',0.1,10.0,valinit=1)
slider_ax2= plt.axes([0.2,0.05,0.65,0.03])

slider_freq1 =Slider(slider_ax2,'Частота 1',0.1,10.0,valinit=1)
slider_ax3 =plt.axes([0.2,0.09,0.65,0.03])
slider_amp2=Slider(slider_ax3,'Амплитуда 2',0.1,10.0,valinit=1)

slider_ax4=plt.axes([0.2,0.13,0.65,0.03])
slider_freq2=Slider(slider_ax4,'Частота 2',0.1,10.0,valinit=1)

slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

update(None)
plt.show()