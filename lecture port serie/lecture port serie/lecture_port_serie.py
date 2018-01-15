from serial import *
ser=Serial('COM6',115200,timeout=0)
if ser.isOpen():
    while True:
        ligne=ser.readline()
        print(ligne)

