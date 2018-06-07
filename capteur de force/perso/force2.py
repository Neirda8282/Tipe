import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

it=pyfirmata.util.Iterator(board)
it.start()

pin=board.get_pin('a:1:i')
while True:
    print(pin.read())
    time.sleep(0.01)

 