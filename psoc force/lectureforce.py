import serial
import csv
from numpy import mean, exp
from time import clock
from pylab import plot, show, figure

ser = serial.Serial('com9', 9600, timeout=0)


def conversion(l, F):  # convertit liste en csv

    file = open(F, 'w', )

    ecriture = csv.writer(file, dialect='excel', delimiter=';')
    ecriture.writerow(['Masse', 'Volts'])
    for i in range(len(l[0]) - 1):
        ecriture.writerow([l[0][i], l[1][i]])
    file.close()


def acquisition(pas):
    R1 = []
    R2 = []
    t = 0

    while t < pas:
        i = 0
        t1 = clock()
        b = ser.readline().decode('Latin-1')

        if b != '':
            # print(b)
            B = b.split(';')
            # print(B)
            try:
                R1.append(int(B[0]))
                R2.append(int(B[1]))
                t2 = clock()
                t = t + t2 - t1

            except:
                i += 1

    # print(i)
    # print(R1,len(R1))
    # print(R2,len(R2))
    # print(mean(R1), mean(R2))
    # print(leplusfrequent(R1), leplusfrequent(R2))
    return [mean(R1), mean(R2)]


def prog():
    while True:
        Tmax = int(input("durée acquisition : "))
        pas = 0.01
        t = 0
        T = []
        R1m, R2m = [], []
        while t < Tmax:
            t1 = clock()
            R = acquisition(pas)
            t2 = clock()
            t = t + t2 - t1
            T.append(t)
            R1m.append(R[0])

            R2m.append(R[1])

        plot(T, R1m, ':r', T, R2m, ':g')
        show()


def capteur1(v):
    f = 0.00993 * exp(0.02513 * v)
    return f


def capteur2(v):
    f = 0.04857 * exp(0.01578 * v)
    return f


def force():
    while True:
        try:
            valeur = acquisition(0.01)
            f1, f2 = capteur1(valeur[0]), capteur2(valeur[1])
            print("force capteur 1 : ", f1)
            print("force capteur 2 : ", f2)
        except KeyboardInterrupt:
            print("fin programme")


# prog()
force()
