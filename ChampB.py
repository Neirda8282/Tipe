import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d.axes3d import Axes3D


Longueur=np.linspace(0,0.03,1000)
Rayon=np.linspace(0.01,0.20,1000)
mu = 12.566370614*10**-7
I = 10

def ChampB(R,L):
    x = mu*I*R**2/(2*(np.sqrt(R**2+L**2))**3)
    return x

#def sommechampB(R,L):
#    r=0
#    Btot=np.zeros((1000,1000))
#    for i in range(len(Rayon)):
#        B=[0 for k in range(1000)]
#        print(B)
#        while r<Rayon[i]:
#            B=B+ChampB(r,L)
#            r+=1.01902
#            print(B)
#        Btot.insert(i,B)
       
Rayon1 , Longueur1 = np.meshgrid(Rayon,Longueur)
B = ChampB(Rayon1,Longueur1)
B1 = ChampB(Rayon1,Longueur1)
for i in range(1,1000):
    B[:,i]=B[:,i]+B[:,i-1]

fig=pl.figure()
ax = pl.axes(projection='3d')
ax.plot_wireframe(Rayon1,Longueur1,B,color='red')
ax.set_xlabel('Rayon')
ax.set_ylabel('Distance')
ax.set_zlabel('Champ B')



fig1=pl.figure()
ax1 = pl.axes(projection='3d')
ax1.plot_wireframe(Rayon1,Longueur1,B1,color='red')
ax1.set_xlabel('Rayon')
ax1.set_ylabel('Distance')
ax1.set_zlabel('Champ B')
pl.show()