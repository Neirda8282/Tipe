#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Contrôle de la luminosité d'une LED l'Arduino
à partir d'un PC au moyen du protocole Firmata
Interface graphique (Tkinter)
"""

from Tkinter import *
import pyfirmata

pin1 = 2
pin2 = 3
pin3 = 4

port = 'COM27'            #windows
#port = '/dev/ttyACM0'   #linux

board = pyfirmata.Arduino(port)

LEDpin = board.get_pin('d:3:p') #on règle la pin 11 en mode PWM

# S'exécute lors d'un changement du slider:
def reglageLED(valeur):
    board.digital[LEDpin.pin_number].write(float(valeur)/100.0)

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("LED") #titre de la fenêtre

        self.pack(fill=BOTH, expand=1)
     
        # Label (le texte dans la fenêtre):
        w = Label(self, wraplength = 200, pady = 10, text="Veuillez glisser le curseur pour contrôler la luminosité de la LED")
        w.pack()

        # Curseur:
        self.var1 = IntVar()      
        w2 = Scale(self, from_=0, to=100, orient=HORIZONTAL, command = reglageLED)
        w2.pack()


def main():
  
    root = Tk()
    root.geometry("250x200+300+300")  # dimension et position initiale de la fenêtre
    app = Example(root)
    root.mainloop()  

if __name__ == '__main__':
    main()