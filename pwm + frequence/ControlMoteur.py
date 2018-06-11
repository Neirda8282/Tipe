import serial
import csv
from time import clock
from pylab import plot,show


#ser1 = serial.Serial('com15',115200,timeout=0) # port com de la due
ser2 = serial.Serial('com10',9600,timeout=0) # port com de la uno

ser2.write(str(7).encode('Latin-1'))


def decode(R):
    R2 = []
    for r in R:
        R2.append(r.decode('Latin-1'))

    while '' in R2:
        T.remove(T[R2.index('')])
        R2.remove('')
    R3 = []
    for r in R2:
        try:
            R3.append(float(r))
        except:
            R3.append(0)
    return R3


def conversion(l,F):  # convertit liste en csv

    file = open(F, 'w', )

    ecriture = csv.writer(file, dialect='excel', delimiter=';')
    ecriture.writerow(['Temps' , 'frequence'])
    for i in range(len(l[0]) - 1):
        ecriture.writerow([l[0][i], l[1][i]])
    file.close()


print("valeurs initial du rapport cyclique de la pwn 7 max 17")
while True:
    T=[]
    val = int(input("lancer le programme avec un saut de rapport de (max :10) :  "))
    R=[]
    t=clock
    ser2.write(str(val).encode('Latin-1'))
    while t<30:
        t1=clock()
        R.append(ser1.readline())
        t2=clock()
        t=t+t2-t1
        T.append(t)
    R=decode(R)
    plot(T,R)
    fichier='test saut'+str(val)+'.csv'
    conversion([T,R],fichier)






