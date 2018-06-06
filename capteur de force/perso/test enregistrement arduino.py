import pyfirmata
from pylab import *
from time import clock
from csv import *

port = 'COM4'

board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)

it.start()

pin5=board.get_pin('d:5:i')





D = int(input("durée de l'acquisition en s : "))

R = []
T = []
t1 = clock()
t = t1
while t <= D:
    t2 = clock()
    R.append(pin5.read())

    T.append(t)
    t3 = clock()
    t = t + t3 - t2

#print(R, T)
plot(T,R)
show()