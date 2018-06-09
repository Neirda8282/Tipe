from pylab import plot, show, linspace, concatenate
import csv


def Cb(x):
    p1 = -0.00014466
    p2 = 0.00053971
    p3 = 0.0021517
    p4 = -0.0010476
    p5 = -0.0054203
    p6 = 0.00025366
    p7 = 0.003779
    p8 = 0.0019848
    p9 = 0.0018452
    p10 = -0.0036385
    p11 = -0.0067363
    mu = 0.052975
    sigma = 0.035511
    z = (x - mu) / sigma

    y = p1 * z ** 10 + p2 * z ** 9 + p3 * z ** 8 + p4 * z ** 7 + p5 * z ** 6 + p6 * z ** 5 + p7 * z ** 4 + p8 * z ** 3 + p9 * z ** 2 + p10 * z + p11
    return y

def Ch(x):
    # Coefficients:
    p1 = -8.5741e-05
    p2 = -0.00017874
    p3 = 0.00019112
    p4 = 0.00081124
    p5 = 3.3946e-05
    p6 = -0.0010828
    p7 = 7.1132e-05
    p8 = 5.1912e-05
    p9 = -0.0022661
    p10 = 0.00076789
    p11 = 0.0076716
    mu = 0.04535
    sigma = 0.032905
    z = (x - mu) / sigma

    y = p1 * z ** 10 + p2 * z ** 9 + p3 * z ** 8 + p4 * z ** 7 + p5 * z ** 6 + p6 * z ** 5 + p7 * z ** 4 + p8 * z ** 3 + p9 * z ** 2 + p10 * z + p11
    return y


def conversion(l, F):  # convertit liste en csv

    file = open(F, 'w', )

    ecriture = csv.writer(file, dialect='excel', delimiter=',')
    # ecriture.writerow(['X', 'Y', 'Z'])
    for i in range(len(l[0]) - 1):
        ecriture.writerow([l[0][i], l[1][i], l[2][i]])
    file.close()


Xb = linspace(0, 0.101, 1000)
Xh = Xb
Yb = Cb(Xb)
Yh = Ch(Xh)

Xb=[x*10**3 for x in Xb]
Xh=[x*10**3 for x in Xh]
Yb=[y*10**3 for y in Yb]
Yh=[y*10**3 for y in Yh]

plot(Xb, Yb, Xh, Yh)
show()

Zb = [0 for k in range(len(Xb))]
Zh = Zb

Lh = [Xh, Yh, Zh]
conversion(Lh, 'pointhaut.txt')

Lb = [Xb, Yb, Zb]
conversion(Lb, 'pointbas.txt')

X = concatenate((Xb, Xh))
Y = concatenate((Yb, Yh))
Z = concatenate((Zb, Zh))
L = [X, Y, Z]
conversion(L, 'point.txt')
