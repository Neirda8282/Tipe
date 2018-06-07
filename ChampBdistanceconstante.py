import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d.axes3d import Axes3D


Longueur=0.02
Rayon=np.linspace(0.001,0.20,1000)
mu = 12.566370614*10**-7
I =np.linspace(0,100,1000)

def ChampB(R,I):
	x = mu*I*R**2/(2*(np.sqrt(R**2+Longueur**2))**3)
	return x

Rayon1 , Intensite1 = np.meshgrid(Rayon,I)
B = ChampB(Rayon1,Intensite1)
B1 = ChampB(Rayon1,Intensite1)
for i in range(1,1000):
    B[:,i]=B[:,i]+B[:,i-1]

fig=pl.figure()
ax = pl.axes(projection='3d')
ax.plot_wireframe(Rayon1,Intensite1,B,color='red')
ax.set_xlabel('Rayon')
ax.set_ylabel('Intensité')
ax.set_zlabel('Champ B')

fig1=pl.figure()
ax1 = pl.axes(projection='3d')
ax1.plot_wireframe(Rayon1,Intensite1,B1,color='red')
ax1.set_xlabel('Rayon')
ax1.set_ylabel('Intensité')
ax1.set_zlabel('Champ B')
pl.show()
