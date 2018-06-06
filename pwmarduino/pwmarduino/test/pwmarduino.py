import pyfirmata

port = 'com27'

board=pyfirmata.Arduino(port)

LEDpin = board.get_pin('d:3:p')

def  reglageMoteur(valeur):
        board.digital[LEDpin.pin_number].write(float(valeur))
while True:
    valeur=float(input('valeurmoteur'))
    try:
        reglageMoteur(valeur)
    except:
        break