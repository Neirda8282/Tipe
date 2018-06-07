import serial
ser=serial.Serial('com15',9600,timeout=0)
while True:
    try :
        valeurs=int(input('rapport cyclique : '))
        valeurs=str(valeurs)
        ser.write(valeurs.encode('Latin-1'))
    except:
        break
    