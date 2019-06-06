import numpy as np
import matplotlib.pyplot as plt
import cmath
import itertools

#shifting the sinewaves can be done by altering the starting and ending values of the linspace
u = np.linspace(-8*np.pi, 8*np.pi, 1000)
u2 = np.linspace(-4*np.pi, 4*np.pi, 1000)
u3 = np.linspace(-2*np.pi, 2*np.pi, 1000)
u4 = np.linspace(-16*np.pi, 16*np.pi, 1000)

sin1 = np.sin(u)
sin2 = np.sin(u2)*1/2
sin3 = np.sin(u3)*1.4
sin4 = np.sin(u4)*0.6

fig, (waves, sum) = plt.subplots(nrows = 2, ncols = 1)
# Amplitude can be controlled by multiplying or dividing the y coordinates of the ploted values
# Frequency can be controlled by multiplying or dividing the x coordinates of the ploted values
waves.plot(u, sin1)
waves.plot(u2*2, sin2)
waves.plot(u3*4, sin3)
waves.plot(u4/2, sin4)
waves.axis('tight')

sumu = u + u2*2 + u3*4 +u4
sumsin = sin1 + sin2 + sin3 + sin4

sum.plot(sumu, sumsin)
fig.set_size_inches(20,10)
#plt.show()

plt.clf()
real = []
imag = []
I = len(sumsin)
for i, (su,si) in enumerate(zip(sumu,sumsin)):
    complex = (su) * np.e ** (-2j * np.pi * si * i/I)
    real.append(complex.real)
    imag.append(complex.imag)

fig.set_size_inches(10,10)
plt.plot(real, imag, 'b-')
plt.show()
