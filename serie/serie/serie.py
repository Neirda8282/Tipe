import serial
portserie=serial.Serial('COM',115200,timeout=0)
while 1:
    try :
        print(portserie.readline())
