import csv
from pylab import *
from mpl_toolkits.mplot3d import Axes3D



def conversion(l): # convertit liste en csv

    file=open("solidnaca.txt",'w',)
    
    ecriture=csv.writer(file,dialect='excel',delimiter=',')
    for i in range (len (l[0])-1):
        ecriture.writerow([l[0][i],l[1][i],l[2][i]]) 
    file.close()

file=open('naca12.csv','r')
#file.readline() #lis la 1e ligne( celle des textes)
x,y=[],[]
fichier=csv.reader(file, delimiter=';')
for ligne in fichier:
    x.append(float(ligne[0]))
    y.append(float(ligne[1]))

#plot(x,y)
#show()

# d=0.00829231
# h=d/len(y)

z=y.copy()
y=x.copy()
x=[0 for i in range(len(y))]

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
show()

# for i in range (len(z)):
#     z[i]=z[i]*10**-2
#
# for i in range(int(len(z)/2)):
#     y[i]=(len(y)-i)*h*10**-2
# for i in range(int(len(z)/2)+1,len(z)):
#     y[i]=i*h*10**-2
    

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
xlabel('x')
ylabel('y')
show()

L=[x,y,z]
conversion(L)
