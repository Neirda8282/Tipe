from numpy import *
from pylab import *
import csv
from mpl_toolkits.mplot3d import Axes3D


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


Xb = linspace(0, 0.101, 1000)
Xh = Xb
Yb = Cb(Xb)
Yh = Ch(Xh)
#plot(Xb, Yb, Xh, Yh)


# show()
# R=[]
# for i in range(len(Yb)):
#     R.append(abs(Yb[i]-Yh[i]))
#
# I=R.index(min(R))




def angle(X, Yb, Yh, angle1, angle2, angle3):
    d1 = 0.02
    d2 = 0.06
    Zh = []
    theta1 = angle1 * pi / 180
    theta2 = angle2 * pi / 180
    theta3 = angle3 * pi / 180
    for i in range(len(X)):
        if X[i] < d1:
            Zh.append(tan(theta1) * (Yh[i] - Yb[i]))
        elif d1 < X[i] < d2:
            Zh.append(tan(theta2) * (Yh[i] - Yb[i]))
        else:
            Zh.append(tan(theta3) * (Yh[i] - Yb[i]))
    return Zh

#
# [XB, YB] = meshgrid(Xb, Yb)
# [XH, YH] = meshgrid(Xh, Yh)
#
Zb = [0 for k in range(len(Xb))]
Zh = Zb

#d=mean(Zh[:198])/198
#for i in range(199):
#    Zb[i]=d*(198-i)


# n=100

# D=Zh[I]
# d=D/n
# C=0
# for i in range(I-n,len(Zb)):
#     Zb[i]=d*C
#     C+=1

    
def conversion(l, F):  # convertit liste en csv

    file = open(F, 'w', )

    ecriture = csv.writer(file, dialect='excel', delimiter=',')
    #ecriture.writerow(['X', 'Y', 'Z'])
    for i in range(len(l[0]) - 1):
        ecriture.writerow([l[0][i], l[1][i], l[2][i]])
    file.close()


Lh = [Xh, Yh,Zh]
conversion(Lh, 'pointhaut.txt')

Lb = [Xb, Yb,Zb]
conversion(Lb, 'pointbas.txt')

X=concatenate((Xb,Xh))
Y=concatenate((Yb,Yh))
Z=concatenate((Zb,Zh))

L=[X,Y,Z]
conversion(L, 'point.txt')

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(Xh, Yh, Zh)
ax.plot(Xb,Yb,Zb)
xlabel('x')
ylabel('y')
#show()
#
# Xh,Yh,Zh=meshgrid(X,Yh,Zh)
#
#
# ax.plot(X,Yh,Zh)
# ax.plot(X,Yb,Zb)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# show()


def S(x,y):

    p00 = 0.002118
    p10 = -0.1458
    p01 = -0.01259
    p20 = 5.277
    p11 = 18.41
    p30 = -71.22
    p21 = -484.2
    p40 = 431.1
    p31 = 5328
    p50 = -1135
    p41 = -2.092e+04
    S = p00 + p10 * x + p01 * y + p20 * (x ** 2) + p11 * x * y + p30 * (x ** 3) + p21 * (x ** 2) * y + p40 * (x ** 4) + p31 * (x ** 3) * y + p50 * (x ** 5) + p41 * (x ** 4) * y

    return S

X=linspace(0,0.102,1000)
Y=linspace(-0.008,0.008,1000)
Z=S(X,Y)

X,Y=meshgrid(X,Y)


ax.plot(X,Y,Z)
# ax.plot(X,Yb,Zb)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

show()
