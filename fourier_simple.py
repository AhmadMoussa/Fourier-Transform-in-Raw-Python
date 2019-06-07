import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-8*np.pi, 8*np.pi, 2000)
sin1 = np.sin(u) + 2
#plt.plot(u, sin1)

fig = plt.figure(figsize = (8,7))
ax = fig.add_subplot(111)

L = len(sin1)
real = []
imag = []
for val in np.arange(0.00001,360,0.00001):
    real = []
    imag = []
    for t,si in zip(np.arange(0,L,val),sin1):
        complex = si * np.e ** (2 * np.pi * 1j * t)
        real.append(complex.real)
        imag.append(complex.imag)

    ax = plt.plot(real, imag, 'b-')
    plt.pause(0.00001)
    plt.cla()

ax = plt.plot(real, imag, 'b-')
plt.show()
