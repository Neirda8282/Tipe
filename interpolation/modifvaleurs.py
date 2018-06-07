from numpy import *
from pylab import *
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


X = linspace(0, 0.1, 1000)
Yb = Cb(X)
Yh = Ch(X)
plot(X, Yb, X, Yh)
#show()


def angle(X, Yb, Yh, angle1, angle2, angle3):
    d1=0.02
    d2=0.06
    Zh = []
    theta1=angle1*pi/180
    theta2=angle2*pi/180
    theta3=angle3*pi/180
    for i in range(len(X)):
        if X[i] < d1:
            Zh.append(tan(theta1) * (Yh[i] - Yb[i]))
        elif d1 < X[i] < d2:
            Zh.append(tan(theta2) * (Yh[i] - Yb[i]))
        else:
            Zh.append(tan(theta3) * (Yh[i] - Yb[i]))
    return Zh

Zb=[0 for k in range(len(X))]
Zh = angle(X, Yb, Yh, 13, 14, 15)

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(X, Yh, Zh)
ax.plot(X,Yb,[0 for k in range(len(X))])
xlabel('x')
ylabel('y')
#show()

Xh,Yh,Zh=meshgrid(X,Yh,Zh)


ax.plot(X,Yh,Zh)
#ax.plot(X,Yb,Zb)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

show()
