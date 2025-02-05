import os
import sys
import App.logic as logic

def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        inputs = input("Ingresa un string de comandos: ")
        if int(inputs) == 0:
            working = False
            print("Gracias por utilizar el robot") 
    sys.exit(0)
    