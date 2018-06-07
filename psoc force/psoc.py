import serial
import csv
from numpy import mean
from time import clock
from pylab import plot, show, figure

ser = serial.Serial('com9', 9600, timeout=0)


def leplusfrequent(L):
    """Retourne l'élément le plus fréquent de la liste"""
    L.sort()  # pour que les éléments identiques soient assemblés
    n0, e0 = 0, None  # pour conserver le plus fréquent
    ep = None  # stocke l'élément distinct de la boucle précédente
    for e in L:
        if e != ep:  # si l'élément e a déjà été rencontré, on ne fait rien
            n = L.count(e)
            if n > n0:
                n0, e0 = n, e  # on stocke le nouvel élément le plus fréquent
            ep = e  # on stocke l'élément courant pour la boucle suivante
    return e0


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

    print(i)
    # print(R1,len(R1))
    # print(R2,len(R2))
    # print(mean(R1), mean(R2))
    # print(leplusfrequent(R1), leplusfrequent(R2))
    return [mean(R1), leplusfrequent(R1), mean(R2), leplusfrequent(R2)]


def prog():
    while True:
        Tmax = int(input("durée acquisition : "))
        pas = float(input("pas de mesure : "))
        t = 0
        T = []
        R1m, R1L, R2m, R2L = [], [], [], []
        while t < Tmax:
            t1 = clock()
            R = acquisition(pas)
            t2 = clock()
            t = t + t2 - t1
            T.append(t)
            R1m.append(R[0])
            R1L.append(R[1])
            R2m.append(R[2])
            R2L.append(R[3])
        plot(T, R1m, ':r', T, R1L, '*r', T, R2m, ':g', T, R2L, '*g')
        show()


def test():
    """test pour verifier la répétabilité de la mesure afin d'étalonner les capteurs
    permet de faire n mesure avec un pas de calcul de t et affiche la valeur moyenne et la valeur la plus frequente de l'acquisition

    """
    n = int(input('nombre de mesure : '))
    pas = float(input("pas de mesure : "))
    for i in range(n):
        R = acquisition(pas)
        print("valeur moyenne capteur 1 :", R[0], "; valeur la plus frequente du capteur 1 : ", R[1],
              "valeur moyenne capteur 2 :", R[2], "; valeur la plus frequente du capteur 2 : ", R[3])


# test()  #test pour verifier la répétabilité de la mesure afin d'étalonner les capteurs
# prog()  # prog pour faire une acquisition pendant un certain temps et voir l'evolution de la valeur

def conversion(l, F):  # convertit liste en csv

    file = open(F, 'w', )

    ecriture = csv.writer(file, dialect='excel', delimiter=';')
    ecriture.writerow(['Masse', 'Volts'])
    for i in range(len(l[0]) - 1):
        ecriture.writerow([l[0][i], l[1][i]])
    file.close()


def etalonage():
    M = [0]
    Rm = []
    Rf = []
    R1 = []
    R2 = []
    ok = True
    print("mesure initiale")
    for i in range(1):
        R = acquisition(0.01)
        R1.append(R[2])
        R2.append(R[3])
    Rm.append(mean(R1))
    Rf.append(mean(R2))
    print("fin mesure valeur initial")
    while ok:
        m = float(input("masse ajouter (g): "))
        if m != -1:
            M.append(M[-1] + m)
            for i in range(1):
                R = acquisition(0.01)
                R1.append(R[2])
                R2.append(R[3])
            Rm.append(mean(R1))
            Rf.append(mean(R2))
        else:
            ok = False

    F1 = 'Votlsmoyennecapteur2test2.csv'
    conversion([M, Rm], F1)
    F2 = 'VoltsFrequencecapteur2test2.csv'
    conversion([M, Rf], F2)
    figure(0)
    plot(M, Rm)
    show()
    figure(1)
    plot(M, Rf)
    show()
    return M, Rm, Rf


etalonage()
