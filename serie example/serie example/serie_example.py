import serial
from time import clock
from pylab import plot,show
ser = serial.Serial('com15', 115200, timeout=0)
t=0
R=[]
t=clock()
T=[t]

while t<5:
 try:
    t1=clock()
    R.append(ser.readline())
    t2=clock()
    t=t+t2-t1
    T.append(t)
     



 
 except ser.serialtimeoutexception:
  print('data could not be read')


#print(type(R[0]))
#print(R)

#R=[b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'453\r\n', b'0\r\n', b'0\rS\xd34\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'453\r\n', b'0\r\n', b'0\rS\xd34\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'454\r\n', b'462\r\n', b'0\r\n', b'454\r\n', b'0\r\n', b'0\r\n', b'453\r\n', b'462\r\n', b'0\r\n', b'453\r\n', b'0\r\n', b'0\rS\xd3', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'']
R2=[]
for r in R:
    R2.append(r.decode('Latin-1'))

while '' in R2:
    T.remove(T[R2.index('')])
    R2.remove('')
R3=[]
for r in R2:
    try:
        R3.append(float(r))
    except :
        R3.append(0)


print(R3)
T.pop()
plot(T,R3)
show()
#

