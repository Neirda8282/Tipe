import csv
from pylab import *

def conversion(l): # convertit liste en csv

    file=open("capteur1.txt",'w',)
    
    ecriture=csv.writer(file,dialect='excel',delimiter=',')
    for i in range (len (l[0])-1):
        ecriture.writerow([l[0][i],l[1][i]]) 
    file.close()

file=open('exp.csv','r')
#file.readline() #lis la 1e ligne( celle des textes)
m,v=[],[]
fichier=csv.reader(file, delimiter=';')
label=file.readline()
for ligne in fichier:
    i=0
    #print(ligne)
    try :
        m.append(float(ligne[0]))
        v.append(float(ligne[1]))
    except:
        i+=1

print(i)
plot(v,m)
show()
for i in range(len(v)):
    v[i]=-v[i]
#print(y)

close()
#y=-y
plot(v,m)
show()
g=9.81
f=[(M*10**-3)*g for M in m]

plot(v,f,':')
xlabel('microvolt sorti psoc')
ylabel('force en N')
legend()
show()

conversion([v,f])

