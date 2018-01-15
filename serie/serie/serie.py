import serial
portserie=serial.Serial('COM5',115200,timeout=0)
while 1:
    try :
        print(portserie.readline())
