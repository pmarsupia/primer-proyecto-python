# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#Creo el vector X con 1,000 elementos de 0 a 1
x = np.linspace(0, 1,num=1000)

#A partir del vector X creo los vectores Y, Z, W y T
y = np.sin(4 * np.pi * x)
z = np.cos(4 * np.pi * x)
w = np.cos(4 * np.pi * x) + 1
t = np.cos(4 * np.pi * x) -1

#Si quiero dibujar sólo la primera gráfica
plt.figure(1)
plt.plot(x,y,'-',label='sin(X)')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.legend(loc='upper right')
plt.annotate('Hola', xy=(0.4,0.5))
plt.savefig('plot_sin.png')

#Si quiero bibujar la segunda gráfica
#plt.figure(2)
#plt.plot(x,z)

#Si quiero dibujar las dos líneas en una misma gráfica
#plt.figure(3)
#plt.plot(x,y,x,z)

#Si quiero las 4 gráficas en una misma figura
#plt.figure(4)
#plt.subplot(221) #2 rows, 2 column, select first one 
#plt.plot(x,y)
#plt.subplot(222) #2 rows, 2 column, select second one 
#plt.plot(x,z)
#plt.subplot(223) #2 rows, 2 column, select third one 
#plt.plot(x,w)
#plt.subplot(224) #2 rows, 2 column, select fouth one 
#plt.plot(x,t)

plt.show() # Muestra todas las figuras que hayas hecho