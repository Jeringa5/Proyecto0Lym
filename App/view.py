import os
import sys
import App.logic as logic
import App.parser as parser

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def main():
    """
    Menu principal
    """
    working = True
    while working:
        print("-------------------------------------")
        print("0. Salir")
        print("1. Analizador sintáctico (Parser)")
        print("-------------------------------------")
        inputs = int(input("Ingrese una opcion: "))

        # Ejecutar el parser
        if int(inputs)==1:
            while True:
                nombre_archivo=input("Ingrese el nombre del archivo .txt: ")
                print("---------------------------------------------")
                if nombre_archivo.endswith('.txt'):
                    archivo=data_dir+nombre_archivo
                    try:
                        with open(archivo, 'r') as file:
                            linea=file.readlines()
                            break
                    except FileNotFoundError:
                        print(f"Error: El archivo '{nombre_archivo}' no existe. Inténtelo de nuevo.")
                    
            if parser.parse(linea):
                print("La sintaxis es correcta")
            else:
                print("Se encontraron errores de sintaxis")
                    
        # Salir de la aplicación
        if int(inputs) == 0:
            working = False
            print("Gracias por utilizar el robot") 
    sys.exit(0)
    