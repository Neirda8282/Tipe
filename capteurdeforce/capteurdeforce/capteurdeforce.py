import pyfirmata 
port = 'COM27' #windows


board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)  # itérateur permet de ne pas engorger 
                                     # la communication série
it.start()

pinA0 = board.get_pin('a:1:i')   # a = analogique, 0 = numéro de la pin, i = input.


while True:
    print(pinA0.read())	      # la valeur varie entre 0 et 1.    
    