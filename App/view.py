import os
import sys
import App.logic as logic

def main():
    """
    Menu principal
    """
    working = True
    while working:
        inputs = input("Ingresa un string de comandos: ")
        # Para iniciar el juego primero se tiene que crear una matriz con el tamaño dado por el usuario
        if inputs == "START":
            tamanio=int(input("Ingrese el tamaño de la matriz que se desea generar: "))
            matriz=logic.crear_matriz(tamanio)   
                    
        if int(inputs) == 0:
            working = False
            print("Gracias por utilizar el robot") 
    sys.exit(0)
    